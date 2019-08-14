from main import generarMazo, jugar, jugarMiedo, jugarBorracho
from opcionales import jugarSmart, jugarSmart2


def quienGano(lista):
    # quienGano recibe una lista con las sumas de cada jugador y devuelve el index del jugador que gano.
    # Si no gano nadie, devuelve None.
    # Si hay empate entre dos o mas jugadores, tambien devuelve None.

    # Primero creo una lista con tuplas que contengan (index, suma)
    l = [(i, x) for i, x in enumerate(lista)]

    # Solo me interesan los que no se pasaron de 21.
    l = [x for x in l if x[1] <= 21]

    if len(l) == 0:
        return None  # Se pasaron todos de 21, perdieron todos.
    elif len(l) == 1:
        return l[0][0]  # Hay uno solo que no perdio por pasarse. Gano ese.

    distancias = [(i, 21 - x) for i, x in l]

    # Ordeno la lista de forma decreciente en base a la distancia al 21.
    distancias.sort(key=lambda x: x[1])

    # El primer jugador de la lista ordenada tiene la misma distancia que el 2do. Hay un empate entre esos dos (o mas jugadores).
    if distancias[0][1] == distancias[1][1]:
        return None
    else:
        return distancias[0][0]


def benchmarkEstrategia(lista_funcs, n=1000):
    # benchmarkEstrategia recibe una lista de funciones estilo jugar(), realiza n partidas
    # y devuelve una lista con tuplas (nombreFuncion, winrate).

    ganadores = []

    print(f"Haciendo {n} partidas con un mazo nuevo cada una...")
    for _ in range(n):
        mazo = generarMazo(len(lista_funcs))

        puntajes = []
        for f in lista_funcs:
            puntajes.append(f(mazo))
        ganadores.append(quienGano(puntajes))

    winrates = []
    for i, _ in enumerate(lista_funcs):
        wins = 0
        for g in ganadores:
            if i == g:
                wins += 1
        winrates.append(wins / n)

    return [(func.__name__, winrate) for func, winrate in zip(lista_funcs, winrates)]
