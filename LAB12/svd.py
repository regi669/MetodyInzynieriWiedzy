import numpy as np
import math as m

np.set_printoptions(formatter={'float_kind':"{:.10f}".format})

def unifikacja (lista, blad_obliczeniowy=0.0000001):
    new_list = []
    for x in lista:
        if abs(x) <= blad_obliczeniowy:
            x = 0
        new_list.append(x)
    return np.array(new_list)

def pobierz_i_posortuj_wartosci_wlasne (matrix):
    return unifikacja(np.sort(np.linalg.eigvals(matrix))[::-1])

def wartosci_singularne_z_wartosci_wlasnych(wartosci_wlasne):
    wartosci_singularne = []
    for x in wartosci_wlasne:
        if x != 0:
            wartosci_singularne.append(np.sqrt(x))
    return np.array(wartosci_singularne)

def sortuj_wiersze(matrix):
    return matrix.T[::-1].T

def oblicz_sigme(matrix, wartosci_singularne):
    i, j = matrix.shape
    sigma = np.zeros((i, j))
    for x in range(i):
        for y in range(j):
            if x == y:
                sigma[x][y] = wartosci_singularne[x]
    return sigma

def svd (matrix):
    AAT = np.dot(matrix, matrix.T)
    AAT_S = AAT.shape[0]
    ATA = np.dot(matrix.T, matrix)
    ATA_S = ATA.shape[0]
    if AAT_S > ATA_S:
        wartosci_wlasne = pobierz_i_posortuj_wartosci_wlasne(AAT)
        wartosci_singularne = wartosci_singularne_z_wartosci_wlasnych(wartosci_wlasne)
        U = sortuj_wiersze(np.linalg.eigh(AAT)[1])
        U = np.array([unifikacja(x) for x in U])
        V = np.array([(np.dot(matrix.T, U.T[x]) * (1/wartosci_singularne[x])) for x in range(ATA_S)])
        V = np.array([unifikacja(x) for x in V])
    else:
        wartosci_wlasne = pobierz_i_posortuj_wartosci_wlasne(ATA)
        wartosci_singularne = wartosci_singularne_z_wartosci_wlasnych(wartosci_wlasne)
        V = sortuj_wiersze(np.linalg.eigh(ATA)[1])
        V = np.array([unifikacja(x) for x in V])
        U = np.array([(np.dot(matrix, V.T[x]) * (1/wartosci_singularne[x])) for x in range(AAT_S)])
        U = np.array([unifikacja(x) for x in U])
        U = sortuj_wiersze(U)
    sigma = oblicz_sigme(matrix, wartosci_singularne)
    return U, sigma, V.T

A = np.array([
    [1, 1],
    [0, 1],
    [-1,1]
])

B = np.array([
    [1, -2, 0],
    [0, -2, 1]
])
print("Macierz 1\n")
U, sigma, V_T = svd(A)
print(U, sigma, V_T, sep="\n\n")
print("\nMacierz 2\n")
U, sigma, V_T = svd(B)
print(U, sigma, V_T, sep="\n\n")