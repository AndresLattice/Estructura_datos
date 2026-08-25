# Prediccion de complejidad - ListaArreglo

Escrita antes de medir nada. `n` es `tamaño` (cantidad de elementos
guardados).

## Diseño interno asumido

`ListaArreglo` guarda los elementos en un bloque de memoria de
capacidad fija (una lista de Python usada solo como arreglo: se
accede y se asigna por indice, nunca con `append`/`insert`/`remove`).
Cuando se llena, se crea un bloque del doble de capacidad y se copian
los elementos uno por uno. Este detalle se retoma en `plan.md`.

## Tabla de complejidad

| Operacion | Big-O | Conteo de operaciones |
|---|---|---|
| `insertar(pos, x)` | O(n) | En el peor caso (`pos == 0`) hay que mover los `n` elementos existentes una posicion a la derecha antes de escribir `x`: `n` asignaciones. En el mejor caso (`pos == n`, insertar al final) no se mueve nada: O(1). Se declara O(n) porque el contrato admite cualquier `pos`. |
| `insertar_ordenado(x)` | O(n) | Hay que recorrer para encontrar la posicion donde `x` mantiene el orden (hasta `n` comparaciones) y luego desplazar los elementos posteriores (hasta `n` asignaciones). Las dos partes son O(n), la suma sigue siendo O(n). |
| `obtener(pos)` | O(1) | Acceso directo por indice al bloque de memoria: una sola lectura, sin importar `n`. |
| `buscar_lineal(x)` | O(n) | En el peor caso (elemento ausente o en la ultima posicion) se comparan los `n` elementos uno por uno. |
| `buscar_binaria(x)` | O(log n) | Cada comparacion descarta la mitad de los elementos restantes. El numero de veces que `n` se puede partir a la mitad hasta llegar a 1 es `log2(n)`. |

## Que se espera ver en las graficas (parte C)

- `obtener`: una linea prácticamente plana (no depende de n).
- `buscar_lineal` e `insertar` (peor caso): crecimiento lineal.
- `buscar_binaria`: crecimiento muy lento; en escala normal puede verse
  casi plana, por eso se recomienda graficarla tambien en escala
  logaritmica en el eje X.
