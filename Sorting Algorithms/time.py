import sys
import time
import string
import gc
import matplotlib.pyplot as plt
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from quick_sort import quick_sort


sys.setrecursionlimit(10000)

max_words = 1000
lst = []
bubble_sort_time = []
selection_sort_time = [] 
merge_sort_time = []
quick_sort_time = []
list_size = []

# Odczy danych
counter = 0
translator = str.maketrans('', '', string.punctuation)
with open("pan-tadeusz.txt", "r", encoding="utf8") as text:
    for line in text:
        if counter >= max_words:
            break
        for word in line.split():
            counter += 1
            lst.append(word.translate(translator).lower())


print("Procent wszytskich posortowanych słów:")

# Sortowanie
for size in range(0, max_words+500, 500):
    
    print("{:d}%".format(int(size/max_words*100)))
    list_size.append(size)

    # Bubble sort
    sorted_bubble = [''] * size
    list_copy = (lst[:size]).copy()
    gc_old = gc.isenabled()
    gc.disable()
    start = time.time()
    sorted_bubble = bubble_sort(list_copy)
    stop = time.time()
    if gc_old:
        gc.enable()
    bubble_sort_time.append(stop - start)
    
    
    # Selected sort
    sorted_selection = [''] * size
    list_copy = (lst[:size]).copy()
    gc_old = gc.isenabled()
    gc.disable()
    start = time.time()
    sorted_selection = selection_sort(list_copy)
    stop = time.time()
    if gc_old:
        gc.enable()
    selection_sort_time.append(stop - start)
    
    
    # Merge sort
    list_copy = (lst[:size]).copy()
    gc_old = gc.isenabled()
    gc.disable()
    start = time.time()
    sorted_merge = merge_sort(list_copy)
    stop = time.time()
    if gc_old:
        gc.enable()
    merge_sort_time.append(stop - start)
    
    
    # Quick sort
    list_copy = (lst[:size]).copy()
    gc_old = gc.isenabled()
    gc.disable()
    start = time.time()
    sorted_quick = quick_sort(list_copy)
    stop = time.time()
    if gc_old:
        gc.enable()
    quick_sort_time.append(stop - start)
    
    
# Zpis najważniejszych informacji do pliku
with open("bubble.txt", "w",  encoding="utf8") as out:
    out.write("Sorting time for {:d} words:\n".format(len(sorted_bubble)))
    out.write("Bubble sort time: {:f}s\n".format(bubble_sort_time[-1]))
    out.write("Sorted text:\n")
    for sorted_word in sorted_bubble:
        out.write(sorted_word + "\n")

with open("selection.txt", "w",  encoding="utf8") as out:
    out.write("Selection time for {:d} words:\n".format(len(sorted_selection)))
    out.write("Selection sort time: {:f}s\n".format(selection_sort_time[-1]))
    out.write("Sorted text:\n")
    for sorted_word in sorted_selection:
        out.write(sorted_word + "\n")

with open("merge.txt", "w",  encoding="utf8") as out:
    out.write("Merge time for {:d} words:\n".format(len(sorted_merge)))
    out.write("Merge sort time: {:f}s\n".format(merge_sort_time[-1]))
    out.write("Sorted text:\n")
    for sorted_word in sorted_merge:
        out.write(sorted_word + "\n")

with open("quick.txt", "w",  encoding="utf8") as out:
    out.write("Sorting time for {:d} words:\n".format(len(sorted_quick)))
    out.write("Quick sort time: {:f}s\n".format(quick_sort_time[-1]))
    out.write("Sorted text:\n")
    for sorted_word in sorted_quick:
        out.write(sorted_word + "\n")

# Wykresy
fig, ax = plt.subplots(nrows = 3, ncols = 2, figsize = (12, 8))
fig.suptitle("Algorytmy sortowania", fontsize = 16)

ax[0][0].plot(list_size, bubble_sort_time, "y")
ax[1][0].plot(list_size, selection_sort_time, "g")
ax[0][1].plot(list_size, merge_sort_time, "r")
ax[1][1].plot(list_size, quick_sort_time, "b")

ax[2][0].plot(list_size, merge_sort_time, "r")
ax[2][0].plot(list_size, quick_sort_time, "b")

ax[2][1].plot(list_size, bubble_sort_time, "y")
ax[2][1].plot(list_size, selection_sort_time, "g")
ax[2][1].plot(list_size, merge_sort_time, "r")
ax[2][1].plot(list_size, quick_sort_time, "b")


ax[2][0].legend(["Merge sort", "Quick sort"], loc = 2)
ax[2][1].legend(["Bubble sort", "Selection sort", "Merge sort", "Quick sort"], loc = 2)

ax[0][0].set_ylabel("Czas[s] - bubble sort")
ax[1][0].set_ylabel("Czas[s] - selection sort")
ax[0][1].set_ylabel("Czas[s] - merge sort")
ax[1][1].set_ylabel("Czas[s] - quick sort")
ax[2][0].set_ylabel("Czas[s] - quick and merge algorithm")
ax[2][1].set_ylabel("Czas[s] - each sorting algorithm")

ax[0][0].set_xlabel("Liczba elementów w liście")
ax[1][0].set_xlabel("Liczba elementów w liście")
ax[0][1].set_xlabel("Liczba elementó ww liście")
ax[1][1].set_xlabel("Liczba elementów w liście")
ax[2][0].set_xlabel("Liczba elementów w liście")
ax[2][1].set_xlabel("Liczba elementów w liście")

for sub in ax:
    for subb in sub:
        subb.grid(True)
plt.show()
fig.savefig('SortingTime.png')   # save the figure to file
plt.close(fig)

