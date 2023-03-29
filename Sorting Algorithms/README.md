[PL]

# Implementacje algorytmów sortowania

W tym repozytorium znajdziesz implementacje czterech popularnych algorytmów sortowania: sortowanie bąbelkowe (bubble sort), sortowanie przez wybieranie (selection sort), sortowanie przez scalanie (merge sort) oraz sortowanie szybkie (quick sort).

## Sortowanie bąbelkowe
Algorytm sortowania bąbelkowego to prosty algorytm sortowania, który działa poprzez porównywanie par sąsiednich elementów i zamienianie ich miejscami, jeśli nie są w odpowiedniej kolejności. W każdej iteracji największy element zostaje przesunięty na końiec tablicy. Algorytm kończy działanie, gdy tablica jest już posortowana.

## Sortowanie przez wybieranie
Algorytm sortowania przez wybieranie działa poprzez wybieranie najmniejszego elementu z pozostałych nieposortowanych elementów i umieszczanie go na odpowiedniej pozycji w tablicy. Algorytm kończy działanie, gdy wszystkie elementy zostaną posortowane.

## Sortowanie przez scalanie
Algorytm sortowania przez scalanie to algorytm dziel i zwyciężaj, który polega na dzieleniu tablicy na połowy aż do osiągnięcia pojedynczych elementów, a następnie scalaniu ich w odpowiedniej kolejności.

## Sortowanie szybkie
Algorytm sortowania szybkiego to algorytm dziel i zwyciężaj, który polega na wybieraniu elementu dzielącego tablicę (tzw. pivot) i umieszczaniu mniejszych elementów przed nim, a większych po nim. Następnie algorytm rekurencyjnie sortuje obie części tablicy.

# ZADANIE: Porównanie algorytmów sortowania
Jako dane do sortowania wykorzystaj plik pan-tadeusz.txt, zawierający słowa oddzielone białymi znakami. Dla każdej z funkcji sortujących:
- sprawdź czy funkcja poprawnie sortuje słowa wczytywane z pliku,
- zmierz czas sortowania list zawierających n pierwszych słów wczytanych z pliku (np. n = 1000, 2000, ..., 10000),
- wygeneruj wykres zależności czasu sortowania od długości listy.

[ENG]

# Sorting Algorithms Implementations
In this repository, you will find implementations of four popular sorting algorithms: bubble sort, selection sort, merge sort, and quick sort.

## Bubble Sort
Bubble sort is a simple sorting algorithm that works by repeatedly swapping adjacent elements if they are in the wrong order. In each iteration, the largest element is moved to the end of the array. The algorithm terminates when the array is already sorted.

## Selection Sort
Selection sort works by repeatedly selecting the smallest remaining element from the unsorted part of the array and placing it in its correct position in the sorted part of the array. The algorithm terminates when all elements have been sorted.

## Merge Sort
Merge sort is a divide-and-conquer algorithm that works by dividing the array into halves until there are single-element arrays, and then merging them in the correct order.

## Quick Sort
Quick sort is a divide-and-conquer algorithm that works by selecting a pivot element from the array and partitioning the array around the pivot. The smaller elements are placed before the pivot, and the larger elements are placed after the pivot. The algorithm then recursively sorts both subarrays.

# TASK: Comparison of sorting algorithms
As data for sorting, use the pan-tadeusz.txt file containing words separated by whitespace. For each of the sorting functions: 
- check if the function correctly sorts the words read from the file,
- measure the sorting time of lists containing the first n words read from file (e.g. n = 1000, 2000, ..., 10000),
- generate a plot of sorting time versus list length.
