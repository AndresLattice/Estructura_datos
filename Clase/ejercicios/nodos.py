

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        
a = Nodo(5)
b = Nodo(10)

print("Referencia del objeto a:", a)
print("Referencia del objeto b:", b)

a.siguiente = b
c = Nodo(15)
d = Nodo(20)

b.siguiente = c
c.siguiente = d

print("Valor del nodo a:", a.dato)
print("Valor del nodo b:", b.dato)
print("Valor del nodo c:", c.dato)
print("Valor del nodo d:", d.dato)


#------------------------------------------------
# Asignacion de Nodo a otro Nodo en medio.
#------------------------------------------------

n1 = Nodo(1)
n2 = Nodo(2)
n3 = Nodo(3)

n1.siguiente = n3
# Opcion 1: Variable temporal
temp = n1.siguiente
n1.siguiente = n2
n2.siguiente = temp
# Opcion 2: Sin variable temporal
n1.siguiente = n2
n2.siguiente = n3

