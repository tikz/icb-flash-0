import random


def generarMazo(n):
    mazo = []
    for _ in range(n):  # jugadores
        for _ in range(4):  # palo
            for x in range(1, 14):  # valores
                mazo.append(x)

    random.shuffle(mazo)
    return mazo


def jugar(m):
    suma = 0
    while suma < 21:
        if len(m) != 0:
            carta = m.pop(0)
            suma += carta
    return suma


def jugar_varios(m, j):
    res = []
    for _ in range(j):
        res.append(jugar(m))
    return res


def jugarMiedo(m):
    suma = 0
    while suma < 19:
        if len(m) != 0:
            carta = m.pop(0)
            suma += carta
    return suma


def jugarBorracho(m):
    suma = 0

    # Siempre saco una carta primero
    suma += m.pop(0)

    # Y ahora me pongo en pedo
    while random.random() > 0.5 and suma < 21:
        suma += m.pop(0)

    return suma
