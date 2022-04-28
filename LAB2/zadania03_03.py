#Zadanie 1
def czy_silne (password):
    male = False
    duze = False
    wykrzyknik = False
    if len(password) < 10:
        return False
    for x in password:
        if x in 'abcdefghijklmnopqrstuvwxyz':
            male = True
        elif x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            duze = True
        elif x == '!':
            wykrzyknik = True
    if male and duze and wykrzyknik:
        return True
    return False
password = '189!1aA012'
print(czy_silne(password))

#Zadanie 2
lista = [1, 2, 99, 3, 5]

for x in lista:
    if x == 99:
        continue
    print(x)


#Zadanie 3

def czy_nalezy (lista, liczba):
    nalezy = False
    while(liczba in lista):
        nalezy = True
        break
    return nalezy

print(czy_nalezy([1, 2, 3, 4, 5], 5))


#Zadanie 4

with open("LAB2/plik.txt", "r") as f:
    lines = f.readlines()

    for x in lines:
        print (x, end='')
    print('\n')


#Zadanie 5

listajezykow = ['C', 'C++', 'Java', 'Python']

with open("LAB2/plik.txt", "w") as f:
    for x in listajezykow:
        print(x, file=f, end=' ')


#Zadanie 6

listanowa = ['Olsztyn', 'Warszawa', 'Krakow', 'Lodz']

nowanowa = list(map(lambda x : x[:3], listanowa))
print(nowanowa)


#Zadanie 7

listaplikow = ['plik.txt', 'plik.docx', 'plik.pdf', 'plik2.txt']

def znajdzplik (lista, rozszerzenie):
    nowalista = []
    rozszerzenie = '.' + rozszerzenie
    for x in lista:
        if rozszerzenie in x:
            nowalista.append(x)
    return nowalista

listanowanowa = znajdzplik(listaplikow, 'txt')
print(listanowanowa)

#Zadanie 8

#Przesłuchać wykłady - i następny wyklad