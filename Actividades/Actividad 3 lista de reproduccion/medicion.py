# Mide las cuatro operaciones de la emisora en las dos listas,
# con 5000 canciones. Ejecutar: python medicion.py

import time
from lista_arreglo import ListaArreglo
from lista_enlazada import ListaEnlazada

CANCIONES = 5000
MITAD = 2500

NOMBRES = ["insertar al principio", "recorrer toda la lista",
           "ir a la cancion N", "borrar la cancion actual"]
VECES_AL_DIA = [40, 3, 200, 15]


def llenar(lista):
    for i in range(CANCIONES):
        lista.insertar(lista.tamaño(), i)


def insertar_al_principio(lista):
    repeticiones = 200
    inicio = time.perf_counter()
    for i in range(repeticiones):
        lista.insertar(0, "x")
    tiempo = time.perf_counter() - inicio
    # Devuelvo la lista a 5000 canciones
    for i in range(repeticiones):
        lista.eliminar(0)
    return tiempo / repeticiones * 1000000


def recorrer(lista):
    repeticiones = 20
    inicio = time.perf_counter()
    for i in range(repeticiones):
        lista.a_lista()
    tiempo = time.perf_counter() - inicio
    return tiempo / repeticiones * 1000000


def ir_a_la_cancion(lista):
    repeticiones = 200
    inicio = time.perf_counter()
    for i in range(repeticiones):
        lista.obtener(MITAD)
    tiempo = time.perf_counter() - inicio
    return tiempo / repeticiones * 1000000


def borrar_la_cancion(lista):
    # Solo se mide eliminar; volver a poner la cancion no cuenta
    repeticiones = 100
    tiempo = 0
    for i in range(repeticiones):
        inicio = time.perf_counter()
        lista.eliminar(MITAD)
        tiempo = tiempo + (time.perf_counter() - inicio)
        lista.insertar(MITAD, "x")
    return tiempo / repeticiones * 1000000


def medir(lista):
    llenar(lista)
    tiempos = []
    tiempos.append(insertar_al_principio(lista))
    tiempos.append(recorrer(lista))
    tiempos.append(ir_a_la_cancion(lista))
    tiempos.append(borrar_la_cancion(lista))
    return tiempos


arreglo = medir(ListaArreglo())
enlazada = medir(ListaEnlazada())

print("Lista de", CANCIONES, "canciones. Tiempos en microsegundos por ejecucion.")
print()
print("| Operacion | Veces al dia | Arreglo (us) | Enlazada (us) |")
print("|---|---|---|---|")
for i in range(4):
    print(f"| {NOMBRES[i]} | {VECES_AL_DIA[i]} | {arreglo[i]:.2f} | {enlazada[i]:.2f} |")

print()
print("Costo de un dia de emision (veces x tiempo, en milisegundos):")
print()
print("| Operacion | Arreglo (ms) | Enlazada (ms) |")
print("|---|---|---|")
total_arreglo = 0
total_enlazada = 0
for i in range(4):
    dia_arreglo = VECES_AL_DIA[i] * arreglo[i] / 1000
    dia_enlazada = VECES_AL_DIA[i] * enlazada[i] / 1000
    total_arreglo = total_arreglo + dia_arreglo
    total_enlazada = total_enlazada + dia_enlazada
    print(f"| {NOMBRES[i]} | {dia_arreglo:.3f} | {dia_enlazada:.3f} |")
print(f"| Total del dia | {total_arreglo:.3f} | {total_enlazada:.3f} |")
