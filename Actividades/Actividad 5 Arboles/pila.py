from nodo import Nodo


class Pila:
    """Pila con nodos. Entra y sale por tope."""

    def __init__(self):
        self.tope = None
        self.cantidad = 0

    def esta_vacia(self):
        """O(1)."""
        return self.tope is None

    def tamaño(self):
        """O(1)."""
        return self.cantidad

    def apilar(self, dato):
        """O(1). Pone el dato encima."""
        nuevo = Nodo(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo
        self.cantidad = self.cantidad + 1

    def desapilar(self):
        """O(1). Saca y devuelve el de encima, o None si está vacía."""
        if self.tope is None:
            return None
        sale = self.tope
        self.tope = sale.siguiente
        self.cantidad = self.cantidad - 1
        return sale.dato
