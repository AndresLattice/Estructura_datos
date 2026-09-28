class Carrito:
    def __init__(self):
        # Cada elemento es un par [producto, cantidad]
        self._items = []

    def buscar(self, producto):
        # Devuelve la posicion del producto, o -1 si no esta
        for i in range(len(self._items)):
            if self._items[i][0] == producto:
                return i
        return -1

    def agregar(self, producto, cantidad):
        if cantidad <= 0:
            return False
        i = self.buscar(producto)
        if i == -1:
            self._items.append([producto, cantidad])
        else:
            self._items[i][1] = self._items[i][1] + cantidad
        return True

    def quitar(self, producto, cantidad):
        if cantidad <= 0:
            return False
        i = self.buscar(producto)
        if i == -1:
            return False
        if cantidad > self._items[i][1]:
            return False
        self._items[i][1] = self._items[i][1] - cantidad
        if self._items[i][1] == 0:
            # Si llega a 0 el producto sale del carrito:
            # se arma una lista nueva sin ese par
            nueva_lista = []
            for item in self._items:
                if item[0] != producto:
                    nueva_lista.append(item)
            self._items = nueva_lista
        return True

    def cantidad_de(self, producto):
        i = self.buscar(producto)
        if i == -1:
            return 0
        return self._items[i][1]

    def total(self):
        total = 0
        for item in self._items:
            total = total + item[1]
        return total

    def esta_vacio(self):
        return len(self._items) == 0
