# Código base — Semana 07
# Fuente: 02-Momento-2-Disciplina-y-jerarquia/07-Semana-07-Listas-dobles-y-circulares/02-guia-de-laboratorio.html

from lista_circular import ListaCircular

jugadores = ListaCircular()
for nombre in ["Ana", "Beto", "Carla", "Dani"]:
    jugadores.agregar(nombre)

print("Orden de la ronda:", list(jugadores))

# Tres rondas completas
for ronda in range(1, 4):
    print(f"\n--- Ronda {ronda} ---")
    for _ in range(len(jugadores)):
        print(f"  Turno de {jugadores.actual()}")
        jugadores.avanzar()

# Un jugador se retira en medio de la partida
print("\nCarla se retira...")
while jugadores.actual() != "Carla":
    jugadores.avanzar()
jugadores.eliminar_actual()
print("Jugadores restantes:", list(jugadores))
print("Turno actual:", jugadores.actual())
