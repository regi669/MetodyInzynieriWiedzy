import math as m
import numpy as np
np.set_printoptions(formatter={'float_kind':"{:.3f}".format})

B_T = np.array([
    [1., 1., 1., 1.,   1., 1., 1., 1.],
    [1., 1., 1., 1.,  -1.,-1.,-1.,-1.],
    [1., 1.,-1.,-1.,   0., 0., 0., 0.],
    [0., 0., 0., 0.,   1., 1.,-1.,-1.],

    [1.,-1., 0., 0.,   0., 0., 0., 0.],
    [0., 0., 1.,-1.,   0., 0., 0., 0.],
    [0., 0., 0., 0.,   1.,-1., 0., 0.],
    [0., 0., 0., 0.,   0., 0., 1.,-1.]
])

B = np.transpose(B_T)

I = np.identity(8)

def czy_diagonalna (matrix):
    for i in range(len(matrix[0])):
        for j in range(len(matrix[:,0])):
            if i != j:
                if matrix[i,j] != 0:
                    return False
    return True

def czy_jednostkowa (matrix, blad_obliczeniowy=0.1):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                if matrix[i,j] < 1 - blad_obliczeniowy and matrix[i,j] > 1 + blad_obliczeniowy:
                    return False
            elif i != j:
                if matrix[i,j] > blad_obliczeniowy and matrix[i,j] < -blad_obliczeniowy:
                    return False
    return True

def dlugosc_2(matrix):
    return np.dot(matrix, matrix.T)

def czy_wektory_ortagonalne (matrix):
    return czy_diagonalna(dlugosc_2(matrix))

def czy_wektory_ortonormalne (matrix):
    return czy_jednostkowa(dlugosc_2(matrix))

def dlugosc_vektora (vektor):
    return np.sqrt(dlugosc_2(vektor))

def normalizuj_wektory (matrix):
    new_matrix = matrix
    for i in range(len(matrix[0])):
        mod = dlugosc_vektora(matrix[i,:])
        for j in range(len(matrix[0,:])):
            new_matrix[i,j] = matrix[i,j]/mod
    return new_matrix

def zmiana_bazy (staraBaza, nowaBaza, vector):
    if czy_wektory_ortagonalne(nowaBaza):
        if czy_wektory_ortonormalne(nowaBaza):
            return np.dot(nowaBaza.T, vector)
        return np.dot(np.dot(nowaBaza.T, staraBaza), vector)
    return np.dot(np.dot(np.linalg.inv(nowaBaza), staraBaza), vector)

print(czy_wektory_ortagonalne(B_T))
B_T_norm = normalizuj_wektory(B_T)
print(czy_wektory_ortonormalne(B_T_norm))

vector_stary = np.array([8,6,2,3,4,6,6,5])
vector_nowy = zmiana_bazy(I, B, vector_stary)
print(vector_nowy)