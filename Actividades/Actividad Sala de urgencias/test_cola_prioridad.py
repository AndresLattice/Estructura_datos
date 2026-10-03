from cola_prioridad import ColaPrioridad


def test_cola_nueva_vacia():
    """CA-01: una cola nueva está vacía."""
    fila = ColaPrioridad()
    assert fila.tamaño() == 0
    assert fila.cabeza is None
    assert fila.cola is None


def test_orden_por_prioridad():
    """CA-02: sale primero el de menor prioridad. Prueba del laboratorio."""
    fila = ColaPrioridad()
    fila.encolar("urgente", 1)
    fila.encolar("normal", 5)
    fila.encolar("critico", 0)
    assert fila.desencolar() == "critico"
    assert fila.desencolar() == "urgente"
    assert fila.desencolar() == "normal"


def test_empate_es_fifo():
    """CA-03: con igual prioridad sale el que llegó antes. Prueba del laboratorio."""
    fila = ColaPrioridad()
    fila.encolar("primero", 3)
    fila.encolar("segundo", 3)
    assert fila.desencolar() == "primero"
    assert fila.desencolar() == "segundo"


def test_vacia_devuelve_none():
    """CA-04: en una cola vacía, frente y desencolar devuelven None."""
    fila = ColaPrioridad()
    assert fila.frente() is None
    assert fila.desencolar() is None
    assert fila.tamaño() == 0


def test_frente_no_modifica():
    """CA-05: frente devuelve el más urgente sin sacarlo."""
    fila = ColaPrioridad()
    fila.encolar("b", 2)
    fila.encolar("a", 1)
    assert fila.frente() == "a"
    assert fila.tamaño() == 2


def test_un_elemento_entra_y_sale():
    """CA-06: con un elemento, cabeza y cola son el mismo y al salir quedan en None."""
    fila = ColaPrioridad()
    fila.encolar("unico", 3)
    assert fila.cabeza is fila.cola
    assert fila.desencolar() == "unico"
    assert fila.cabeza is None
    assert fila.cola is None


def test_mas_urgente_pasa_a_cabeza():
    """CA-07: el más urgente de todos queda en la cabeza."""
    fila = ColaPrioridad()
    fila.encolar("p3", 3)
    fila.encolar("p4", 4)
    fila.encolar("p1", 1)
    assert fila.cabeza.dato == "p1"
    assert fila.a_lista() == ["p1", "p3", "p4"]


def test_menos_urgente_actualiza_cola():
    """CA-08: igual o menos urgente que el último queda de último y actualiza cola."""
    fila = ColaPrioridad()
    fila.encolar("a", 2)
    fila.encolar("b", 5)
    fila.encolar("c", 5)
    assert fila.cola.dato == "c"
    assert fila.cola.siguiente is None


def test_retirar_cabeza():
    """CA-09: retirar la cabeza deja como cabeza al siguiente."""
    fila = ColaPrioridad()
    fila.encolar({"turno": "a"}, 1)
    fila.encolar({"turno": "b"}, 2)
    fila.encolar({"turno": "c"}, 3)
    assert fila.retirar_turno("a") == {"turno": "a"}
    assert fila.cabeza.dato == {"turno": "b"}
    assert fila.tamaño() == 2


def test_retirar_ultimo_actualiza_cola():
    """CA-10: retirar el último hace retroceder la cola."""
    fila = ColaPrioridad()
    fila.encolar({"turno": "a"}, 1)
    fila.encolar({"turno": "b"}, 2)
    fila.encolar({"turno": "c"}, 3)
    assert fila.retirar_turno("c") == {"turno": "c"}
    assert fila.cola.dato == {"turno": "b"}
    assert fila.cola.siguiente is None
    assert fila.tamaño() == 2


def test_retirar_del_medio_conserva_orden():
    """CA-11: retirar uno del medio no cambia el orden de los demás."""
    fila = ColaPrioridad()
    fila.encolar({"turno": "a"}, 1)
    fila.encolar({"turno": "b"}, 2)
    fila.encolar({"turno": "c"}, 3)
    fila.retirar_turno("b")
    assert fila.a_lista() == [{"turno": "a"}, {"turno": "c"}]


def test_retirar_inexistente_devuelve_none():
    """CA-12: retirar algo que no está devuelve None y no cambia la cola."""
    fila = ColaPrioridad()
    assert fila.retirar_turno("z") is None
    fila.encolar({"turno": "a"}, 1)
    assert fila.retirar_turno("z") is None
    assert fila.tamaño() == 1


def test_buscar_documento():
    """CA-13: buscar devuelve el paciente sin sacarlo, o None si no está."""
    fila = ColaPrioridad()
    fila.encolar({"documento": "1001"}, 1)
    assert fila.buscar_documento("1001") == {"documento": "1001"}
    assert fila.buscar_documento("9999") is None
    assert fila.tamaño() == 1


def test_operaciones_mezcladas():
    """CA-14: tras varias operaciones la cola sigue en orden y consistente."""
    fila = ColaPrioridad()
    fila.encolar({"turno": "a"}, 3)
    fila.encolar({"turno": "b"}, 1)
    fila.encolar({"turno": "c"}, 4)
    fila.encolar({"turno": "d"}, 1)
    fila.encolar({"turno": "e"}, 2)
    fila.retirar_turno("c")
    fila.desencolar()
    assert fila.a_lista() == [{"turno": "d"}, {"turno": "e"}, {"turno": "a"}]
    assert fila.tamaño() == 3
    assert fila.cola.dato == {"turno": "a"}
    assert fila.cola.siguiente is None
