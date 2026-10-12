# Código base — Semana 09
# Fuente: 02-Momento-2-Disciplina-y-jerarquia/09-Semana-09-Colas/02-guia-de-laboratorio.html

# COLA INGENUA — no la uses, solo mídela
class ColaIngenua:
    def __init__(self):
        self._datos = []

    def encolar(self, x):
        self._datos.append(x)         # O(1)

    def desencolar(self):
        return self._datos.pop(0)     # O(n) — ¡desplaza TODO el arreglo!


import time
N = 50_000
cola = ColaIngenua()
for i in range(N):
    cola.encolar(i)

inicio = time.perf_counter()
for _ in range(N):
    cola.desencolar()
print(f"{N:,} desencolados ingenuos: {time.perf_counter() - inicio:.3f} s")

# Duplica N y mide otra vez. ¿El tiempo se duplicó o se cuadruplicó?
# Anota la respuesta: es la evidencia de que es O(n) por operación.
