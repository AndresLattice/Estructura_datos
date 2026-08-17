class Carrito:
    def __init__(self):
        self._items = []

    def _indice_de(self, producto):
        for i, (p, _) in enumerate(self._items):
            if p == producto:
                return i
        return -1

    def agregar(self, producto, cantidad):
        if not isinstance(cantidad, int) or isinstance(cantidad, bool):
            raise ValueError("cantidad debe ser un entero")
        if cantidad <= 0:
            raise ValueError("cantidad debe ser mayor que 0")

        i = self._indice_de(producto)
        if i == -1:
            self._items.append([producto, cantidad])
        else:
            self._items[i][1] += cantidad

    def quitar(self, producto, cantidad):
        if not isinstance(cantidad, int) or isinstance(cantidad, bool):
            raise ValueError("cantidad debe ser un entero")
        if cantidad <= 0:
            raise ValueError("cantidad debe ser mayor que 0")

        i = self._indice_de(producto)
        if i == -1:
            raise ValueError(f"'{producto}' no esta en el carrito")

        disponible = self._items[i][1]
        if cantidad > disponible:
            raise ValueError(
                f"no hay suficiente '{producto}' en el carrito "
                f"(disponible: {disponible}, pedido: {cantidad})"
            )

        nueva_cantidad = disponible - cantidad
        if nueva_cantidad == 0:
            del self._items[i]
        else:
            self._items[i][1] = nueva_cantidad

    def cantidad_de(self, producto):
        i = self._indice_de(producto)
        if i == -1:
            return 0
        return self._items[i][1]

    def total(self):
        return sum(cantidad for _, cantidad in self._items)

    def esta_vacio(self):
        return len(self._items) == 0
