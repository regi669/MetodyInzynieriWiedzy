import numpy as np
import math

PI = 3.141592653589793


def factorial(x):
    if x == 0:
        return 1
    if x > 0:
        x = x * factorial(x - 1)
    return x


def func1(x):
    return x


def func1_int(a, b):
    return (1 / 2) * (b ** 2 - a ** 2)


def func2(x):
    return math.sin(x)


def sin(x):
    taylor_expansions = 20
    m = {0: 1, 1: 0, 2: -1, 3: 0}
    delta = x - PI / 2
    return sum([m[y % 4] * delta ** y / factorial(y) for y in range(20)])


def func2_int(a, b):
    return math.cos(a) - math.cos(b)


def mc_integrate(func, a, b, n=10000):
    losowe_wartosci = np.random.uniform(a, b, n)
    y = [func(wartosc) for wartosc in losowe_wartosci]
    y_srednia = np.sum(y) / n
    wynik = (b - a) * y_srednia
    return wynik


def rectangle_integrate(func, a, b, n=10000):
    x = np.linspace(a, b, n)
    y = func(x)  # wysokosc kwadrata
    wynik = np.sum(y) * (b - a) / n  # suma wysokosci pomnozona przez szerokość
    return wynik


print('MC x = {}'.format(mc_integrate(func1, -2, 5)))
print('RI x = {}'.format(rectangle_integrate(func1, -2, 5)))
print('Real Value x = {}'.format(func1_int(-2, 5)))

print('MC sin(x) = {}'.format(mc_integrate(func2, -2, 5)))
print('RI sin(x) = {}'.format(rectangle_integrate(sin, -2, 5)))
print('Real Value sin(x) = {}'.format(func2_int(-2, 5)))