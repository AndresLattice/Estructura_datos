class Carrito:
    def __init__(self):
        self._items = []

    def _indice_de(self, producto):
        # Recorre la lista buscando el producto. `for i, (p, _) in enumerate(...)`
        # desempaqueta cada par [producto, cantidad]: i es la posicion, p el nombre,
        # _ la cantidad (que aqui no se usa). Este recorrido es lo que vuelve
        # O(n) a agregar, quitar y cantidad_de. Devuelve -1 si no lo encuentra.
        for i, (p, _) in enumerate(self._items):
            if p == producto:
                return i
        return -1

    def agregar(self, producto, cantidad):
        # bool es subclase de int en Python, asi True/False pasarian como enteros:
        # se excluyen a proposito para que agregar(prod, True) no cuente como 1.
        if not isinstance(cantidad, int) or isinstance(cantidad, bool):
            raise ValueError("cantidad debe ser un entero")
        if cantidad <= 0:
            raise ValueError("cantidad debe ser mayor que 0")

        i = self._indice_de(producto)
        if i == -1:
            self._items.append([producto, cantidad])
        else:
            # self._items[i] es el par [producto, cantidad]; [1] es la cantidad.
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
            # Al llegar a 0 se borra el par entero: el producto no queda "en 0",
            # sale del carrito (asi esta_vacio y total no lo cuentan).
            del self._items[i]
        else:
            self._items[i][1] = nueva_cantidad

    def cantidad_de(self, producto):
        i = self._indice_de(producto)
        if i == -1:
            return 0
        return self._items[i][1]

    def total(self):
        # Generador: por cada par [producto, cantidad] toma solo la cantidad
        # (ignora el nombre con _) y las suma todas.
        return sum(cantidad for _, cantidad in self._items)

    def esta_vacio(self):
        return len(self._items) == 0
