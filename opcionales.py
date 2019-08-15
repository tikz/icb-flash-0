import random
from main import generarMazo, jugar, jugarMiedo, jugarBorracho


def jugarSmart(m, p_cutoff=0.6):
    # jugarSmart saca una carta solo si la probabilidad de mejorar la suma (sin pasarse de 21) es mayor a una probabilidad de corte arbitraria p_cutoff por defecto 0.6.
    # Para ello, lee el contenido de la lista mazo y calcula probabilidades para cada uno de los valores, sin saber su orden.
    # Si bien podría decirse que es hacer trampa, es análogo a "contar cartas" en donde se está al tanto de las cartas que salieron para deducir las que quedan.

    suma = 0
    p_mejorar = 1

    while suma < 21 and p_mejorar > p_cutoff and len(m) != 0:
        suma += m.pop(0)

        # probs contiene tuplas (valor_carta, probabilidad)
        probs = []
        for v in range(1, 14):
            probs.append((v, m.count(v) / len(m)))

        # max_sin_perder es el máximo valor de carta que puedo sacar para mejorar mi suma sin que me haga pasarme de 21.
        max_sin_perder = 21 - suma
        p_mejorar = sum([p for v, p in probs if v <= max_sin_perder])

    return suma


def jugarSmartSugerido(m):
    # La estrategia jugarSmart sugerida en el enunciado.
    suma = 0

    while random.random() > suma / 20 and suma < 21 and len(m) != 0:
        suma += m.pop(0)

    return suma


def compararEstrategia(lista_jug):
    mazo = generarMazo(len(lista_jug))

    funcs = [jugar, jugarMiedo, jugarBorracho, jugarSmart]
    res = []
    for j in lista_jug:
        res.append(funcs[j](mazo))

    return res
