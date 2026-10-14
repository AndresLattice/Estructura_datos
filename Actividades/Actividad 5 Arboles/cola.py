from nodo import Nodo


class Cola:
    """Cola FIFO con nodos. Entra por cola, sale por cabeza."""

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

    def encolar(self, dato):
        """O(1). Pone el dato al final."""
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            self.cola.siguiente = nuevo
        self.cola = nuevo
        self.cantidad = self.cantidad + 1

    def desencolar(self):
        """O(1). Saca y devuelve el primero, o None si está vacía."""
        if self.cabeza is None:
            return None
        sale = self.cabeza
        self.cabeza = sale.siguiente
        if self.cabeza is None:
            self.cola = None
        self.cantidad = self.cantidad - 1
        return sale.dato
