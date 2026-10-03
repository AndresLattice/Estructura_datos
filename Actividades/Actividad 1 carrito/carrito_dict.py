class Carrito:
    def __init__(self):
        # La clave es el producto y el valor es su cantidad
        self._cantidades = {}

    def agregar(self, producto, cantidad):
        if cantidad <= 0:
            return False
        if producto in self._cantidades:
            self._cantidades[producto] = self._cantidades[producto] + cantidad
        else:
            self._cantidades[producto] = cantidad
        return True

    def quitar(self, producto, cantidad):
        if cantidad <= 0:
            return False
        if producto not in self._cantidades:
            return False
        if cantidad > self._cantidades[producto]:
            return False
        self._cantidades[producto] = self._cantidades[producto] - cantidad
        if self._cantidades[producto] == 0:
            # Si llega a 0 el producto sale del carrito:
            # se arma un diccionario nuevo sin esa clave
            nuevo = {}
            for p in self._cantidades:
                if p != producto:
                    nuevo[p] = self._cantidades[p]
            self._cantidades = nuevo
        return True

    def cantidad_de(self, producto):
        if producto in self._cantidades:
            return self._cantidades[producto]
        return 0

    def total(self):
        total = 0
        for producto in self._cantidades:
            total = total + self._cantidades[producto]
        return total

    def esta_vacio(self):
        return len(self._cantidades) == 0
