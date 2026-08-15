# Código base — Semana 01
# Fuente: 01-Momento-1-Contrato-y-secuencia/01-Semana-01-Repaso-y-modelo-de-memoria/02-guia-de-laboratorio.html

x = [1, 2, 3]
y = x
y.append(4)
print(x)          # ¿qué imprime?

z = x[:]          # esto sí es una copia
z.append(5)
print(x, z)       # ¿y ahora?

def agregar(lista):
    lista.append(99)

agregar(x)
print(x)          # ¿la función modificó x?
