# Código base — Semana 07
# Fuente: 02-Momento-2-Disciplina-y-jerarquia/07-Semana-07-Listas-dobles-y-circulares/02-guia-de-laboratorio.html

import pytest
from lista_doble import ListaDoble, PosicionInvalidaError


def verificar_consistencia(lista):
    """IR-02: para todo nodo, n.siguiente.anterior is n.
    Recorre en ambos sentidos y comprueba que coinciden."""
    hacia_adelante = list(lista)
    hacia_atras = list(reversed(lista))
    assert hacia_adelante == hacia_atras[::-1], "los enlaces no son consistentes"

    # Recorrido explícito verificando cada par de enlaces
    actual = lista._centinela
    for _ in range(lista.tamaño() + 1):
        assert actual.siguiente.anterior is actual, "enlace roto hacia atrás"
        assert actual.anterior.siguiente is actual, "enlace roto hacia adelante"
        actual = actual.siguiente
    assert actual is lista._centinela, "el recorrido no cerró en el centinela"


def test_vacia():
    lista = ListaDoble()
    assert lista.esta_vacia()
    assert lista.tamaño() == 0
    verificar_consistencia(lista)


def test_insertar_extremos():
    lista = ListaDoble()
    lista.insertar_al_final("b")
    lista.insertar_al_inicio("a")
    lista.insertar_al_final("c")
    assert list(lista) == ["a", "b", "c"]
    verificar_consistencia(lista)


def test_recorrido_inverso():
    lista = ListaDoble()
    for v in ["a", "b", "c"]:
        lista.insertar_al_final(v)
    assert list(reversed(lista)) == ["c", "b", "a"]


def test_eliminar_nodo_directo():
    """La ventaja de la lista doble: eliminar en O(1) con la referencia."""
    lista = ListaDoble()
    lista.insertar_al_final("a")
    nodo_b = lista.insertar_al_final("b")
    lista.insertar_al_final("c")
    lista.eliminar_nodo(nodo_b)          # sin recorrer nada
    assert list(lista) == ["a", "c"]
    verificar_consistencia(lista)


def test_eliminar_hasta_vaciar():
    lista = ListaDoble()
    for v in range(5):
        lista.insertar_al_final(v)
    for _ in range(5):
        lista.eliminar(0)
        verificar_consistencia(lista)
    assert lista.esta_vacia()


def test_no_se_puede_eliminar_centinela():
    lista = ListaDoble()
    with pytest.raises(ValueError):
        lista.eliminar_nodo(lista._centinela)
