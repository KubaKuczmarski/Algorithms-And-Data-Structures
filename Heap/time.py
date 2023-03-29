import time
from binaryHeapN import MinHeap
from numpy import random
from matplotlib import pyplot as plt 
import timeit
from functools import partial

# Generowanie listy 100000 losowych liczb z zakresu od 1 do 300000
random_list = [random.randint(1,300000) for _ in range(100000)]

create_times_heap2 = []
create_times_heap5 = []
create_times_heap7 = []

n_values_create = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

for n in n_values_create:
    # Kopiec 2-arny
    start_time = time.time()
    minHeap2 = MinHeap(2)
    for element in random_list[:n]:
        minHeap2.push(element)
    create_times_heap2.append(time.time() - start_time)

    # Kopiec 5-arny
    start_time = time.time()
    minHeap5 = MinHeap(5)
    for element in random_list[:n]:
        minHeap5.push(element)
    create_times_heap5.append(time.time() - start_time)

    # Kopiec 7-arny
    start_time = time.time()
    minHeap7 = MinHeap(7)
    for element in random_list[:n]:
        minHeap7.push(element)
    create_times_heap7.append(time.time() - start_time)


# Mierzenie czasu wykonania n operacji usunięcia szczytu kopca
detele_times_heap2 = []
detele_times_heap5 = []
detele_times_heap7 = []

n_values_delete = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 99999]


for number in n_values_delete:
    # Kopiec 2-arny
    minHeap2 = MinHeap(2)
    for element in random_list:
        minHeap2.push(element)
    start_time = time.time()
    for n in range(number):
        minHeap2.pop()
    detele_times_heap2.append(time.time() - start_time)
    
    # Kopiec 5-arny
    minHeap5 = MinHeap(5)
    for element in random_list:
        minHeap5.push(element)
    start_time = time.time()
    for n in range(number):
        minHeap5.pop()
    detele_times_heap5.append(time.time() - start_time)
    
    
    # Kopiec 7-arny
    minHeap7 = MinHeap(7)
    for element in random_list:
        minHeap7.push(element)
    start_time = time.time()
    for n in range(number):
        minHeap7.pop()
    detele_times_heap7.append(time.time() - start_time)

fig1, ax1 = plt.subplots(nrows = 4, ncols = 1, figsize = (6, 7))
fig1.suptitle("Heap Creation Time", fontsize = 16)
ax1[0].plot(n_values_create, create_times_heap2, "b")
ax1[1].plot(n_values_create, create_times_heap5, "g")
ax1[2].plot(n_values_create, create_times_heap7, "r")

ax1[3].plot(n_values_create, create_times_heap2, "b")
ax1[3].plot(n_values_create, create_times_heap5, "g")
ax1[3].plot(n_values_create, create_times_heap7, "r")
ax1[3].legend(["Hep 2-ary", "Heap 5-ary", "Heap 7-ary" ], loc = 2)

ax1[3].set_ylabel("Time in seconds of creating heap")
ax1[3].set_xlabel("Number of elements in heap")

fig2, ax2 = plt.subplots(nrows = 4, ncols = 1, figsize = (6, 7))
fig2.suptitle("Root Delete Time", fontsize = 16)
ax2[0].plot(n_values_delete, detele_times_heap2, "b")
ax2[1].plot(n_values_delete, detele_times_heap5, "g")
ax2[2].plot(n_values_delete, detele_times_heap7, "r")

ax2[3].plot(n_values_delete, detele_times_heap2, "b")
ax2[3].plot(n_values_delete, detele_times_heap5, "g")
ax2[3].plot(n_values_delete, detele_times_heap7, "r")
ax2[3].legend(["Hep 2-ary", "Heap 5-ary", "Heap 7-ary" ], loc = 2)

ax2[3].set_ylabel("Time in seconds of deleting root")
ax2[3].set_xlabel("Number of elements in heap")

for sub in ax1, ax2:
    for subb in sub:
        subb.grid(True)

plt.show()

fig1.savefig('Create_time.png')
fig2.savefig('Delete_ime.png') 

plt.close(fig1)
plt.close(fig2)