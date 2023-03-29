**[PL]**

# Implementacja algorytmów wyszukiwania wzorca

Napisz dwie funkcje, które implementują następujące algorytmy wyszukiwania wzorca w tekście:
- algorytm N (tzw. naiwny),

Algorytm N, zwany również algorytmem naiwnym lub brute-force, polega na porównywaniu wzorca z tekstem znak po znaku, zaczynając od pierwszego znaku w tekście. Jeśli znak w tekście nie pasuje do wzorca, algorytm przesuwa się o jeden znak w prawo w tekście i zaczyna porównywanie od nowa. Algorytm kończy się, gdy wzorzec zostanie znaleziony lub gdy przeszukanie całego tekstu zakończy się niepowodzeniem.

- algorytm KMP (Knutha-Morrisa-Pratta)

Algorytm KMP, znany również jako algorytm Knutha-Morrisa-Pratta, jest bardziej wydajnym algorytmem wyszukiwania wzorca w tekście. Polega on na konstrukcji tzw. tablicy przejść (ang. failure function), która zawiera informacje o tym, ile znaków wzorca można przesunąć, gdy nastąpi niedopasowanie. Dzięki temu algorytm nie musi porównywać znak po znaku całego wzorca z tekstem w każdej iteracji.

# Sprawdzenie poprawności implementacji
Przetestuj obie funkcje dla przypadków brzegowych:
- pusty jeden lub oba napisy wejściowe,
- napis string równy napisowi text ,
- napis string dłuższy od napisu text ,
- napis string nie występuje w text .
Przetestuj implementację algorytmu naiwnego (dobierz kilka zestawów danych testowych oraz sprawdź poprawność wyników). Następnie przetestuj
implementację drugiego algorytmu w ten sposób, że dla generowanych losowo tekstów i wzorców (alfabet ogranicz do dwóch liter), sprawdź czy obie
implementacje zwracają ten sam wynik.

# Porównanie algorytmów wyszukiwania wzorca
Jako tekst przeszukiwany wykorzystaj plik pan-tadeusz.txt . Dla każdej z funkcji:
- zmierz czas wyszukiwania n pierwszych słów wczytanych z pliku (np. n = 100, 200, ..., 1000) w całym pliku (od początku do jego końca).

Narysuj zbiorczy wykres (jeden wykres dla obu funkcji) pokazujący zależność czasu wyszukiwania od liczby szukanych słów.


=====================================================================================

**[ENG]**

# Implementation of pattern search algorithms

Write two functions that implement the following text pattern search algorithms:
- N algorithm (so-called naive),

Algorithm N, also known as the naive or brute-force algorithm, involves comparing the pattern with the text character by character, starting from the first character in the text. If a character in the text does not match the pattern, the algorithm shifts one character to the right in the text and begins comparison again. The algorithm ends when the pattern is found or when the entire text search fails.

- KMP (Knuth-Morris-Pratt) algorithm

The Knuth-Morris-Pratt (KMP) algorithm is a more efficient pattern matching algorithm. It involves constructing a failure function, which contains information about how many characters the pattern can be shifted when a mismatch occurs. This allows the algorithm to avoid comparing the entire pattern with the text in each iteration.

# Validation of implementation
Test both functions for edge cases:
- empty one or both input strings,
- string string equal to text ,
- string longer than text ,
- string is not present in text .
Test the implementation of the naive algorithm (choose several sets of test data and check the correctness of the results). Then test
implementation of the second algorithm in such a way that for randomly generated texts and patterns (limit the alphabet to two letters), check whether both
implementations return the same result.

# Comparison of pattern search algorithms
Use the pan-tadeusz.txt file as the searchable text. For each function:
- measure the search time of the first n words read from the file (e.g. n = 100, 200, ..., 1000) in the entire file (from the beginning to its end).

Draw a cumulative graph (one graph for both functions) showing the dependence of the search time on the number of searched words.
