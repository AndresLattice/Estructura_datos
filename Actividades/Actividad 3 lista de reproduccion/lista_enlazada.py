from nodo import Nodo


class ListaEnlazada:
    # cabeza es el primer nodo, cola el ultimo y cantidad cuantos hay.
    # Si la lista esta vacia, cabeza y cola son None y cantidad es 0.

    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.cantidad = 0

    def tamaño(self):
        """O(1)."""
        return self.cantidad

    def nodo_en(self, posicion):
        """O(p). Camina desde la cabeza hasta el nodo de esa posicion."""
        actual = self.cabeza
        for i in range(posicion):
            actual = actual.siguiente
        return actual

    def obtener(self, posicion):
        """O(p). Devuelve None si la posicion no es valida."""
        if posicion < 0 or posicion >= self.cantidad:
            return None
        return self.nodo_en(posicion).dato

    def insertar(self, posicion, elemento):
        """O(1) al principio y al final, O(p) en el medio. Devuelve False si la posicion no es valida."""
        if posicion < 0 or posicion > self.cantidad:
            return False
        nuevo = Nodo(elemento)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            if posicion == 0:
                nuevo.siguiente = self.cabeza
                self.cabeza = nuevo
            else:
                if posicion == self.cantidad:
                    self.cola.siguiente = nuevo
                    self.cola = nuevo
                else:
                    # Primero el nuevo apunta al que sigue y despues
                    # el anterior apunta al nuevo, si no se pierde el resto
                    anterior = self.nodo_en(posicion - 1)
                    nuevo.siguiente = anterior.siguiente
                    anterior.siguiente = nuevo
        self.cantidad = self.cantidad + 1
        return True

    def eliminar(self, posicion):
        """O(1) el primero, O(p) los demas. Devuelve la cancion quitada, o None si la posicion no es valida."""
        if posicion < 0 or posicion >= self.cantidad:
            return None
        if posicion == 0:
            eliminado = self.cabeza
            self.cabeza = eliminado.siguiente
            if self.cabeza is None:
                self.cola = None
        else:
            anterior = self.nodo_en(posicion - 1)
            eliminado = anterior.siguiente
            anterior.siguiente = eliminado.siguiente
            if eliminado == self.cola:
                self.cola = anterior
        self.cantidad = self.cantidad - 1
        return eliminado.dato

    def buscar(self, elemento):
        """O(n). Devuelve la posicion de la primera aparicion, o -1."""
        actual = self.cabeza
        i = 0
        while actual is not None:
            if actual.dato == elemento:
                return i
            actual = actual.siguiente
            i = i + 1
        return -1

    def a_lista(self):
        """O(n). Devuelve las canciones en orden en una lista de Python."""
        resultado = []
        actual = self.cabeza
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado
