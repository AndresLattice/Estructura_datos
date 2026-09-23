import tkinter as tk
from nodo import Nodo


class ListaCircular:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.actual = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            self.actual = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.cola.siguiente = self.cabeza
        self.cabeza.anterior = self.cola


ventana = tk.Tk()
lista = ListaCircular()

lista.agregar(tk.PhotoImage(file="imagenes/01_evaporacion.png"))
lista.agregar(tk.PhotoImage(file="imagenes/02_condensacion.png"))
lista.agregar(tk.PhotoImage(file="imagenes/03_precipitacion.png"))
lista.agregar(tk.PhotoImage(file="imagenes/04_escorrentia.png"))
lista.agregar(tk.PhotoImage(file="imagenes/05_infiltracion.png"))
lista.agregar(tk.PhotoImage(file="imagenes/06_acumulacion.png"))

etiqueta = tk.Label(ventana, image=lista.actual.valor)
etiqueta.pack()


def siguiente():
    lista.actual = lista.actual.siguiente
    etiqueta.config(image=lista.actual.valor)


def anterior():
    lista.actual = lista.actual.anterior
    etiqueta.config(image=lista.actual.valor)


tk.Button(ventana, text="Anterior", command=anterior).pack(side="left")
tk.Button(ventana, text="Siguiente", command=siguiente).pack(side="right")

ventana.mainloop()
