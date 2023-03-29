import random
import time

# Algorytm naiwny (tzw. "brute-force")
def naive(pattern, text):
    positions = []
    n = len(pattern)
    m = len(text)
    for i in range(m - n + 1):
        if text[i:i+n] == pattern:
            positions.append(i)
    return positions

# Algorytm KMP
def LPS(pattern):
    m = len(pattern)
    lps = [0] * m
    j = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def KMP(pattern, text):
    if pattern == "": return 0;
    patternPosition = []
    n = len(text)
    m = len(pattern)
    lps = LPS(pattern)
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            patternPosition.append(i-j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return patternPosition


def showPattern(text, positions, size):
    print(text)
    for i in range(size):
        if i in positions:
            print("^", end="")
        else:
            print(" ", end="")
    print('\n')
    
'''    
# Przykład
text = "ABABDABACDABAB"
pattern = "ABAB"
size = len(text)

# Algorytm KMP
print("Algorytm Knutha-Morrisa-Pratta")
positionsKMP = KMP(text, pattern)  
lps = LPS(pattern)
print(f"LPS: {lps}") 
showPattern(text, positionsKMP, size)
 
# Algorytm naiwny
print("Algorytm naiwny")
positionsN = naive(pattern, text)
showPattern(text,positionsN,size)'''
