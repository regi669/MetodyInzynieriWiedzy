import math as m
import numpy as np

def regresja_liniowa (matrix):
    x = np.array([[1, i[0]] for i in matrix])
    y = np.array([i[1] for i in matrix])
    X = np.dot(x.T, x)
    X_inv = np.linalg.inv(X)
    inv = np.dot(X_inv, x.T)
    return np.dot(inv, y)

matrix = np.array([
    [2,1],
    [5,2],
    [7,3],
    [8,3]])
print(regresja_liniowa(matrix))