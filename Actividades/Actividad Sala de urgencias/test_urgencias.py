from urgencias import Urgencias


def registrar(u, documento, nivel):
    """Registra un paciente con datos de prueba."""
    return u.registrar(documento, "Paciente de prueba", 30, nivel, "Dolor abdominal")


def documentos_en_fila(u):
    """Devuelve los documentos en el orden de la fila."""
    documentos = []
    for paciente in u.ver_fila():
        documentos.append(paciente["documento"])
    return documentos


def test_registrar_paciente():
    """CA-15: un registro válido devuelve el paciente con su turno."""
    u = Urgencias()
    paciente = registrar(u, "1001", 2)
    assert paciente["turno"] == "U-1"
    assert paciente["nivel"] == 2


def test_registrar_nivel_invalido():
    """CA-16: un nivel fuera de 1 a 5 devuelve error y la fila no cambia."""
    u = Urgencias()
    assert "error" in registrar(u, "1001", 0)
    assert "error" in registrar(u, "1001", 6)
    assert u.estado()["total"] == 0


def test_registrar_documento_duplicado():
    """CA-17: un documento que ya está esperando devuelve error y no se duplica."""
    u = Urgencias()
    registrar(u, "1001", 3)
    assert "error" in registrar(u, "1001", 1)
    assert u.estado()["total"] == 1


def test_documento_puede_volver_tras_atencion():
    """CA-18: después de atendido, el mismo documento puede registrarse otra vez."""
    u = Urgencias()
    registrar(u, "1001", 3)
    u.atender()
    assert registrar(u, "1001", 4)["turno"] == "U-2"


def test_siguiente_no_modifica():
    """CA-19: consultar el siguiente devuelve el más urgente y no lo saca."""
    u = Urgencias()
    registrar(u, "1001", 4)
    registrar(u, "1002", 2)
    assert u.siguiente()["documento"] == "1002"
    assert u.estado()["total"] == 2


def test_siguiente_cola_vacia():
    """CA-20: consultar el siguiente con la fila vacía devuelve error."""
    u = Urgencias()
    assert u.siguiente() == {"error": "No hay pacientes en espera"}


def test_atender_respeta_prioridad_y_llegada():
    """CA-21: atender saca primero al más grave y, en empate, al que llegó antes."""
    u = Urgencias()
    registrar(u, "A", 3)
    registrar(u, "B", 1)
    registrar(u, "C", 3)
    registrar(u, "D", 2)
    registrar(u, "E", 1)
    orden = []
    for i in range(5):
        orden.append(u.atender()["documento"])
    assert orden == ["B", "E", "D", "A", "C"]
    assert u.estado()["atendidos"] == 5


def test_atender_cola_vacia():
    """CA-22: atender con la fila vacía devuelve error y no cuenta un atendido."""
    u = Urgencias()
    assert u.atender() == {"error": "No hay pacientes en espera"}
    assert u.estado()["atendidos"] == 0


def test_retirar_paciente():
    """CA-23: retirar por turno lo saca y conserva el orden de los demás."""
    u = Urgencias()
    registrar(u, "1001", 1)
    registrar(u, "1002", 2)
    registrar(u, "1003", 3)
    assert u.retirar("U-2")["documento"] == "1002"
    assert documentos_en_fila(u) == ["1001", "1003"]


def test_retirar_inexistente():
    """CA-24: retirar un turno que no está devuelve error y la fila no cambia."""
    u = Urgencias()
    registrar(u, "1001", 3)
    assert "error" in u.retirar("U-99")
    assert u.estado()["total"] == 1


def test_estado_conteo():
    """CA-25: el estado muestra el total y los cinco niveles, incluso los que están en 0."""
    u = Urgencias()
    registrar(u, "1", 1)
    registrar(u, "2", 3)
    registrar(u, "3", 3)
    registrar(u, "4", 5)
    estado = u.estado()
    assert estado["total"] == 4
    assert estado["por_nivel"] == {1: 1, 2: 0, 3: 2, 4: 0, 5: 1}


def test_fila_en_orden():
    """CA-26: la fila completa sale en el orden en que serán atendidos."""
    u = Urgencias()
    registrar(u, "1", 5)
    registrar(u, "2", 2)
    registrar(u, "3", 2)
    registrar(u, "4", 1)
    assert documentos_en_fila(u) == ["4", "2", "3", "1"]
