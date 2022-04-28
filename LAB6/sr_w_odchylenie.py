import numpy as np
import math as m
def srednia(list1):
	sum = 0
	for x in list1:
		sum += x
	return x / len(list1)

def warjancja(list1):
	mean_avg = srednia(list1)
	sum = 0
	for x in list1:
		sum += pow((x-mean_avg),2)
	return sum / len(list1)

def odchylenie(list1):
	return pow(warjancja(list1), 1/2)

def srednia_matrix(lista):
    ones = np.ones((len(lista),1))
    return float(1/len(lista))*np.dot(np.array(lista),ones)[0]

def wariancja_matrix(lista):
    srednia = srednia_matrix(lista)
    ones = np.ones((1,len(lista)))*srednia
    minus = np.array(lista) - ones
    return float(1/len(lista))*np.dot(minus[0],minus[0].T)

def odchylenie_matrix(lista):
    return m.sqrt(wariancja_matrix(lista))


lista = [5,5,5,5]
print(srednia(lista))
print(warjancja(lista))
print(odchylenie(lista))

print(srednia_matrix(lista))
print(wariancja_matrix(lista))
print(odchylenie_matrix(lista))