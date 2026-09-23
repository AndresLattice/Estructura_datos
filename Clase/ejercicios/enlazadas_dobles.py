from nodo import Nodo
class Lista_Doblemente_Enlazada:

    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.ultimo_eliminado = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            return
        nuevo_nodo.anterior = self.cola
        self.cola.siguiente = nuevo_nodo
        self.cola = nuevo_nodo

    def eliminar(self, valor):
        if self.cabeza is None:
            return False
        actual = self.cabeza
        while actual is not None and actual.valor != valor:
            actual = actual.siguiente
        if actual is None:
            return False
        if actual == self.cabeza and actual == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            if actual == self.cabeza:
                self.cabeza = actual.siguiente
                self.cabeza.anterior = None
            else:
                if actual == self.cola:
                    self.cola = actual.anterior
                    self.cola.siguiente = None
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
        self.ultimo_eliminado = actual
        return True

    def deshacer(self):
        if self.ultimo_eliminado is None:
            return False
        nodo = self.ultimo_eliminado
        if nodo.anterior is None and nodo.siguiente is None:
            self.cabeza = nodo
            self.cola = nodo
        else:
            if nodo.anterior is None:
                nodo.siguiente.anterior = nodo
                self.cabeza = nodo
            else:
                if nodo.siguiente is None:
                    nodo.anterior.siguiente = nodo
                    self.cola = nodo
                else:
                    nodo.anterior.siguiente = nodo
                    nodo.siguiente.anterior = nodo
        self.ultimo_eliminado = None
        return True
