import numpy as np
import math as m
def srednia(lista):
	sum = 0
	for x in lista:
		sum += x
	return x / len(lista)

def warjancja(lista):
	mean_avg = srednia(lista)
	sum = 0
	for x in lista:
		sum += pow((x-mean_avg),2)
	return sum / len(lista)

def odchylenie(lista):
	return pow(warjancja(lista), 1/2)

def srednia_matrix(lista):
    return np.dot(np.array(lista), np.ones(len(lista))) / len(lista)

def wariancja_matrix(lista):
    lista_minus_srednia = np.array(lista) - srednia_matrix(lista)
    return np.dot(lista_minus_srednia, lista_minus_srednia) / len(lista)

def odchylenie_matrix(lista):
    return m.sqrt(wariancja_matrix(lista))


lista = [5.,5.,5.,5.]
print(srednia(lista))
print(warjancja(lista))
print(odchylenie(lista))

print(srednia_matrix(lista))
print(wariancja_matrix(lista))
print(odchylenie_matrix(lista))