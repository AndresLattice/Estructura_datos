class ListaArreglo:
    def __init__(self):
        self._capacidad = 4
        self._datos = [None] * self._capacidad
        self._tamano = 0

    def tamano(self):
        return self._tamano

    def _crecer(self):
        nueva_capacidad = self._capacidad * 2
        nuevos_datos = [None] * nueva_capacidad
        for i in range(self._tamano):
            nuevos_datos[i] = self._datos[i]
        self._datos = nuevos_datos
        self._capacidad = nueva_capacidad

    def insertar(self, pos, x):
        if pos < 0 or pos > self._tamano:
            raise ValueError("posicion fuera de rango")
        if self._tamano == self._capacidad:
            self._crecer()
        for i in range(self._tamano, pos, -1):
            self._datos[i] = self._datos[i - 1]
        self._datos[pos] = x
        self._tamano += 1

    def insertar_ordenado(self, x):
        pos = 0
        while pos < self._tamano and self._datos[pos] <= x:
            pos += 1
        self.insertar(pos, x)

    def obtener(self, pos):
        if pos < 0 or pos >= self._tamano:
            raise ValueError("posicion fuera de rango")
        return self._datos[pos]

    def buscar_lineal(self, x):
        for i in range(self._tamano):
            if self._datos[i] == x:
                return i
        return -1

    def buscar_binaria(self, x):
        inicio, fin = 0, self._tamano - 1
        while inicio <= fin:
            medio = (inicio + fin) // 2
            if self._datos[medio] == x:
                return medio
            if self._datos[medio] < x:
                inicio = medio + 1
            else:
                fin = medio - 1
        return -1
