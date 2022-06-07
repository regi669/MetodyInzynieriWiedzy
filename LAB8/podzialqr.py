import math as m
import numpy as np

def dlugosc(matrix):
    return m.sqrt(np.dot(matrix.T,matrix))

def projekcja(matrix_u, matrix_v):
    matrix_u_v = np.dot(matrix_u.T,matrix_v)
    matrix_u_u = np.dot(matrix_u.T,matrix_u)
    if matrix_u_u == 0:
        return matrix_u
    return (matrix_u_v/matrix_u_u)*matrix_u


def q_dekompozycja(matrix_a):
    matrix_v=[ [ x[y] for x in matrix_a ] for y in range(len(matrix_a[1])) ]
    matrix_u = []
    matrix_q = []
    for vector_v in matrix_v:
        vector_v = np.array(vector_v)
        suma = 0
        for vector_u in matrix_u:
            vector_u = np.array(vector_u)
            suma += projekcja(vector_u, vector_v)
        vector_u = vector_v - suma #Suma projekcji na macierz v, dla 1 u jest równa 0 dlatego v1=u1, dla większych macierzy sumuje wszsytkie projekcję na dany vektor
        matrix_u.append(vector_u)
        if dlugosc(vector_u) == 0:
            vector_e = vector_u
        else:
            vector_e = (1 / dlugosc(vector_u)) * vector_u
        matrix_q.append(vector_e)
        
    return np.array(matrix_q).T

a = np.array([
    [1, 0],
    [0, 1],
    [2, 1],
])

q = q_dekompozycja(a)
r = np.dot(q.T,a)
matrix_a_new = np.dot(q,r)
np.set_printoptions(formatter={'float_kind':"{:.5f}".format})
print(q)
print(r)
print(matrix_a_new)