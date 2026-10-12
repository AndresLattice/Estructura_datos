# SIN centinela — lista con [A, B, C]
#   None <- [A] <-> [B] <-> [C] -> None
#   Al eliminar A hay que actualizar `cabeza`.
#   Al eliminar C hay que actualizar `cola`.
#   Al eliminar B no hay que actualizar nada.
#   => tres casos distintos

# CON centinela — lista con [A, B, C]
#   [S] <-> [A] <-> [B] <-> [C] <-> (vuelve a S)
#    ^--------------------------------|
#   El centinela S nunca guarda datos.
#   Eliminar CUALQUIER nodo es siempre:
#       nodo.anterior.siguiente = nodo.siguiente
#       nodo.siguiente.anterior = nodo.anterior
#   => un solo caso

# Lista VACÍA con centinela:
#   [S] <-> (vuelve a S)      es decir  S.siguiente is S  y  S.anterior is S