from numpy import random
from matplotlib import pyplot as plt 
import timeit
from functools import partial
from Trees import Node, BinarySearchTree, AVLTree


arr = random.randint(low = 1, high = 30000, size = 10000)

list_of_lists = []
number_of_elements = []

BST_create_time = []
AVL_create_time = []

BST_find_time = []
AVL_find_time = []

for n in range(0, len(arr) - 1, 1000):
    list_of_lists.append(arr[:n])

for n in list_of_lists:
    number_of_elements.append(len(n))

avl_tree = AVLTree(arr)
bst_tree = BinarySearchTree(arr)


for small_list in list_of_lists:
    BST_time = partial(BinarySearchTree, small_list)
    BST_create_time.append(timeit.timeit(BST_time, number=1))
    
    AVL_time = partial(AVLTree, small_list)
    AVL_create_time.append(timeit.timeit(AVL_time, number=1))

    BST_find = 0
    AVL_find = 0
    for element in small_list:
        search_bst = partial(bst_tree.findNode, element)
        BST_find += timeit.timeit(search_bst, number=1)
        
        search_avl = partial(avl_tree.findNode, element)
        AVL_find += timeit.timeit(search_avl, number=1)
        
    BST_find_time.append(BST_find)
    AVL_find_time.append(AVL_find)

print(number_of_elements)
print(BST_create_time)


with open("trees_output.txt", "w") as out:
    time_iterator = 0
    for small_list in list_of_lists:
        out.write("Number of elements: {:d}\n".format(len(small_list)))
        out.write("Binary Search Tree construdction time: {:f}s\n".format(BST_create_time[time_iterator]))
        out.write("AVL Tree construdction time: {:f}s\n".format(AVL_create_time[time_iterator]))
        out.write("Binary Search Tree search time: {:f}s\n".format(BST_find_time[time_iterator]))
        out.write("AVL Tree search time: {:f}s\n".format(AVL_find_time[time_iterator]))
        out.write("\n\n")
        time_iterator += 1


fig1, ax1 = plt.subplots(nrows = 3, ncols = 1, figsize = (6, 7))
fig1.suptitle("Trees' Creation Time", fontsize = 16)
ax1[0].plot(number_of_elements, BST_create_time, "b")
ax1[1].plot(number_of_elements, AVL_create_time, "g")

ax1[2].plot(number_of_elements, BST_create_time, "b")
ax1[2].plot(number_of_elements, AVL_create_time, "g")
ax1[2].legend(["BST tree", "AVL tree"], loc = 2)

ax1[2].set_ylabel("Time in seconds of creating BST and AVL Tree")
ax1[2].set_xlabel("Number of elements in tree")

fig2, ax2 = plt.subplots(nrows = 3, ncols = 1, figsize = (6, 7))
fig2.suptitle("Trees' Searching Time", fontsize = 16)
ax2[0].plot(number_of_elements, BST_find_time, "b")
ax2[1].plot(number_of_elements, AVL_find_time, "g")

ax2[2].plot(number_of_elements, BST_find_time, "b")
ax2[2].plot(number_of_elements, AVL_find_time, "g")
ax2[2].legend(["BST tree", "AVL tree"], loc = 2)

ax2[2].set_ylabel("Time in seconds of finding the node in BST and AVL Tree")
ax2[2].set_xlabel("Number of elements in tree")


for sub in ax1, ax2:
    for subb in sub:
        subb.grid(True)

plt.show()

fig1.savefig('Create_time.png')   
fig2.savefig('Search_ime.png') 

plt.close(fig1)
plt.close(fig2)
