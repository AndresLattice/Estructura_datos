"""Mide las cuatro operaciones de la emisora en las dos listas.

Lista de 5.000 canciones. Cada operación se repite varias veces y se
promedia el tiempo de una sola ejecución. Ejecutar: python medicion.py
"""

from time import perf_counter

from lista_arreglo import ListaArreglo
from lista_enlazada import ListaEnlazada

CANCIONES = 5000
MITAD = CANCIONES // 2

# Veces al día, dadas por la emisora.
FRECUENCIAS = {
    "insertar al principio": 40,
    "recorrer toda la lista": 3,
    "ir a la canción N": 200,
    "borrar la canción actual": 15,
}


def crear(Lista):
    lista = Lista()
    for i in range(CANCIONES):
        lista.insertar(0, i)
    return lista


def promedio_us(operacion, repeticiones):
    """Tiempo promedio de una ejecución de `operacion`, en microsegundos."""
    total = 0
    for _ in range(repeticiones):
        inicio = perf_counter()
        operacion()
        total += perf_counter() - inicio
    return total / repeticiones * 1_000_000


def medir(Lista):
    lista = crear(Lista)
    tiempos = {}

    tiempos["insertar al principio"] = promedio_us(lambda: lista.insertar(0, "x"), 200)
    for _ in range(200):
        lista.eliminar(0)  # devuelve la lista a 5.000 canciones

    def recorrer():
        for _ in lista:
            pass

    tiempos["recorrer toda la lista"] = promedio_us(recorrer, 20)
    tiempos["ir a la canción N"] = promedio_us(lambda: lista.obtener(MITAD), 200)

    # Se mide solo eliminar; devolver la canción a su sitio no cuenta.
    total = 0
    repeticiones = 100
    for _ in range(repeticiones):
        inicio = perf_counter()
        lista.eliminar(MITAD)
        total += perf_counter() - inicio
        lista.insertar(MITAD, "x")
    tiempos["borrar la canción actual"] = total / repeticiones * 1_000_000

    return tiempos


if __name__ == "__main__":
    arreglo = medir(ListaArreglo)
    enlazada = medir(ListaEnlazada)

    print(f"Lista de {CANCIONES} canciones. Tiempos en microsegundos por ejecución.\n")
    print("| Operación | Veces al día | Arreglo (µs) | Enlazada (µs) |")
    print("|---|---|---|---|")
    total_arreglo = total_enlazada = 0
    for nombre, veces in FRECUENCIAS.items():
        print(f"| {nombre} | {veces} | {arreglo[nombre]:.2f} | {enlazada[nombre]:.2f} |")
        total_arreglo += veces * arreglo[nombre]
        total_enlazada += veces * enlazada[nombre]

    print("\nCosto de un día de emisión (frecuencia × tiempo, en milisegundos):\n")
    print("| Operación | Arreglo (ms) | Enlazada (ms) |")
    print("|---|---|---|")
    for nombre, veces in FRECUENCIAS.items():
        print(f"| {nombre} | {veces * arreglo[nombre] / 1000:.3f} | {veces * enlazada[nombre] / 1000:.3f} |")
    print(f"| **Total del día** | **{total_arreglo / 1000:.3f}** | **{total_enlazada / 1000:.3f}** |")
