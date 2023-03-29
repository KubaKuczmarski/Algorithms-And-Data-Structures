**[PL]**

Algorytm Dijkstry to algorytm służący do znajdowania najkrótszej ścieżki między wierzchołkami w grafie ważonym. Algorytm rozpoczyna działanie od wierzchołka startowego i stopniowo przeszukuje graf, przypisując odległości między wierzchołkami. Dla każdego wierzchołka w grafie odległości te są aktualizowane w czasie działania algorytmu.

# ZADANIE

Dana jest plansza o dowolnych wymiarach. Na dwóch polach planszy znajduje się cyfra 0. Na pozostałych polach planszy znajdują się cyfry z przedziału od 1
do 9. Na przykład:

| PLANSZA |
| ------- |
| 111122  |
| 104122  |
| 942111  |
| 996411  |
| 990411  |
| 991111  |



Przyjmijmy teraz, że po polach można się przemieszczać w kierunkach prawolewo i góra-dół (lecz nie na skos), a cyfry oznaczają koszt opuszczenia (zejścia z) pola. Zadanie polega na napisaniu programu, który:

1. wczyta planszę z pliku (nazwa pliku przekazana jako argument wywołania programu);
2. korzystając z algorytmu Dijkstry, znajdzie dowolną z najmniej kosztownych tras przejścia pomiędzy polami z cyfrą 0;
3. wyświetli pola planszy (cyfry znajdujące się na tych polach), które leżą na znalezionej trasie.

|  WYNIK  |
| ------- |
| -111--  |
| -0-1--  |
| ---11-  |
| ----1-  |
| --0-1-  |
| --111-  |

 
 
 ===================================================================================================================
 
 **[ENG]**
 
Dijkstra's algorithm is an algorithm used to find the shortest path between vertices in a weighted graph. The algorithm begins at a starting vertex and gradually explores the graph, assigning distances between vertices. For each vertex in the graph, these distances are updated during the course of the algorithm.
 
 # TASK

A board of any size is given. On two fields of the board there is a number 0. On the other fields of the board there are numbers from 1
to 9. For example:

|  BOARD  |
| ------- |
| 111122  |
| 104122  |
| 942111  |
| 996411  |
| 990411  |
| 991111  |

Now let's assume that the fields can be moved in the right-left and up-down directions (but not diagonally), and the numbers indicate the cost of leaving (going off) the field. The task is to write a program that:

1. load the board from a file (file name passed as an argument to program invocation);
2. using Dijkstra's algorithm, he will find any of the least expensive routes between the fields with the number 0;
3. will display the board fields (numbers on these fields) that lie on the found route.

| RESULT  |
| ------- |
| -111--  |
| -0-1--  |
| ---11-  |
| ----1-  |
| --0-1-  |
| --111-  |
 
