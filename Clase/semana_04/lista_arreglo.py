# Código base — Semana 04
# Fuente: 01-Momento-1-Contrato-y-secuencia/04-Semana-04-Arreglos-y-estructuras-estaticas/02-guia-de-laboratorio.html

from array import array


class PosicionInvalidaError(IndexError):
    """La posición solicitada está fuera del rango válido."""


class ListaArreglo:
    """Lista implementada sobre un arreglo de tamaño fijo con redimensionamiento.

    Atributos internos:
        _datos      arreglo subyacente (capacidad fija en cada momento)
        _capacidad  cuántas posiciones tiene el arreglo
        _tamaño     cuántas posiciones están realmente ocupadas

    Invariante de representación: 0 <= _tamaño <= _capacidad

    Complejidad:
        obtener          -> O(1)
        insertar(final)  -> O(1) amortizado
        insertar(inicio) -> O(n)
        eliminar         -> O(n)
        buscar           -> O(n)
    """

    CAPACIDAD_INICIAL = 4

    def __init__(self):
        self._capacidad = self.CAPACIDAD_INICIAL
        self._datos = [None] * self._capacidad
        self._tamaño = 0

    # ---------- operaciones públicas ----------

    def tamaño(self):
        return self._tamaño

    def obtener(self, posicion):
        """Devuelve el elemento en `posicion`. O(1)."""
        self._validar(posicion, incluir_final=False)
        return self._datos[posicion]

    def insertar(self, posicion, elemento):
        """Inserta desplazando los elementos siguientes hacia la derecha."""
        self._validar(posicion, incluir_final=True)
        if self._tamaño == self._capacidad:
            self._redimensionar(self._capacidad * 2)
        # Desplaza desde el FINAL hacia atrás. ¿Por qué desde el final?
        # Si lo haces desde el principio, sobrescribes los datos.
        # i - 1 = "copia lo que hay en el vecino de la izquierda"
        for i in range(self._tamaño, posicion, -1):
            self._datos[i] = self._datos[i - 1]
        self._datos[posicion] = elemento  # deja el hueco listo en `posicion`
        self._tamaño += 1

    def eliminar(self, posicion):
        """Elimina y devuelve el elemento, desplazando los siguientes."""
        self._validar(posicion, incluir_final=False)
        elemento = self._datos[posicion]
        # i + 1 = "copia lo que hay en el vecino de la derecha" (tapa el hueco)
        for i in range(posicion, self._tamaño - 1):
            self._datos[i] = self._datos[i + 1]
        self._tamaño -= 1
        self._datos[self._tamaño] = None  # limpia el casillero que sobró
        return elemento

    def buscar(self, elemento):
        """Devuelve la posición de la primera aparición, o -1."""
        for i in range(self._tamaño):  # recorre índices 0 .. tamaño-1
            if self._datos[i] == elemento:
                return i
        return -1  # -1 = "no encontrado" (nunca es un índice real)

    # ---------- auxiliares ----------

    def _validar(self, posicion, incluir_final):
        limite = self._tamaño if incluir_final else self._tamaño - 1
        if not 0 <= posicion <= limite:
            raise PosicionInvalidaError(
                f"posicion {posicion} fuera de rango [0, {limite}]"
            )

    def _redimensionar(self, nueva_capacidad):
        """Crea un arreglo mayor y copia los elementos. O(n)."""
        nuevos_datos = [None] * nueva_capacidad
        for i in range(self._tamaño):
            nuevos_datos[i] = self._datos[i]
        self._datos = nuevos_datos
        self._capacidad = nueva_capacidad

    # ---------- protocolo de Python ----------

    def __len__(self):
        return self._tamaño

    def __getitem__(self, i):
        return self.obtener(i)

    def __iter__(self):
        for i in range(self._tamaño):
            yield self._datos[i]

    def __repr__(self):
        return f"ListaArreglo({list(self)!r})"
