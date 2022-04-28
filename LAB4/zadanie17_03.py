import math

nazwapliku = 'LAB4/australian.dat'

def stworz_macierz (plik):
    macierz = []
    with open(plik,"r") as f:
        macierz = [list(map(lambda x: float(x), line.split())) for line in f]
    return macierz

def euklides (lista1, lista2):
    wynik = 0
    for x in range(len(lista1) - 1):
        wynik += (lista1[x] - lista2[x]) ** 2
    return math.sqrt(wynik)

macierz = stworz_macierz(nazwapliku)

#Zadanie 1

def liczba_decyzyjna_i_odleglosc(x, matrix):
    lista = []
    for y in matrix:
        odleglosc = euklides(x, y)
        lista.append((y[-1], odleglosc))
    return lista

wynik = liczba_decyzyjna_i_odleglosc([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], macierz)
#print(wynik)

#Zadanie 2

#Z listy wyników zrobić słownik 1 i 0 

def slownik_z_touple (lista_touple):
    slownik = dict()
    for x in lista_touple:
        klucz = x[0]
        if klucz not in slownik.keys():
            slownik[klucz] = []
        slownik[klucz].append(x[1])
    return slownik

slownik_pogrupowany = slownik_z_touple(wynik)
print('\n')
#print(slownik_pogrupowany)

#Zadanie 3

# k najblizszych (najmniejszych odleglosci) somsiadow z kazdej listy dodać 

def k_najmniejszych_odleglosci (k, slownik):
    wynik = dict()
    for x in slownik.keys():
        lista = slownik[x]
        lista.sort()
        wynik2 = 0.0
        for y in range(k):
            wynik2 += lista[y]
        wynik[x] = wynik2
    return wynik
        



#Do domu metryka euklidesowa w oparciu o wektor i działania na wektorze
#Zrob funkcje ktora przyjmie x liste i k i zwróci decyzję


def k_n_n (macierz, k, x):
    lista = []
    for y in macierz:
        odleglosc = euklides(x, y)
        lista.append((y[-1], odleglosc))
    slownik = dict()
    wynik = dict()
    for x in lista:
        klucz = x[0]
        if klucz not in slownik.keys():
            slownik[klucz] = []
        slownik[klucz].append(x[1])
    for x in slownik.keys():
        lista = slownik[x]
        lista.sort()
        wynik2 = 0.0
        for y in range(k):
            wynik2 += lista[y]
        wynik[x] = wynik2
    if wynik[0] > wynik[1]:
        return 0
    else:
        return 1


nowy_wiersz = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(k_n_n(macierz, 5, nowy_wiersz))

import numpy as np
def euklides_wektorowo (list1, list2):
    vector1 = np.array(list1)
    vector2 = np.array(list2)
    subtraction = vector1 - vector2
    return math.sqrt(np.dot(subtraction, subtraction))

print(euklides_wektorowo(macierz[0], macierz[1]))