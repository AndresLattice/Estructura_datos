# Arreglo de capacidad 5. Índices `frente` y `final`.
#
# Vacía:        [_, _, _, _, _]   frente=0  final=0  tamaño=0
# encolar A:    [A, _, _, _, _]   frente=0  final=1  tamaño=1
# encolar B:    [A, B, _, _, _]   frente=0  final=2  tamaño=2
# desencolar:   [_, B, _, _, _]   frente=1  final=2  tamaño=1
# ...
# encolar C,D,E:[_, B, C, D, E]   frente=1  final=0  tamaño=4   <- final "dio la vuelta"
# encolar F:    [F, B, C, D, E]   frente=1  final=1  tamaño=5   <- LLENA
#
# ¡AQUÍ ESTÁ LA TRAMPA!
#   Cola vacía:  frente == final
#   Cola llena:  frente == final
#   Son indistinguibles solo con los índices.
#
# Tres soluciones posibles:
#   (a) Guardar `_tamaño` explícitamente        <- la que usaremos
#   (b) Dejar siempre una posición sin usar
#   (c) Guardar una bandera booleana `llena`
#
# Avanzar un índice circularmente:
#   indice = (indice + 1) % capacidad