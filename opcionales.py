import random
from main import *
from fun import *

# Del enunciado de compararEstrategia
# index 0=jugar, 1=jugarMiedo, 2=jugarBorracho, 3=jugarSmart, 4=jugarSmart2
funcs = [jugar, jugarMiedo, jugarBorracho, jugarSmart, jugarSmart2]


def jugarSmart(m):
    suma = 0

    while random.random() > suma/20 and suma < 21:
        carta = m.pop(0)
        suma += carta

    return suma


def jugarSmart2(m):
    suma = 0
    n = 0

    # Por cada carta que saque, se cambia el limite de corte
    # hasta 5 cartas ya que 5*1/5 = 1 y random.random() devuelve entre [0,1)
    while random.random() > n*1/5 and suma < 21:
        carta = m.pop(0)
        suma += carta
        n += 1

    return suma


def compararEstrategia(lista_jug):
    mazo = generarMazo(len(lista_jug))

    res = []
    for j in lista_jug:
        res.append(funcs[j](mazo))
    return res
