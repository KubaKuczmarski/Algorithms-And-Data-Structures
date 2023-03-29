"""
Sortowanie przez wybieranie (ang. selection sort)

Złożonosc algorytmu O(n^2) - dosc czasochłonny algorytmy
"""

def selection_sort(lista):

    for i in range(0, len(lista)-1):
        minIndex = i  
        for j in range(i+1, len(lista)): 
            if lista[minIndex] > lista[j]:
                minIndex = j
        lista[i], lista[minIndex] = lista[minIndex], lista[i]
        i += 1
    return lista 