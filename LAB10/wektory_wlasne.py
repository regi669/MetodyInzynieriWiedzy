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
        vector_u = vector_v - suma
        matrix_u.append(vector_u)
        if dlugosc(vector_u) == 0:
            vector_e = vector_u
        else:
            vector_e = (1 / dlugosc(vector_u)) * vector_u
        matrix_q.append(vector_e)
        
    return np.array(matrix_q).T

def macierz_k(matrix_a):
    matrix_q = q_dekompozycja(matrix_a)
    matrix_a_new = np.dot(np.dot(matrix_q.T, matrix_a), matrix_q)
    return matrix_a_new

def matrix_wartosci_wlasne(matrix_a):
    matrix_a_new = matrix_a
    while (np.diag(matrix_a_new)-np.dot(matrix_a_new, np.ones((matrix_a_new.shape[0],1))).T).all()>0.0001:
        matrix_a_new = macierz_k(matrix_a_new)
    return matrix_a_new
      
def gauss(matrix):
    column_len = len(matrix.T[0])

    for x in range(column_len):
        if matrix[x][x] == 0:
            raise ZeroDivisionError()
            
        for y in range(column_len):
            if x != y:
                factor = matrix[y][x]/matrix[x][x]

                for z in range(column_len + 1):
                    matrix[y][z] = matrix[y][z] - factor * matrix[x][z]
    return [matrix[i][column_len]/matrix[i][i] for i in range(column_len)]

a=np.array([[1.,3.,5.,7.,9.],
            [3.,3.,3.,5.,7.],
            [5.,3.,5.,7.,9.],
            [7.,5.,7.,7.,9.],
            [9.,7.,9.,9.,9.]
])

np.set_printoptions(formatter={'float_kind':"{:.5f}".format})
print(a)
wartosci_wlasne = np.diag(matrix_wartosci_wlasne(a))
print(wartosci_wlasne)

b= np.array([[1, 3, 4],
            [2, 5, 8]
])

print(gauss(b))


