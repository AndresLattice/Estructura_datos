from cola import Cola
from pila import Pila


class Carpeta:
    def __init__(self, nombre, entregas):
        self.nombre = nombre
        self.entregas = entregas
        self.hijos = []

    def agregar(self, hijo):
        self.hijos.append(hijo)
        return hijo


def arbol_de_prueba():
    """Árbol dibujado en recorridos.md. Tiene 14 entregas y profundidad 4."""
    ingenieria = Carpeta("Ingeniería", 0)
    sistemas = ingenieria.agregar(Carpeta("Sistemas", 0))
    estructuras = sistemas.agregar(Carpeta("Estructuras de Datos", 0))
    estructuras.agregar(Carpeta("2026-1", 5))
    estructuras.agregar(Carpeta("2026-2", 3))
    programacion = sistemas.agregar(Carpeta("Programación", 0))
    programacion.agregar(Carpeta("2026-1", 4))
    ingenieria.agregar(Carpeta("Civil", 2))
    return ingenieria


def contar(carpeta):
    """O(n). Total de entregas en la carpeta y todo lo que tiene adentro."""
    if carpeta is None:
        return 0
    total = carpeta.entregas
    for hijo in carpeta.hijos:
        total = total + contar(hijo)
    return total


def profundidad(carpeta):
    """O(n). Cantidad de carpetas en la ruta más larga."""
    if carpeta is None:
        return 0
    mayor = 0
    for hijo in carpeta.hijos:
        p = profundidad(hijo)
        if p > mayor:
            mayor = p
    return 1 + mayor


def ruta_mas_profunda(carpeta):
    """O(n). Lista de nombres de la ruta más larga."""
    if carpeta is None:
        return []
    mejor = []
    for hijo in carpeta.hijos:
        ruta = ruta_mas_profunda(hijo)
        # Con empate se queda la primera que encontró.
        if len(ruta) > len(mejor):
            mejor = ruta
    return [carpeta.nombre] + mejor


def por_niveles(raiz):
    """O(n). Nombres nivel por nivel, usando la cola."""
    resultado = []
    if raiz is None:
        return resultado
    pendientes = Cola()
    pendientes.encolar(raiz)
    while not pendientes.esta_vacia():
        actual = pendientes.desencolar()
        resultado.append(actual.nombre)
        for hijo in actual.hijos:
            pendientes.encolar(hijo)
    return resultado


def con_pila(raiz):
    """O(n). El mismo código de por_niveles, pero con una pila."""
    resultado = []
    if raiz is None:
        return resultado
    pendientes = Pila()
    pendientes.apilar(raiz)
    while not pendientes.esta_vacia():
        actual = pendientes.desapilar()
        resultado.append(actual.nombre)
        for hijo in actual.hijos:
            pendientes.apilar(hijo)
    return resultado


# Ejecutar: python arbol_carpetas.py
arbol = arbol_de_prueba()
print("Total de entregas:", contar(arbol))
print("Profundidad máxima:", profundidad(arbol))
print("Ruta más profunda:", ruta_mas_profunda(arbol))
print("Por niveles (cola):", por_niveles(arbol))
print("Con pila:", con_pila(arbol))
