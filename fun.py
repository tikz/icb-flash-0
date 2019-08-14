from main import *
from opcionales import *


def quienGano(lista):
    # Recibe una lista con las sumas de cada jugador (como la salida de jugar_varios) y devuelve
    # el index del jugador que gano.
    # Si no gano nadie, devuelve None.
    # Si hay empate (ej: los mejores puntajes son dos jugadores que tienen 20) considero que no gano
    # nadie, y tambien devuelvo None.

    # Primero creo una lista con tuplas que contengan (index, suma)
    l = [(i, x) for i, x in enumerate(lista)]

    # Solo me interesan los que no se pasaron de 21
    l = [x for x in l if x[1] <= 21]

    if len(l) == 0:
        return None  # Se pasaron todos de 21
    elif len(l) == 1:
        return l[0][0]  # Hay uno solo que todavia no perdio. Gano ese.

    distancias = [(i, 21-x) for i, x in l]

    # Ordeno la lista de forma creciente en base a la distancia al 21
    distancias.sort(key=lambda x: x[1])

    # El primer jugador de la lista ordenada tiene la misma distancia que el 2do. Hay un empate entre esos dos (o mas).
    if distancias[0][1] == distancias[1][1]:
        return None
    else:
        return distancias[0][0]


def compararEstrategia2(lista_jug):
    # compararEstrategia2 recibe una lista de jugadores al igual que compararEstrategia
    # pero realiza 1000 partidas y devuelve una lista con el winrate de cada jugador

    # 0=jugar, 1=jugarMiedo, 2=jugarBorracho, 3=jugarSmart, 4=jugarSmart2
    funcs = [jugar, jugarMiedo, jugarBorracho, jugarSmart, jugarSmart2]

    ganadores = []

    n = 1000

    print(f"Haciendo {n} partidas con un mazo nuevo cada una...")
    for _ in range(n):
        mazo = generarMazo(len(lista_jug))

        puntajes = []
        for j in lista_jug:
            puntajes.append(funcs[j](mazo))
        ganadores.append(quienGano(puntajes))

    winrates = []
    for jug in lista_jug:
        wins = 0
        for g in ganadores:
            if jug == g:
                wins += 1
        winrates.append(wins/n)

    return winrates
