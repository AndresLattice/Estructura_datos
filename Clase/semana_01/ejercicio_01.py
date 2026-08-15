# Código base — Semana 01
# Fuente: 01-Momento-1-Contrato-y-secuencia/01-Semana-01-Repaso-y-modelo-de-memoria/02-guia-de-laboratorio.html


def invertida(lista):
    return lista[::-1]


def invertir_en_sitio(lista):
    lista.reverse()


a = [1, 2, 3]
b = invertida(a)
print(a, b, id(a), id(b))  # a NO cambió, b es un objeto distinto

c = [1, 2, 3]
print(id(c))
invertir_en_sitio(c)
print(c, id(c))  # c SÍ cambió, pero es el MISMO objeto
