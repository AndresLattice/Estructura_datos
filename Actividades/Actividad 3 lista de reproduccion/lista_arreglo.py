class ListaArreglo:
    # Las canciones se guardan una junto a otra en "datos", que tiene
    # "capacidad" espacios. Solo los primeros "cantidad" estan ocupados.

    def __init__(self):
        self.capacidad = 4
        self.datos = []
        for i in range(self.capacidad):
            self.datos.append(None)
        self.cantidad = 0

    def tamaño(self):
        """O(1)."""
        return self.cantidad

    def obtener(self, posicion):
        """O(1). Devuelve None si la posicion no es valida."""
        if posicion < 0 or posicion >= self.cantidad:
            return None
        return self.datos[posicion]

    def insertar(self, posicion, elemento):
        """O(n) al principio, O(1) al final. Devuelve False si la posicion no es valida."""
        if posicion < 0 or posicion > self.cantidad:
            return False
        if self.cantidad == self.capacidad:
            self.agrandar()
        # Muevo cada cancion un lugar a la derecha, empezando por la ultima,
        # para dejar libre "posicion"
        i = self.cantidad
        while i > posicion:
            self.datos[i] = self.datos[i - 1]
            i = i - 1
        self.datos[posicion] = elemento
        self.cantidad = self.cantidad + 1
        return True

    def eliminar(self, posicion):
        """O(n). Devuelve la cancion quitada, o None si la posicion no es valida."""
        if posicion < 0 or posicion >= self.cantidad:
            return None
        eliminado = self.datos[posicion]
        # Muevo cada cancion un lugar a la izquierda para tapar el hueco
        i = posicion
        while i < self.cantidad - 1:
            self.datos[i] = self.datos[i + 1]
            i = i + 1
        self.cantidad = self.cantidad - 1
        self.datos[self.cantidad] = None
        return eliminado

    def buscar(self, elemento):
        """O(n). Devuelve la posicion de la primera aparicion, o -1."""
        for i in range(self.cantidad):
            if self.datos[i] == elemento:
                return i
        return -1

    def a_lista(self):
        """O(n). Devuelve las canciones en orden en una lista de Python."""
        resultado = []
        for i in range(self.cantidad):
            resultado.append(self.datos[i])
        return resultado

    def agrandar(self):
        """O(n). Pasa todo a un espacio con el doble de capacidad."""
        nueva_capacidad = self.capacidad * 2
        nuevos_datos = []
        for i in range(nueva_capacidad):
            nuevos_datos.append(None)
        for i in range(self.cantidad):
            nuevos_datos[i] = self.datos[i]
        self.datos = nuevos_datos
        self.capacidad = nueva_capacidad
