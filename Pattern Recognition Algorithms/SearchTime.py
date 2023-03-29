import random
import time
import matplotlib.pyplot as plt
from PatternSearchAlgorithm import naive, KMP, showPattern

def measure_time(function, pattern, text, repetitions):
    times = []
    for i in range(repetitions):
        start = time.time()
        function(pattern, text)
        end = time.time()
        times.append(end - start)
    return sum(times) / len(times)

# Odczyt pliku .txt
with open("pan-tadeusz.txt", "r", encoding="utf8") as f:
    text = f.read()

# Podział tekstu na słowa
words = text.split()

# Liczba słów do wyszukania
n_values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# Pomiar czasu dla danego algorytmu i odpowieniej liczby słów z n_values
naive_times = []
kmp_times = []
for n in n_values:
    pattern = " ".join(words[:n])
    naive_time = measure_time(naive, pattern, text, 10)
    kmp_time = measure_time(KMP, pattern, text, 10)
    naive_times.append(naive_time)
    kmp_times.append(kmp_time)

# Wykres
plt.plot(n_values, naive_times, label="Naive")
plt.plot(n_values, kmp_times, label="KMP")
plt.xlabel("Number of words")
plt.ylabel("Time (seconds)")
plt.legend()
plt.show()

plt.savefig("search_times.png")






# Pusty napis wejściowy i wzorze
print("Empty text and pattern")
pattern = ""
text = ""
size = len(text)
print(f"Text: {text} ---> pattern: {pattern}")
positionsN = naive(pattern, text)
print(f"Position of pattern: {positionsN}") # [0]
showPattern(text,positionsN,size)
positionsKMP = naive(pattern, text)
print(f"Position of pattern: {positionsN}") # [0]
showPattern(text,positionsKMP,size)
print('---------------------------------------')   

# Pusty napis wejściowy
print("Empty text")
pattern = ""
text = "abc"
size = len(text)
print(f"Text: {text} ---> pattern: {pattern}")
positionsN = naive(pattern, text)
print(f"Position of pattern: {positionsN}") # [0]
showPattern(text,positionsN,size)
positionsKMP = naive(pattern, text)
print(f"Position of pattern: {positionsN}") # [0]
showPattern(text,positionsKMP,size)
print('---------------------------------------') 

# Pusty napis szukany
print("Empty pattern")
pattern = "abc"
text = ""
size = len(text)
print(f"Text: {text} ---> pattern: {pattern}")
positionsN = naive(pattern, text)
print(f"Position of pattern: {positionsN}") # [0]
showPattern(text,positionsN,size)
positionsKMP = naive(pattern, text)
print(f"Position of pattern: {positionsN}") # [0]
showPattern(text,positionsKMP,size)
print('---------------------------------------') 

# Napis szukany jest taki sam jak napis wejściowy
print("The search string is the same as the input string")
pattern = "abc"
text = "abc"
size = len(text)
print(f"Text: {text} ---> pattern: {pattern}")
positionsN = naive(pattern, text)
print(f"Position of pattern: {positionsN}") # [0]
showPattern(text,positionsN,size)
positionsKMP = naive(pattern, text)
print(f"Position of pattern: {positionsN}") # [0]
showPattern(text,positionsKMP,size)
print('---------------------------------------') 

# Napis szukany jest dłuższy niż napis wejściowy
print("The search string is longer than the input string")
pattern = "abcd"
text = "abc"
size = len(text)
print(f"Text: {text} ---> pattern: {pattern}")
positionsN = naive(pattern, text)
print(f"Position of pattern: {positionsN}") # [0]
showPattern(text,positionsN,size)
positionsKMP = naive(pattern, text)
print(f"Position of pattern: {positionsN}") # [0]
showPattern(text,positionsKMP,size)
print('---------------------------------------') 

# Napis szukany nie występuje w napisie wejściowym
print("The search string is not in the input string")
pattern = "def"
text = "abc"
size = len(text)
print(f"Text: {text} ---> pattern: {pattern}")
positionsN = naive(pattern, text)
print(f"Position of pattern: {positionsN}") # [0]
showPattern(text,positionsN,size)
positionsKMP = naive(pattern, text)
print(f"Position of pattern: {positionsN}") # [0]
showPattern(text,positionsKMP,size)
print('---------------------------------------') 

# Napis szukany występuje w napisie wejściowym kilka razy
print("The search string appears several times in the input string")
pattern = "abc"
text = "abcabcabc"
size = len(text)
print(f"Text: {text} ---> pattern: {pattern}")
positionsN = naive(pattern, text)
print(f"Position of pattern: {positionsN}") # [0]
showPattern(text,positionsN,size)
positionsKMP = naive(pattern, text)
print(f"Position of pattern: {positionsN}") # [0]
showPattern(text,positionsKMP,size)
print('---------------------------------------') 

# Napis szukany występuje w napisie wejściowym tylko raz
print("The search string appears only once in the input string")
pattern = "def"
text = "abcdefghi"
size = len(text)
print(f"Text: {text} ---> pattern: {pattern}")
positionsN = naive(pattern, text)
print(f"Position of pattern: {positionsN}") 
showPattern(text,positionsN,size)
positionsKMP = naive(pattern, text)
print(f"Position of pattern: {positionsN}")
showPattern(text,positionsKMP,size)
print('---------------------------------------') 

# Napis szykany występuje w napisie wejsciowym losową ilosć razy
print("The search string appears in the input string a random number of times")

# generujemy łańcuch
text = ""
for i in range(30):
    text += chr(65 + (random.randint(0, 2)))
print(f"Text: {text}")
size = len(text)

# generujemy wzorzec
pattern = ""
for i in range(3):
    pattern += chr(65 + (random.randint(0, 2)))
print(f"Pattern: {pattern}")   
 
size = len(text)
positionsN = naive(pattern, text)
print(f"Position of pattern: {positionsN}") 
showPattern(text,positionsN,size)
positionsKMP = naive(pattern, text)
print(f"Position of pattern: {positionsN}") 
showPattern(text,positionsKMP,size)
print('---------------------------------------') 