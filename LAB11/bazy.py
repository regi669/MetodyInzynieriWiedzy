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

def czy_diagonalna (matrix):
    for i in range(len(matrix[0])):
        for j in range(len(matrix[:,0])):
            if i != j:
                if matrix[i,j] != 0:
                    return False
    return True

def czy_jednostkowa (matrix):
    for i in range(len(matrix[0])):
        for j in range(len(matrix[:,0])):
            if i == j:
                if matrix[i,j] != 1:
                    return False
            elif i != j:
                if matrix[i,j] != 0:
                    return False
    return True

def iloczyn_skalarny(matrix):
    return np.dot(matrix, matrix.T)

def czy_wektory_ortagonalne (matrix):
    return czy_diagonalna(iloczyn_skalarny(matrix))

def czy_wektory_ortonormalne (matrix):
    return czy_jednostkowa(iloczyn_skalarny(matrix))

def dlugosc_vektora (vektor):
    return np.sqrt(iloczyn_skalarny(vektor))

def normalizuj_wektory (matrix):
    new_matrix = matrix
    for i in range(len(matrix[0])):
        mod = dlugosc_vektora(matrix[i,:])

        for j in range(len(matrix[0,:])):
            new_matrix[i,j] = matrix[i,j]/mod
    return new_matrix

print(czy_wektory_ortagonalne(B_T))
B_T_norm = normalizuj_wektory(B_T)
print(czy_wektory_ortonormalne(B_T_norm))

vector_stary = np.array([8,6,2,3,4,6,6,5])
vector_nowy = np.dot(B_T, vector_stary)
print(vector_nowy)