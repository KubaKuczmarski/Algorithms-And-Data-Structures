"""
Algorytm sortowania szybkiego (ang. quick sort)

Algorytm "dziel i zwycięzaj"

Algorytm rekurencyjny 

Wersja optymistyczna - O(nlogn), pesymistyczna - O(n^2) - zalezy od wyboru piwota, im badziej srodkowa wartosc tym lepiej
"""

def quick_sort(lst):
    quick(lst, 0, len(lst)-1)
    return lst


def quick(lst, low, high):
    if low < high:
        pi = partition(lst, low, high)
        quick(lst, low, pi - 1) 
        quick(lst, pi + 1, high) 
    return lst


def partition(lst, low, high):
    pivot = lst[high]
    pointer = low
    for iter in range(low, high):
        if lst[iter] <= pivot:
            (lst[iter], lst[pointer]) = (lst[pointer], lst[iter])
            pointer += 1
    (lst[pointer], lst[high]) = (lst[high], lst[pointer])
    return pointer





