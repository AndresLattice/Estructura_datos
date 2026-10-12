# Código base — Semana 07
# Fuente: 02-Momento-2-Disciplina-y-jerarquia/07-Semana-07-Listas-dobles-y-circulares/02-guia-de-laboratorio.html

from nodo_doble import NodoDoble


class PosicionInvalidaError(IndexError):
    """La posición solicitada está fuera del rango válido."""


class ListaDoble:
    """Lista doblemente enlazada con nodo centinela.

    Invariantes de representación:
        IR-01: _centinela nunca contiene datos válidos
        IR-02: para todo nodo n:  n.siguiente.anterior is n
        IR-03: lista vacía  <=>  _centinela.siguiente is _centinela
        IR-04: _tamaño no cuenta el centinela

    Complejidad:
        insertar(0)          -> O(1)
        insertar(tamaño)     -> O(1)   ¡sin necesidad de referencia a la cola!
        insertar(i)          -> O(n)   por el recorrido, no por el reenlazado
        eliminar_nodo(nodo)  -> O(1)   si ya tienes la referencia
        obtener(i)           -> O(n)   pero puede recorrer desde el extremo más cercano
    """

    def __init__(self):
        self._centinela = NodoDoble(None)
        self._centinela.siguiente = self._centinela
        self._centinela.anterior = self._centinela
        self._tamaño = 0

    def tamaño(self):
        return self._tamaño

    def esta_vacia(self):
        return self._centinela.siguiente is self._centinela

    # ---------- inserción ----------

    def _insertar_entre(self, dato, anterior, siguiente):
        """Inserta un nodo nuevo entre dos nodos existentes. O(1).

        Este es el ÚNICO método que reenlaza. Todos los demás lo llaman.
        Orden de las cuatro asignaciones: primero los enlaces del nuevo
        (que no rompen nada), después los de los vecinos.
        """
        nuevo = NodoDoble(dato, anterior, siguiente)
        anterior.siguiente = nuevo
        siguiente.anterior = nuevo
        self._tamaño += 1
        return nuevo

    def insertar_al_inicio(self, dato):
        return self._insertar_entre(dato, self._centinela, self._centinela.siguiente)

    def insertar_al_final(self, dato):
        return self._insertar_entre(dato, self._centinela.anterior, self._centinela)

    def insertar(self, posicion, dato):
        self._validar(posicion, incluir_final=True)
        siguiente = self._nodo_en(posicion) if posicion < self._tamaño else self._centinela
        return self._insertar_entre(dato, siguiente.anterior, siguiente)

    # ---------- eliminación ----------

    def eliminar_nodo(self, nodo):
        """Elimina un nodo dado su referencia. O(1).

        Esta es LA ventaja de la lista doble: en la lista simple
        necesitarías recorrer para encontrar el nodo anterior.
        """
        if nodo is self._centinela:
            raise ValueError("no se puede eliminar el centinela")
        nodo.anterior.siguiente = nodo.siguiente
        nodo.siguiente.anterior = nodo.anterior
        self._tamaño -= 1
        return nodo.dato

    def eliminar(self, posicion):
        self._validar(posicion, incluir_final=False)
        return self.eliminar_nodo(self._nodo_en(posicion))

    # ---------- acceso ----------

    def _nodo_en(self, posicion):
        """Recorre desde el extremo MÁS CERCANO. Sigue siendo O(n),
        pero en la práctica hace la mitad de los pasos."""
        if posicion <= self._tamaño // 2:
            actual = self._centinela.siguiente
            for _ in range(posicion):
                actual = actual.siguiente
        else:
            actual = self._centinela.anterior
            for _ in range(self._tamaño - posicion - 1):
                actual = actual.anterior
        return actual

    def obtener(self, posicion):
        self._validar(posicion, incluir_final=False)
        return self._nodo_en(posicion).dato

    def _validar(self, posicion, incluir_final):
        limite = self._tamaño if incluir_final else self._tamaño - 1
        if not 0 <= posicion <= limite:
            raise PosicionInvalidaError(f"posicion {posicion} fuera de [0, {limite}]")

    # ---------- protocolo ----------

    def __len__(self):
        return self._tamaño

    def __iter__(self):
        actual = self._centinela.siguiente
        while actual is not self._centinela:
            yield actual.dato
            actual = actual.siguiente

    def __reversed__(self):
        """Recorrido hacia atrás: imposible en una lista simple."""
        actual = self._centinela.anterior
        while actual is not self._centinela:
            yield actual.dato
            actual = actual.anterior

    def __repr__(self):
        return f"ListaDoble({list(self)!r})"
