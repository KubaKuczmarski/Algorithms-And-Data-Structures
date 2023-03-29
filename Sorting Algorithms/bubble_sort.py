"""
Sortowanie bąbelkowe ang. bubble sort)

Złożonosc algorytmu O(n^2)
"""

def bubble_sort(lista):

    n = len(lista) 
    
    while n>1: 
        zamien = False 
        for i in range(0, n-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                zamien=True
        n-= 1

        if zamien == False: 
            break

    return lista