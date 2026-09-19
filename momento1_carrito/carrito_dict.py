class Carrito:
    def __init__(self):
        self._cantidades = {}

    def agregar(self, producto, cantidad):
        # bool es subclase de int en Python, asi True/False pasarian como enteros:
        # se excluyen a proposito para que agregar(prod, True) no cuente como 1.
        if not isinstance(cantidad, int) or isinstance(cantidad, bool):
            raise ValueError("cantidad debe ser un entero")
        if cantidad <= 0:
            raise ValueError("cantidad debe ser mayor que 0")

        # .get(producto, 0) devuelve la cantidad actual o 0 si el producto no existe.
        # Con eso, "producto nuevo" y "acumular sobre lo que ya habia" se resuelven
        # en una sola linea, sin un if para cada caso.
        self._cantidades[producto] = self._cantidades.get(producto, 0) + cantidad

    def quitar(self, producto, cantidad):
        if not isinstance(cantidad, int) or isinstance(cantidad, bool):
            raise ValueError("cantidad debe ser un entero")
        if cantidad <= 0:
            raise ValueError("cantidad debe ser mayor que 0")

        if producto not in self._cantidades:
            raise ValueError(f"'{producto}' no esta en el carrito")

        disponible = self._cantidades[producto]
        if cantidad > disponible:
            raise ValueError(
                f"no hay suficiente '{producto}' en el carrito "
                f"(disponible: {disponible}, pedido: {cantidad})"
            )

        nueva_cantidad = disponible - cantidad
        if nueva_cantidad == 0:
            # Al llegar a 0 se borra la clave: el producto no queda "en 0",
            # sale del carrito (asi esta_vacio y total no lo cuentan).
            del self._cantidades[producto]
        else:
            self._cantidades[producto] = nueva_cantidad

    def cantidad_de(self, producto):
        return self._cantidades.get(producto, 0)

    def total(self):
        return sum(self._cantidades.values())

    def esta_vacio(self):
        return len(self._cantidades) == 0
