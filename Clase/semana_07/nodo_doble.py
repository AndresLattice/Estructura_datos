# Código base — Semana 07
# Fuente: 02-Momento-2-Disciplina-y-jerarquia/07-Semana-07-Listas-dobles-y-circulares/02-guia-de-laboratorio.html

class NodoDoble:
    """Un eslabón con enlaces en ambos sentidos."""

    def __init__(self, dato, anterior=None, siguiente=None):
        self.dato = dato
        self.anterior = anterior
        self.siguiente = siguiente

    def __repr__(self):
        return f"NodoDoble({self.dato!r})"
