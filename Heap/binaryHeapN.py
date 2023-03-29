# Python3 implementation of Min Heap

from numpy import random

class MinHeap:

    def __init__(self, d):
        self.d = d
        self.size = 0
        self.Heap = []
     

    # Function to return the position of parent for the node currently at pos
    def parent(self, pos):
        return (pos-1) // self.d

    # Function to return the position of the left child for the node currently at pos
    def leftChild(self, pos):
        return self.d * pos + 1

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def up_heap(self, pos):
        while pos != 0 and self.Heap[self.parent(pos)] > self.Heap[pos]:
            self.swap(self.parent(pos), pos)
            pos = self.parent(pos)

    def down_heap(self, pos):
        while self.leftChild(pos) < self.size:
            j = self.leftChild(pos)
            k=j
            for i in range(1, self.d + 1): 
                if k+i < self.size and self.Heap[k+i] < self.Heap[j]:
                    j = k+i
            if self.Heap[pos] < self.Heap[j]:
                break
            self.swap(pos, j)
            pos = j

    def top(self):
        return self.Heap[0]

    def push(self, value):
        self.Heap.append(value)
        self.size += 1
        self.up_heap(self.size-1)

    def pop(self):
        root = self.top()
        self.size -= 1
        self.Heap[0] = self.Heap.pop()
        self.down_heap(0)
        return root
        
    # Function to print the contents of the heap
    def print(self):
        for i in range(0, (self.size // self.d) + 1):
            line = " PARENT: " + str(self.Heap[i]) + " CHILDS: "
            for j in range(1, self.d + 1):
                if self.d * i + j > self.size - 1:
                    break
                line = line + str(self.Heap[self.d * i + j]) + ", "
            print(line)


    def display(self, k):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.leftChild(k)+1 > self.size-1 and self.leftChild(k) > self.size-1:
            line = f"{self.Heap[k]}"  # key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.leftChild(k)+1 > self.size-1:
            lines, n, p, x = self.display(self.leftChild(k))
            s = f"{self.Heap[k]}"  # key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.leftChild(k) > self.size-1:
            lines, n, p, x = self.display(self.leftChild(k)+1)
            s = f"{self.Heap[k]}"  # key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.display(self.leftChild(k))
        right, m, q, y = self.display(self.leftChild(k)+1)
        s = f"{self.Heap[k]}"  # key
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


    def printHeap(self):
        if self.d != 2:
            pass
        lines, *_ = self.display(0)
        for line in lines:
            print(line)


# Driver Code
if __name__ == "__main__":
    print("Kopiec 2-arny")
    minHeap2 = MinHeap(2)
    random_list = [random.randint(1, 100) for _ in range(20)]
    for element in random_list:
        minHeap2.push(element)
    minHeap2.printHeap()
    print()
    minHeap2.print()
    print()
    print("USUWANIE")
    minHeap2.pop()
    minHeap2.printHeap()
    print()
    minHeap2.print()

    print()
    print("Kopiec 5-arny")
    minHeap5 = MinHeap(5)
    for element in random_list:
        minHeap5.push(element)
    minHeap5.print()
    print()
    print("USUWANIE")
    minHeap5.pop()
    minHeap5.print()

    print()
    print("Kopiec 7-arny")
    minHeap7 = MinHeap(7)
    for element in random_list:
        minHeap7.push(element)
    minHeap7.print()
    print()
    print("USUWANIE")
    minHeap7.pop()
    minHeap7.print()
