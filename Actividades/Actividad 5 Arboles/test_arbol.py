from arbol_carpetas import Carpeta, arbol_de_prueba, contar, profundidad
from arbol_carpetas import ruta_mas_profunda, por_niveles, con_pila


def test_contar():
    """CA-09: vacío da 0, un nodo da sus entregas, árbol de prueba da 14."""
    assert contar(None) == 0
    assert contar(Carpeta("Sola", 7)) == 7
    assert contar(arbol_de_prueba()) == 14


def test_profundidad():
    """CA-10: vacío da 0, un nodo da 1, árbol de prueba da 4."""
    assert profundidad(None) == 0
    assert profundidad(Carpeta("Sola", 7)) == 1
    assert profundidad(arbol_de_prueba()) == 4


def test_ruta_mas_profunda():
    """CA-11: la ruta más profunda del árbol de prueba es correcta."""
    assert ruta_mas_profunda(None) == []
    assert ruta_mas_profunda(Carpeta("Sola", 7)) == ["Sola"]
    esperada = ["Ingeniería", "Sistemas", "Estructuras de Datos", "2026-1"]
    assert ruta_mas_profunda(arbol_de_prueba()) == esperada


def test_por_niveles():
    """CA-12: vacío da [] y el árbol de prueba da el orden esperado."""
    assert por_niveles(None) == []
    esperado = ["Ingeniería",
                "Sistemas", "Civil",
                "Estructuras de Datos", "Programación",
                "2026-1", "2026-2", "2026-1"]
    assert por_niveles(arbol_de_prueba()) == esperado


def test_con_pila():
    """CA-13: con_pila da un orden distinto con las mismas carpetas."""
    assert con_pila(None) == []
    esperado = ["Ingeniería", "Civil", "Sistemas", "Programación",
                "2026-1", "Estructuras de Datos", "2026-2", "2026-1"]
    con_cola = por_niveles(arbol_de_prueba())
    con_la_pila = con_pila(arbol_de_prueba())
    assert con_la_pila == esperado
    assert con_la_pila != con_cola
    assert len(con_la_pila) == len(con_cola)
