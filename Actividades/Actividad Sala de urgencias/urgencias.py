from cola_prioridad import ColaPrioridad


class Urgencias:
    """Fila de urgencias ordenada por nivel de triage, del 1 al 5."""

    def __init__(self):
        self.cola = ColaPrioridad()
        self.turno = 0
        self.atendidos = 0

    def registrar(self, documento, nombre, edad, nivel, motivo):
        """O(n). Devuelve el paciente con su turno, o un error."""
        if nivel < 1 or nivel > 5:
            return {"error": "El nivel debe estar entre 1 y 5"}
        if self.cola.buscar_documento(documento) is not None:
            return {"error": "Ese documento ya está en espera"}
        self.turno = self.turno + 1
        paciente = {"turno": "U-" + str(self.turno), "documento": documento, "nombre": nombre,
                    "edad": edad, "nivel": nivel, "motivo": motivo}
        self.cola.encolar(paciente, nivel)
        return paciente

    def ver_fila(self):
        """O(n). La fila completa en orden de atención."""
        return self.cola.a_lista()

    def siguiente(self):
        """O(1). Muestra quién sigue sin sacarlo."""
        if self.cola.tamaño() == 0:
            return {"error": "No hay pacientes en espera"}
        return self.cola.frente()

    def atender(self):
        """O(1). Saca al siguiente para atenderlo."""
        if self.cola.tamaño() == 0:
            return {"error": "No hay pacientes en espera"}
        self.atendidos = self.atendidos + 1
        return self.cola.desencolar()

    def retirar(self, turno):
        """O(n). Saca de la fila al paciente con ese turno."""
        paciente = self.cola.retirar_turno(turno)
        if paciente is None:
            return {"error": "No hay un paciente en espera con ese turno"}
        return paciente

    def estado(self):
        """O(n). Cuántos faltan en total y por nivel."""
        por_nivel = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        for paciente in self.cola.a_lista():
            por_nivel[paciente["nivel"]] = por_nivel[paciente["nivel"]] + 1
        return {"total": self.cola.tamaño(), "por_nivel": por_nivel, "atendidos": self.atendidos}
