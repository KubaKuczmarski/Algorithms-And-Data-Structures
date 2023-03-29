class Node:
    def __init__(self, value=None, size=0):
        self.value = value
        self.left = None
        self.right = None
        self.size = size
        self.height = 0

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child
        if self.right is None and self.left is None:
            line = f"{self.value}" #key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = f"{self.value}" #key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = f"{self.value}" #key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = f"{self.value}" #key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2



class BinarySearchTree:
    def __init__(self, values=None):
        self.root = None
        if values is not None:
            for value in values:
                self.addNode(value)

    def display(self):
        lines, *_ = self.root._display_aux()
        for line in lines:
            print(line)

    def addNode(self, val):
        self.root = self._addNode(self.root, val)

    def _addNode(self, currentNode, val):
        if currentNode is None:
            node = Node(value=val)
            return node
        if val < currentNode.value:
            currentNode.left = self._addNode(currentNode.left, val)
        else:
            currentNode.right = self._addNode(currentNode.right, val)
        return currentNode

    def deleteNode(self, val):
        if val is None:
            raise Exception("Incorrect value")
        self.root = self._deleteNode(self.root, val)

    def _deleteNode(self, currentNode, val):
        if currentNode is None: 
            return None
        if val < currentNode.value:#
            currentNode.left = self._deleteNode(currentNode.left, val)
        elif val > currentNode.value:
            currentNode.right = self._deleteNode(currentNode.right, val)
        else: 
            # One/No child
            if currentNode.right is None:
                return currentNode.left
            if currentNode.left is None:
                return currentNode.right
            # Two children
            temp = currentNode
            currentNode = self.min(temp.right)  
            currentNode.right = self.deleteMin(temp.right) 
            currentNode.left = temp.left
        return currentNode


    def min(self, node):
        if node.left is None:
            return node
        else:
            return self.min(node.left)

    def deleteMin(self, node):
        if node.left is None:
            return node.right
        node.left = self.deleteMin(node.left)
        return node

    def findNode(self, val):
        return self._findNode(self.root, val)

    def _findNode(self, currentNode, val):
        if val is None:
            raise Exception("Incorrect value")
        if currentNode is None:
            return None
        if val == currentNode.value:
            return currentNode
        elif val < currentNode.value:
            return self._findNode(currentNode.left, val)
        elif val > currentNode.value:
            return self._findNode(currentNode.right, val)

    def displayTree(self):
        result = ""
        
        def VLR(result, currentNode):  
            if currentNode:
                if currentNode.value:
                    result += str(currentNode.value) + "-"
                    result = VLR(result, currentNode.left)
                    result = VLR(result, currentNode.right)
            return result

        def LVR(result, currentNode):
            if currentNode:
                if currentNode.value:
                    result = LVR(result, currentNode.left)
                    result += str(currentNode.value) + "-"
                    result = LVR(result, currentNode.right)
            return result

        def LRV(result, currentNode):
            if currentNode:
                if currentNode.value:
                    result = LRV(result, currentNode.left)
                    result = LRV(result, currentNode.right)
                    result += str(currentNode.value) + "-"
            return result
        print(VLR(result, self.root))
        print(LVR(result, self.root))
        print(LRV(result, self.root))


class AVLTree(BinarySearchTree):
    
    def _addNode(self, currentNode, val):
        currentNode = super()._addNode(currentNode, val)
        
        currentNode.height = max(self.getHeight(currentNode.left), self.getHeight(currentNode.right)) + 1
        
        balance = self.getBalance(currentNode)
        if balance < -1 and val < currentNode.left.value: # left left
            return self.rightRotate(currentNode)
        if balance > 1 and val > currentNode.right.value: # right right
            return self.leftRotate(currentNode)
        if balance < -1 and val > currentNode.left.value: # left right
            currentNode.left = self.leftRotate(currentNode.left)
            return self.rightRotate(currentNode)
        if balance > 1 and val < currentNode.right.value: # right left
            currentNode.right = self.rightRotate(currentNode.right)
            return self.leftRotate(currentNode)
        return currentNode

    def _findNode(self, currentNode, val):
        super()._findNode(currentNode, val)


    def getHeight(self, currentNode):
        if currentNode is None:
            return 0
        return currentNode.height

    def getBalance(self, currentNode):
        if currentNode is None:
            return 0
        return self.getHeight(currentNode.right) - self.getHeight(currentNode.left)


    def leftRotate(self, z):
        y = z.right
        T = y.left
        y.left = z
        z.right = T
        z.height = max(self.getHeight(z.left), self.getHeight(z.right)) + 1
        y.height = max(self.getHeight(y.left), self.getHeight(y.right)) + 1
        return y


    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = max(self.getHeight(z.left), self.getHeight(z.right)) + 1
        y.height = max(self.getHeight(y.left), self.getHeight(y.right)) + 1
        return y


