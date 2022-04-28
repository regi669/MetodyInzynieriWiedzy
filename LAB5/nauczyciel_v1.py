import math
import re
from turtle import pu
import numpy as np
import pandas as pd
import random


nazwapliku = 'LAB5/australian.dat'

def stworz_macierz(plik):
    macierz = []
    with open(plik, "r") as f:
        macierz = [list(map(lambda x: float(x), line.split())) for line in f]
    return macierz

def euklides(list1, list2):
    vector1 = np.array(list1)
    vector2 = np.array(list2)
    subtraction = vector1[:-1] - vector2[:-1]
    return math.sqrt(np.dot(subtraction, subtraction))

dataset = stworz_macierz(nazwapliku)
def data_preprocessing(dataset):
    slownik = dict()
    for wiersz in dataset:
        wiersz[-1] = random.randrange(0, 2)
        if wiersz[-1] not in slownik.keys():
            slownik[wiersz[-1]] = []
        slownik[wiersz[-1]].append(wiersz)
    return slownik

def initialize_centers(punkty):
    srodki = {}
    for key in punkty.keys():
        pomoc = {}
        for x in range(len(punkty[key])):
            suma_odleglosci = 0
            for y in range(len(punkty[key])):
                if x != y:
                    odleglosc = euklides(punkty[key][x], punkty[key][y])
                    suma_odleglosci += odleglosc
            pomoc[tuple(punkty[key][x])] = suma_odleglosci
        srodki[key] = list(min(pomoc, key=pomoc.get))
    return srodki


def get_points(punkty, centry):
    nowe_punkty = dict()
    lista_punktow = []
    nie_koncz = False
    for i in punkty.keys():
        lista_punktow += punkty[i]
    for punkt in lista_punktow:
        temp = punkt[-1]
        min_odleglosc = 1e500
        for j in centry.keys():
            odleglosc = euklides(punkt, centry[j])
            if odleglosc <= min_odleglosc:
                min_odleglosc = odleglosc
                punkt[-1] = j
        if punkt[-1] not in nowe_punkty.keys():
            nowe_punkty[punkt[-1]] = []
        nowe_punkty[punkt[-1]].append(punkt)
        if temp != punkt[-1]:
            nie_koncz = True
    return nowe_punkty, nie_koncz


def naucz_optymalne(dataset):
    punkty = data_preprocessing(dataset)
    centry = initialize_centers(punkty)
    i = 0
    nie_koncz = True
    while nie_koncz:
        print('Iteracja {}'.format(i))
        i += 1
        punkty, nie_koncz = get_points(punkty, centry)
        nowe_centry = initialize_centers(punkty)
        centry = nowe_centry
    return punkty

nowe_punkty = naucz_optymalne(dataset)
print(len(nowe_punkty[0]))
print(len(nowe_punkty[1]))

#print(nowe_punkty[0])
#print(nowe_punkty[1])
