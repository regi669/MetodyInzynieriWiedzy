import math

matrix = []

with open("LAB3/australian.dat","r") as f:
    matrix = [list(map(lambda x: float(x), line.split())) for line in f]

#print(matrix)

def euclides_metric(list1, list2):
    result = 0
    for i in range(len(list1) - 1):
        result += (list1[i]-list2[i]) ** 2
    return math.sqrt(result)

print(euclides_metric(matrix[0], matrix[1]))
print(euclides_metric(matrix[0], matrix[2]))
print(euclides_metric(matrix[0], matrix[3]))

results = [euclides_metric(matrix[0], matrix[i]) for i in range(1, len(matrix))]
print(results)

def grupowanie_australijczykow(lista, nr_indexu_decyzyjna):
    grupy = dict()
    y = lista[0]
    for x in range(1,len(lista)):
        decyzyjna = lista[x][nr_indexu_decyzyjna]
        if decyzyjna in grupy.keys():
            grupy[decyzyjna].append(euclides_metric(y, lista[x]))
        else:
            grupy[decyzyjna]=[euclides_metric(y, lista[x])]
    return grupy

print("********** Dom **********")
print(grupowanie_australijczykow(matrix,14))