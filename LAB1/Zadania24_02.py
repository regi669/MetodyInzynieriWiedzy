from ctypes import sizeof

#Zadanie 1
#input1 = input("Wpisz swoje imię \n");
#print('Cześć, {imie}!'.format(imie = input1))

#Zadanie 2
a = "Kappa"
b = 10
c = 150.15
print('Nazwa: a, Typ {type}, Wartosc {wartosc}'.format(type = type(a), wartosc = a))
print('Nazwa: b, Typ {type}, Wartosc {wartosc}'.format(type = type(b), wartosc = b))
print('Nazwa: c, Typ {type}, Wartosc {wartosc}'.format(type = type(c), wartosc = c))

#Zadanie 3
ListaStringow = ["Kappa", "Lis", "Pies", "Kot"]
x = "#".join(ListaStringow)
nowalista = x
print(x)

#Zadanie 4
y = x.split("#")
print(y)

#Zadanie 5
z = "Metody Inżynierii Wiedzy są najlepsze"
print('{napis}, dlugosc = {dlugosc}'.format(napis = z, dlugosc = len(z)))

z1 = z.lower()
print(z1)

#Zadanie 6
z2 = z.replace('ż', 'z').replace('ą', 'a').replace(' ', '')
print('{napis}, dlugosc = {dlugosc}'.format(napis = z2, dlugosc = len(z2)))

#Zadanie 7
set1 = set(z2)
print(set1)
print(len(set1))

#Zadanie 8
x1 = "Kappa123"
x2 = 15
para = (x1, x2)
print('wartosc {zmienna}, typ {typ}'.format(zmienna = para, typ = type(para)))

#Zadanie 9
listajezykow = ['C', 'C++', 'Java', 'Python']
print(len(listajezykow))
print(listajezykow.index('Python'))

#Zadanie 10
print(ListaStringow)
print(listajezykow)
nowalista = ListaStringow + listajezykow
print(nowalista)
ListaStringow.extend(listajezykow)
print(ListaStringow)

#Zadanie 11
slownik = {'poslka' : 'warszawa', 'rosja' : 'moskwa', 'litwa' : 'wilno', 'czechy' : 'praga', 'niemcy' : 'berlin', 'słowacja' : 'bratysława'}
wartosci = slownik.values()
sortedwartosci = sorted(wartosci)
print(wartosci)
posortowany = {}

#Zadanie 12 - do domu posortowany slownik
for i in sortedwartosci:
    for k in slownik.keys():
        if slownik[k] == i:
            posortowany[k] = slownik[k]
            break

print(posortowany)

#Zadanie 13
print(bool(' '))
print(bool(''))
print(bool('1'))
print(bool('0'))
print(bool(['','']))

#Zadanie 14
zdanie = "Ala ma kota"

if (len(set(zdanie)) > 15):
    print("this sentence has more than 15 unique characters")
else:
    print("this sentence has less than 15 unique characters")

#Zadanie 15
if 'j' in zdanie:
    print('Tak')

#Zadanie 16
for i in range(10):
    print(i)

#Zadanie 17
ListaStringow2 = ["Kappa", "Lis", "Pies", "Kot"]
nowa = "#".join(ListaStringow2)

print(nowa)
nowysrt = ''
for x in nowa:
    if x != '#':
        nowysrt = nowysrt + x
    else:
        nowysrt = nowysrt + ' '
print(nowysrt)
