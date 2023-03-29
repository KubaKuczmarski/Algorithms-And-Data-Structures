**[PL]**

# Implementacja drzew

Przygotuj implementacje następujących drzew:
- drzewo BST (ang. Binary Search Tree)

Drzewo BST to drzewo binarne, w którym wartości w węzłach są ułożone w taki sposób, że wartości mniejsze od korzenia są przechowywane w lewym poddrzewie, a większe - w prawym poddrzewie. Dzięki takiemu uporządkowaniu, operacje takie jak wstawianie, usuwanie i wyszukiwanie elementu w BST można wykonywać w czasie logarytmicznym     O(log n).

- drzewo AVL.

Drzewo AVL to drzewo BST z dodatkową cechą - każde poddrzewo ma zbalansowaną wysokość, czyli różnica wysokości lewego i prawego poddrzewa wynosi co najwyżej 1. Dzięki temu, drzewo AVL jest w stanie utrzymać złożoność czasową operacji wstawiania, usuwania i wyszukiwania elementu w czasie O(log n), nawet w przypadku, gdy drzewo nie jest zbalansowane.

# ZADANIE
Wymagane operacje:
- wstawianie elementu do drzewa,
- wyszukiwanie elementu w drzewie,
- usuwanie elementu z drzewa (tylko dla drzewa BST),
- wyświetlanie drzewa na ekranie (tak, aby widoczna była jego struktura).

# Porównanie drzew

Wygeneruj wejściową listę liczb (np. 10000 losowych liczb z zakresu od 1 do 30000), która posłuży dalej do badania wydajności.
Dla każdego z drzew:
- zmierz czas tworzenia drzewa na podstawie n pierwszych liczb listy
- wejściowej (np. n = 1000, 2000, ..., 10000), zmierz czasy wyszukiwania n pierwszych liczb listy wejściowej (np. n = 1000, 2000, ..., 10000) w drzewie, które dla każdego n zostało utworzone na podstawie całej listy wejściowej,

Wygeneruj zbiorcze wykresy (jeden wykres dla obu typów drzew) pokazujące uzyskane wyniki.

Dla drzewa BST:
- zmierz czasy usuwania n pierwszych liczb listy wejściowej (np. n = 1000, 2000, ..., 10000) w drzewie, które dla każdego n zostało utworzone na
podstawie całej listy wejściowej.

Wygeneruj wykres pokazujący uzyskane wyniki.


============================================================================================

**[ENG]**

# Implementation of trees

Prepare implementations of the following trees:
- BST tree (Binary Search Tree)

A BST is a binary tree in which the values at the nodes are arranged so that values smaller than the root are stored in the left subtree, and values larger than the root are stored in the right subtree. With this ordering, operations such as inserting, deleting, and searching for an element in the BST can be performed in O(log n) logarithmic time.

- AVL tree

The AVL tree is a BST tree with an additional feature - each subtree is height-balanced, i.e. the difference in the height of the left and right subtrees is at most 1. Thanks to this, the AVL tree is able to maintain the time complexity of inserting, deleting and searching for an element in O(log n), even if the tree is unbalanced.

# TASK
Required Operations:
- inserting an element into the tree,
- searching for an element in the tree,
- deleting an element from the tree (only for BST tree),
- displaying the tree on the screen (so that its structure is visible).

# Compare trees

Generate an input list of numbers (e.g., 10,000 random numbers between 1 and 30,000) for further performance testing.
For each tree:
- measure the tree creation time based on the first n numbers of the list
- input (e.g. n = 1000, 2000, ..., 10000), measure the search times for the first n numbers of the input list (e.g. n = 1000, 2000, ..., 10000) in the tree that was created for each n based on the entire input list,

Generate summary graphs (one graph for both types of trees) showing the obtained results.

For BST tree:
- measure the removal times of the first n numbers of the input list (e.g. n = 1000, 2000, ..., 10000) in a tree that for each n was created on based on the entire input list.

Generate a chart showing your results.
