import pytest
from lista_arreglo import ListaArreglo
from lista_enlazada import ListaEnlazada

IMPLEMENTACIONES = [ListaArreglo, ListaEnlazada]


@pytest.fixture(params=IMPLEMENTACIONES)
def Lista(request):
    return request.param


def test_lista_vacia(Lista):
    """CA-01: una lista nueva tiene tamaño 0."""
    assert Lista().tamaño() == 0


def test_insertar_en_vacia(Lista):
    """CA-02: insertar en posición 0 en lista vacía."""
    lista = Lista()
    assert lista.insertar(0, "a") is True
    assert lista.tamaño() == 1
    assert lista.obtener(0) == "a"


def test_insertar_inicio(Lista):
    """CA-03: insertar al inicio desplaza sin perder elementos."""
    lista = Lista()
    lista.insertar(0, "b")
    lista.insertar(1, "c")
    lista.insertar(0, "a")
    assert lista.obtener(0) == "a"
    assert lista.obtener(1) == "b"
    assert lista.obtener(2) == "c"


def test_eliminar(Lista):
    """CA-04: eliminar reduce el tamaño y devuelve el elemento."""
    lista = Lista()
    lista.insertar(0, "x")
    assert lista.eliminar(0) == "x"
    assert lista.tamaño() == 0


def test_posicion_invalida(Lista):
    """CA-05: con una posición fuera de rango, obtener devuelve None e insertar devuelve False."""
    lista = Lista()
    assert lista.obtener(0) is None
    assert lista.insertar(5, "x") is False
    assert lista.insertar(-1, "x") is False
    assert lista.tamaño() == 0


def test_buscar_ausente(Lista):
    """CA-06: buscar devuelve -1 si no está."""
    assert Lista().buscar("fantasma") == -1


def test_redimensionamiento(Lista):
    """CA-07: insertar 100 canciones seguidas no pierde ni desordena ninguna."""
    lista = Lista()
    for i in range(100):
        lista.insertar(i, i)
    assert lista.tamaño() == 100
    for i in range(100):
        assert lista.obtener(i) == i
