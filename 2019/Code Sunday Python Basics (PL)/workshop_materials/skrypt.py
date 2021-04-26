import string
import random

def generuj_haslo(liczba_znakow):  # wywołanie funkcji
    pelen_zakres = string.ascii_letters + string.digits
    haslo = ''
    for x in range(0, liczba_znakow): # pętla, która powtarza kroki tyle razy, ile znakow zadalismy
        wylosowany_znak = random.choice(pelen_zakres) # losowanie znaku - Twoje zadania
        haslo = haslo + wylosowany_znak
        print(haslo)
    return haslo