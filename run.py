import main
import opcionales
import fun

print("=== FUNCIONES OBLIGATORIAS ==")

print("generarMazo(2)")
m = main.generarMazo(2)
print(m)

print("jugar(m)")
print(main.jugar(m))
# print(jugarSmart(m))
# # print(comparar_estrategia([0, 1]))
nombres = ["jugar", "jugarMiedo", "jugarBorracho", "jugarSmart", "jugarSmart2"]
jugadores = [0, 1, 2, 3, 4]
m = fun.generarMazo(len(jugadores))
winrates = fun.compararEstrategia2(jugadores)

for i, w in enumerate(winrates):
    print(nombres[i], "=", w)
