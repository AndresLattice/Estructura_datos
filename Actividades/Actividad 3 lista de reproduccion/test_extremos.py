# Casos extremos (CA-08 a CA-12) y pruebas de consistencia (CA-13, CA-14).

import pytest
from lista_arreglo import ListaArreglo
from lista_enlazada import ListaEnlazada


@pytest.mark.parametrize("Lista", [ListaArreglo, ListaEnlazada])
def test_eliminar_de_vacia(Lista):
    """CA-08: en una lista vacía, obtener y eliminar devuelven None y el tamaño sigue en 0."""
    lista = Lista()
    assert lista.obtener(0) is None
    assert lista.eliminar(0) is None
    assert lista.tamaño() == 0


def test_insertar_en_vacia_fija_cabeza_y_cola():
    """CA-09: insertar el primer elemento deja tamaño 1 y cabeza y cola en el mismo nodo."""
    lista = ListaEnlazada()
    lista.insertar(0, "único")
    assert lista.cabeza is lista.cola
    assert lista.tamaño() == 1


def test_eliminar_unico_deja_lista_consistente():
    """CA-10: eliminar el único elemento deja cabeza Y cola en None y tamaño 0."""
    lista = ListaEnlazada()
    lista.insertar(0, "único")
    lista.eliminar(0)
    assert lista.cabeza is None
    assert lista.cola is None       # el error más común: olvidar esta línea
    assert lista.tamaño() == 0


def test_eliminar_cabeza_con_varios():
    """CA-11: borrar el primero conserva el resto en orden."""
    lista = ListaEnlazada()
    lista.insertar(0, "a")
    lista.insertar(1, "b")
    lista.insertar(2, "c")
    assert lista.eliminar(0) == "a"
    assert lista.tamaño() == 2
    assert lista.a_lista() == ["b", "c"]
    assert lista.cabeza.dato == "b"


def test_eliminar_ultimo_actualiza_cola():
    """CA-12: al borrar el último, el tamaño baja, el resto queda igual y la cola pasa al penúltimo."""
    lista = ListaEnlazada()
    lista.insertar(0, "a")
    lista.insertar(1, "b")
    lista.insertar(2, "c")
    assert lista.eliminar(2) == "c"
    assert lista.tamaño() == 2
    assert lista.a_lista() == ["a", "b"]
    assert lista.cola.dato == "b"
    assert lista.cola.siguiente is None


def test_insertar_y_eliminar_alternado():
    """CA-13: estrés: la lista debe quedar consistente tras muchas operaciones."""
    lista = ListaEnlazada()
    for i in range(50):
        lista.insertar(0, i)
    for i in range(25):
        lista.eliminar(0)
    assert lista.tamaño() == 25
    assert lista.cola.siguiente is None


@pytest.mark.parametrize("Lista", [ListaArreglo, ListaEnlazada])
def test_recorrer_en_orden(Lista):
    """CA-14: recorrer devuelve todas las canciones en orden."""
    lista = Lista()
    lista.insertar(0, "a")
    lista.insertar(1, "b")
    lista.insertar(2, "c")
    lista.insertar(3, "d")
    assert lista.a_lista() == ["a", "b", "c", "d"]
