import csv
import statistics
import timeit

import matplotlib.pyplot as plt

from lista_arreglo import ListaArreglo

TAMANOS = [1000, 10000, 80000, 200000]
REPETICIONES = 5

OPERACIONES = {
    "insertar": lambda lista, n: lista.insertar(0, -1),
    "insertar_al_final": lambda lista, n: lista.insertar(lista.tamano(), -1),
    "insertar_ordenado": lambda lista, n: lista.insertar_ordenado(n // 2),
    "obtener": lambda lista, n: lista.obtener(n // 2),
    "buscar_lineal": lambda lista, n: lista.buscar_lineal(-1),
    "buscar_binaria": lambda lista, n: lista.buscar_binaria(-1),
}


def lista_de_tamano(n):
    lista = ListaArreglo()
    for i in range(n):
        lista.insertar(i, i)
    return lista


def mediana_de_tiempos(operacion, n):
    lista = lista_de_tamano(n)
    tiempos = [timeit.timeit(lambda: operacion(lista, n), number=1) for _ in range(REPETICIONES)]
    return statistics.median(tiempos)


filas = [
    {"tamano": n, "operacion": nombre, "tiempo_s": mediana_de_tiempos(operacion, n)}
    for n in TAMANOS
    for nombre, operacion in OPERACIONES.items()
]

with open("resultados.csv", "w", newline="") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=["tamano", "operacion", "tiempo_s"])
    escritor.writeheader()
    escritor.writerows(filas)

for nombre in OPERACIONES:
    puntos = [f for f in filas if f["operacion"] == nombre]
    plt.plot([p["tamano"] for p in puntos], [p["tiempo_s"] for p in puntos], marker="o", label=nombre)

plt.xscale("log")
plt.xlabel("tamaño del catalogo (n, escala logaritmica)")
plt.ylabel("tiempo (segundos, mediana de 5 repeticiones)")
plt.title("Tiempo de cada operacion de ListaArreglo segun n")
plt.legend()
plt.savefig("grafica_operaciones.png")
