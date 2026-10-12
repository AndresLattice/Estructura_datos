# Código base — Semana 07
# Fuente: 02-Momento-2-Disciplina-y-jerarquia/07-Semana-07-Listas-dobles-y-circulares/02-guia-de-laboratorio.html

from nodo import Nodo


class ListaCircular:
    """Lista circular simple: el último nodo apunta al primero.

    Guarda una referencia al nodo ACTUAL, no a la cabeza: en una lista
    circular no hay un «primero» natural.

    Invariantes de representación:
        IR-01: lista vacía  <=>  _actual is None
        IR-02: si tiene un solo nodo, ese nodo apunta a sí mismo
        IR-03: recorrer siempre vuelve al punto de partida en _tamaño pasos
    """

    def __init__(self):
        self._actual = None
        self._tamaño = 0

    def esta_vacia(self):
        return self._actual is None

    def agregar(self, dato):
        """Inserta después del actual. O(1)."""
        nuevo = Nodo(dato)
        if self._actual is None:
            nuevo.siguiente = nuevo          # apunta a sí mismo
            self._actual = nuevo
        else:
            nuevo.siguiente = self._actual.siguiente
            self._actual.siguiente = nuevo
        self._tamaño += 1
        return nuevo

    def avanzar(self):
        """Pasa el turno al siguiente. O(1). Devuelve el dato del nuevo actual."""
        if self._actual is None:
            raise IndexError("lista circular vacía")
        self._actual = self._actual.siguiente
        return self._actual.dato

    def actual(self):
        if self._actual is None:
            raise IndexError("lista circular vacía")
        return self._actual.dato

    def eliminar_actual(self):
        """Elimina el nodo actual y avanza. O(n) porque hay que llegar al anterior.

        CUIDADO con el caso de un solo nodo: hay que dejar _actual en None.
        """
        if self._actual is None:
            raise IndexError("lista circular vacía")
        dato = self._actual.dato
        if self._tamaño == 1:
            self._actual = None
            self._tamaño = 0
            return dato
        # buscar el nodo anterior al actual
        anterior = self._actual
        while anterior.siguiente is not self._actual:
            anterior = anterior.siguiente
        anterior.siguiente = self._actual.siguiente
        self._actual = anterior.siguiente
        self._tamaño -= 1
        return dato

    def rotar(self, k):
        """Avanza k posiciones. O(k)."""
        for _ in range(k):
            self.avanzar()

    def __len__(self):
        return self._tamaño

    def __iter__(self):
        """Recorre exactamente _tamaño elementos y se detiene.

        Sin el contador, esto sería un ciclo infinito.
        """
        if self._actual is None:
            return
        nodo = self._actual
        for _ in range(self._tamaño):
            yield nodo.dato
            nodo = nodo.siguiente
