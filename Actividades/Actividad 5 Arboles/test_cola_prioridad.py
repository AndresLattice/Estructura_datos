from cola_prioridad import ColaPrioridad


def test_orden_por_nivel():
    """CA-01: sale primero el nivel 1."""
    fila = ColaPrioridad()
    fila.encolar("Ana", 3, 0)
    fila.encolar("Luis", 1, 0)
    fila.encolar("Juan", 2, 0)
    assert fila.atender(0)["nombre"] == "Luis"
    assert fila.atender(0)["nombre"] == "Juan"
    assert fila.atender(0)["nombre"] == "Ana"


def test_empate_es_fifo():
    """CA-02: con empate sale el primero en llegar."""
    fila = ColaPrioridad()
    fila.encolar("primero", 2, 0)
    fila.encolar("segundo", 2, 0)
    assert fila.atender(0)["nombre"] == "primero"
    assert fila.atender(0)["nombre"] == "segundo"


def test_vacia_devuelve_none():
    """CA-03: atender con cola vacía devuelve None."""
    fila = ColaPrioridad()
    assert fila.esta_vacia()
    assert fila.atender(5) is None


def test_nivel_invalido():
    """CA-04: un nivel que no es 1, 2 o 3 devuelve False."""
    fila = ColaPrioridad()
    assert fila.encolar("Ana", 0, 0) is False
    assert fila.encolar("Ana", 4, 0) is False
    assert fila.tamaño() == 0


def test_un_elemento():
    """CA-05: un solo estudiante entra y sale."""
    fila = ColaPrioridad()
    assert fila.encolar("Ana", 2, 0) is True
    assert fila.tamaño() == 1
    assert fila.atender(0)["nombre"] == "Ana"
    assert fila.esta_vacia()
    # Se puede volver a usar después de quedar vacía.
    fila.encolar("Luis", 1, 1)
    assert fila.atender(1)["nombre"] == "Luis"


def test_envejecimiento():
    """CA-06: en el minuto 30, un nivel 3 que llegó en el 0 sale antes que un nivel 1 recién llegado."""
    # Ana: 3 - 30 // 10 = 0. Luis: 1 - 0 // 10 = 1.
    fila = ColaPrioridad()
    fila.encolar("Ana", 3, 0)
    fila.encolar("Luis", 1, 30)
    assert fila.atender(30)["nombre"] == "Ana"


def test_no_espera_para_siempre():
    """CA-07: si llega un nivel 1 cada minuto, un nivel 3 sale antes del minuto 30."""
    fila = ColaPrioridad()
    fila.encolar("Ana", 3, 0)
    minuto_de_ana = -1
    for minuto in range(100):
        fila.encolar("urgente", 1, minuto)
        atendido = fila.atender(minuto)
        if atendido["nombre"] == "Ana":
            minuto_de_ana = minuto
            break
    assert minuto_de_ana != -1
    assert minuto_de_ana <= 30
