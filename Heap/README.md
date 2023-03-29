**[PL]**

# Implementacja kopców

Zaimplementuj trzy kopce zupełne: 2-arny, 5-arny i 7-arny. Każdy z kopców zaimplementuj w tablicy (liście w Pythonie). 

Kopiec to rodzaj struktury danych, która reprezentuje drzewo binarne z pewnymi dodatkowymi warunkami. Kopiec musi być drzewem binarnym, tzn. każdy węzeł ma maksymalnie dwóch potomków. Ponadto, w kopcu każdy węzeł ma wartość większą lub równą wartości swoich potomków (dla tzw. kopca typu max) lub mniejszą lub równą wartości swoich potomków (dla tzw. kopca typu min).

Arność kopca to liczba potomków każdego węzła. W przypadku kopca binarnego, arność wynosi 2. Jednak w przypadku ogólniejszych kopców, arność może być większa niż 2. Arność kopców jest zwykle określana przez nazwę kopca, np. kopiec czterowęzłowy to kopiec, w którym każdy węzeł ma maksymalnie czterech potomków.

# ZADANIE 

Wymagane operacje:
- wstawianie elementu do kopca,
- usuwanie szczytu kopca,
- wyświetlanie kopca na ekranie (w dowolny, ale czytelny sposób).

# Porównanie kopców
Wygeneruj wejściową listę liczb (np. 100000 losowych liczb z zakresu od 1 do 300000), która posłuży dalej do badania wydajności.
Dla każdego z kopców:
- zmierz czas tworzenia kopca na podstawie n pierwszych liczb listy wejściowej (np. n = 10000, 20000, ..., 100000),
- zmierz czas wykonania n operacji usunięcia szczytu kopca (np. n = 10000, 20000, ..., 100000) w kopcu, który dla każdego n został utworzony na
podstawie całej listy wejściowej.

Dla każdej z operacji wygeneruj zbiorcze wykresy (jeden wykres dla trzech typów kopców) pokazujące zależność czasu wykonania operacji od liczby
elementów/wykonań.


============================================================================================

**[ENG]**

# Implementation of heaps

Implement three complete heaps: 2-aryns, 5-aryns, and 7-aryns. Implement each of the heaps in an array (leaves in Python).

A heap is a type of data structure that represents a binary tree with some additional conditions. The heap must be a binary tree, meaning that each node can have at most two children. Additionally, in a heap, each node has a value greater than or equal to the value of its children (for a max heap) or less than or equal to the value of its children (for a min heap).

The arity of a heap is the number of children each node can have. In the case of a binary heap, the arity is 2. However, in more general heaps, the arity can be greater than 2. The arity of a heap is typically specified by the name of the heap, e.g. a four-way heap is a heap in which each node can have at most four children.

# TASK

Required Operations:
- inserting an element into a heap,
- removal of the top of the mound,
- displaying the mound on the screen (in any, but legible way).

# Comparison of mounds
Generate an input list of numbers (e.g., 100,000 random numbers between 1 and 300,000) for further performance testing.
For each mound:
- measure the heap creation time based on the first n numbers of the input list (e.g. n = 10000, 20000, ..., 100000),
- measure the execution time of n operations to remove the top of the heap (e.g. n = 10000, 20000, ..., 100000) in the heap that for each n was created on
based on the entire input list.

For each operation, generate summary charts (one chart for three types of heaps) showing the dependence of operation execution time on the number of
elements/performances.
