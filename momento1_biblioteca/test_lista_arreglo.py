import pytest

from lista_arreglo import ListaArreglo


@pytest.fixture
def lista():
    return ListaArreglo()


def test_lista_nueva_esta_vacia(lista):
    """CA-01: una lista recien creada tiene tamaño 0."""
    assert lista.tamano() == 0


def test_obtener_en_vacia_lanza_error(lista):
    """CA-02: obtener una posicion en una lista vacia se rechaza."""
    with pytest.raises(ValueError):
        lista.obtener(0)


def test_insertar_en_lista_vacia(lista):
    """CA-03: insertar en la posicion 0 de una lista vacia deja un elemento."""
    lista.insertar(0, 10)
    assert lista.tamano() == 1
    assert lista.obtener(0) == 10


def test_insertar_al_inicio_desplaza(lista):
    """CA-04: insertar al inicio desplaza los elementos existentes."""
    lista.insertar(0, 1)
    lista.insertar(0, 2)
    lista.insertar(0, 3)
    assert lista.obtener(0) == 3
    assert lista.obtener(1) == 2
    assert lista.obtener(2) == 1


def test_insertar_al_final_no_desplaza(lista):
    """CA-05: insertar al final no desplaza ningun elemento existente."""
    lista.insertar(0, 1)
    lista.insertar(1, 2)
    lista.insertar(2, 3)
    assert lista.obtener(0) == 1
    assert lista.obtener(1) == 2
    assert lista.obtener(2) == 3


def test_insertar_en_medio_desplaza_lo_necesario(lista):
    """CA-06: insertar en una posicion intermedia desplaza solo los elementos posteriores."""
    lista.insertar(0, 1)
    lista.insertar(1, 3)
    lista.insertar(1, 2)
    assert lista.obtener(0) == 1
    assert lista.obtener(1) == 2
    assert lista.obtener(2) == 3


def test_insertar_posicion_negativa_lanza_error(lista):
    """CA-07: insertar con una posicion negativa se rechaza."""
    with pytest.raises(ValueError):
        lista.insertar(-1, 1)


def test_insertar_posicion_mayor_al_tamano_lanza_error(lista):
    """CA-08: insertar con una posicion mayor al tamaño se rechaza."""
    lista.insertar(0, 1)
    with pytest.raises(ValueError):
        lista.insertar(2, 99)


def test_insertar_ordenado_en_vacia(lista):
    """CA-09: insertar_ordenado en una lista vacia deja un elemento."""
    lista.insertar_ordenado(5)
    assert lista.tamano() == 1
    assert lista.obtener(0) == 5


def test_insertar_ordenado_mantiene_orden(lista):
    """CA-10: insertar_ordenado mantiene el orden ascendente."""
    for valor in [5, 1, 9, 3]:
        lista.insertar_ordenado(valor)
    assert [lista.obtener(i) for i in range(lista.tamano())] == [1, 3, 5, 9]


def test_insertar_ordenado_con_repetidos(lista):
    """CA-11: insertar_ordenado con un valor repetido lo coloca despues del ultimo igual."""
    for valor in [1, 5, 5, 9]:
        lista.insertar_ordenado(valor)
    lista.insertar_ordenado(5)
    assert [lista.obtener(i) for i in range(lista.tamano())] == [1, 5, 5, 5, 9]


def test_obtener_devuelve_elemento_correcto(lista):
    """CA-12: obtener devuelve el elemento correcto en una posicion valida."""
    lista.insertar(0, 7)
    lista.insertar(1, 8)
    assert lista.obtener(1) == 8


def test_obtener_posicion_negativa_lanza_error(lista):
    """CA-13: obtener con posicion negativa se rechaza."""
    lista.insertar(0, 1)
    with pytest.raises(ValueError):
        lista.obtener(-1)


def test_obtener_posicion_fuera_de_rango_lanza_error(lista):
    """CA-14: obtener con posicion igual o mayor al tamaño se rechaza."""
    lista.insertar(0, 1)
    with pytest.raises(ValueError):
        lista.obtener(1)


def test_buscar_lineal_en_vacia(lista):
    """CA-15: buscar_lineal en una lista vacia devuelve -1."""
    assert lista.buscar_lineal(1) == -1


def test_buscar_lineal_encuentra_elemento(lista):
    """CA-16: buscar_lineal encuentra un elemento presente y devuelve su posicion."""
    for valor in [4, 7, 2]:
        lista.insertar(lista.tamano(), valor)
    assert lista.buscar_lineal(7) == 1


def test_buscar_lineal_elemento_ausente(lista):
    """CA-17: buscar_lineal devuelve -1 si el elemento no esta."""
    for valor in [4, 7, 2]:
        lista.insertar(lista.tamano(), valor)
    assert lista.buscar_lineal(99) == -1


def test_buscar_binaria_en_vacia(lista):
    """CA-18: buscar_binaria en una lista vacia devuelve -1."""
    assert lista.buscar_binaria(1) == -1


def test_buscar_binaria_lista_de_un_elemento(lista):
    """CA-19: buscar_binaria encuentra un elemento en una lista de un elemento."""
    lista.insertar_ordenado(5)
    assert lista.buscar_binaria(5) == 0
    assert lista.buscar_binaria(9) == -1


def test_buscar_binaria_bordes_tamano_par(lista):
    """CA-20: buscar_binaria encuentra los bordes en una lista de tamaño par."""
    for valor in [1, 2, 3, 4]:
        lista.insertar_ordenado(valor)
    assert lista.buscar_binaria(1) == 0
    assert lista.buscar_binaria(4) == 3


def test_buscar_binaria_bordes_tamano_impar(lista):
    """CA-21: buscar_binaria encuentra los bordes en una lista de tamaño impar."""
    for valor in [1, 2, 3, 4, 5]:
        lista.insertar_ordenado(valor)
    assert lista.buscar_binaria(1) == 0
    assert lista.buscar_binaria(5) == 4


def test_buscar_binaria_elemento_ausente(lista):
    """CA-22: buscar_binaria devuelve -1 si el elemento no esta, en una lista de tamaño par."""
    for valor in [1, 2, 3, 4]:
        lista.insertar_ordenado(valor)
    assert lista.buscar_binaria(10) == -1
