from nodo import Nodo

# Cada 10 minutos de espera la prioridad efectiva baja 1.
MINUTOS_POR_NIVEL = 10


class ColaPrioridad:
    """Sala de cómputo con tres niveles y envejecimiento.

    Nivel 1: entrega con plazo hoy.
    Nivel 2: actividades de clases.
    Nivel 3: uso libre.

    Envejecimiento: efectiva = nivel - minutos_esperando // 10.
    Sale la menor efectiva. Con empate, el que llegó antes.
    Así nadie espera para siempre: con el tiempo su efectiva baja
    hasta ganarle a cualquiera que acabe de llegar.
    """

    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.cantidad = 0

    def esta_vacia(self):
        """O(1)."""
        return self.cabeza is None

    def tamaño(self):
        """O(1)."""
        return self.cantidad

    def encolar(self, nombre, nivel, llegada):
        """O(1). Pone al estudiante al final. Devuelve False si el nivel no es 1, 2 o 3."""
        if nivel < 1 or nivel > 3:
            return False
        estudiante = {"nombre": nombre, "nivel": nivel, "llegada": llegada}
        nuevo = Nodo(estudiante)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            self.cola.siguiente = nuevo
        self.cola = nuevo
        self.cantidad = self.cantidad + 1
        return True

    def efectiva(self, estudiante, minuto):
        """O(1). Prioridad del estudiante en ese minuto."""
        espera = minuto - estudiante["llegada"]
        return estudiante["nivel"] - espera // MINUTOS_POR_NIVEL

    def atender(self, minuto):
        """O(n). Saca y devuelve al de menor efectiva, o None si está vacía."""
        if self.cabeza is None:
            return None

        # Buscar el mejor y el nodo anterior a él.
        # Solo se cambia si es estrictamente menor: el empate lo gana quien llegó antes.
        mejor = self.cabeza
        anterior_mejor = None
        anterior = self.cabeza
        actual = self.cabeza.siguiente
        while actual is not None:
            if self.efectiva(actual.dato, minuto) < self.efectiva(mejor.dato, minuto):
                mejor = actual
                anterior_mejor = anterior
            anterior = actual
            actual = actual.siguiente

        # Sacar el nodo mejor de la lista.
        if anterior_mejor is None:
            self.cabeza = mejor.siguiente
        else:
            anterior_mejor.siguiente = mejor.siguiente
        if mejor == self.cola:
            self.cola = anterior_mejor
        self.cantidad = self.cantidad - 1
        return mejor.dato
