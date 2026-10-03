from nodo import Nodo


class ColaPrioridad:
    """Sale primero el de menor prioridad. Con igual prioridad, el que llegó antes."""

    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.cantidad = 0

    def tamaño(self):
        """O(1)."""
        return self.cantidad

    def encolar(self, dato, prioridad):
        """O(1) si va de primero o de último, O(n) si va en el medio."""
        nuevo = Nodo(dato, prioridad)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
        elif prioridad < self.cabeza.prioridad:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
        elif prioridad >= self.cola.prioridad:
            self.cola.siguiente = nuevo
            self.cola = nuevo
        else:
            anterior = self.cabeza
            while anterior.siguiente.prioridad <= prioridad:
                anterior = anterior.siguiente
            nuevo.siguiente = anterior.siguiente
            anterior.siguiente = nuevo
        self.cantidad = self.cantidad + 1

    def frente(self):
        """O(1). Devuelve el primero sin sacarlo, o None si está vacía."""
        if self.cabeza is None:
            return None
        return self.cabeza.dato

    def desencolar(self):
        """O(1). Saca y devuelve el primero, o None si está vacía."""
        if self.cabeza is None:
            return None
        eliminado = self.cabeza
        self.cabeza = eliminado.siguiente
        if self.cabeza is None:
            self.cola = None
        self.cantidad = self.cantidad - 1
        return eliminado.dato

    def buscar_documento(self, documento):
        """O(n). Devuelve el paciente con ese documento, o None."""
        actual = self.cabeza
        while actual is not None:
            if actual.dato["documento"] == documento:
                return actual.dato
            actual = actual.siguiente
        return None

    def retirar_turno(self, turno):
        """O(n). Saca y devuelve el paciente con ese turno, o None."""
        if self.cabeza is None:
            return None
        if self.cabeza.dato["turno"] == turno:
            return self.desencolar()
        anterior = self.cabeza
        actual = self.cabeza.siguiente
        while actual is not None:
            if actual.dato["turno"] == turno:
                anterior.siguiente = actual.siguiente
                if actual == self.cola:
                    self.cola = anterior
                self.cantidad = self.cantidad - 1
                return actual.dato
            anterior = actual
            actual = actual.siguiente
        return None

    def a_lista(self):
        """O(n). Devuelve los datos en el orden en que van a salir."""
        resultado = []
        actual = self.cabeza
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado
