import random
import numpy as np
import math


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

data = stworz_macierz(nazwapliku)

def mix(dataset):
    for point in range(len(dataset)):
        dataset[point][-1] = random.randrange(0, 2)
    return dataset

def list_to_dict(list):
    dict = {}
    for x in list:
        if x[-1] not in dict.keys():
            dict[x[-1]] = [x]
        else:
            dict[x[-1]].append(x)
    return dict

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

def punkt_pozadkowy(punkt, centry):
    odleglosc = {}
    for i in centry.keys():
        odleglosc[i] = euklides(punkt, centry[i])
    return min(odleglosc, key=odleglosc.get)

def naucz (dataset):
    end = False
    while not end:
        end = True
        punkty = list_to_dict(dataset)
        centry = initialize_centers(punkty)
        for x in range(len(dataset)):
            if punkt_pozadkowy(dataset[x], centry) != dataset[x][-1]:
                dataset[x][-1] = punkt_pozadkowy(dataset[x], centry)
                end = False
    return dataset


mixed_dataset = mix(data)
dataset2 = naucz(mixed_dataset)
segregacja = list_to_dict(dataset2)
print(len(segregacja[0]))
print(len(segregacja[1]))