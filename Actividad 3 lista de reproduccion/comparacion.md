# Comparación: ListaArreglo frente a ListaEnlazada

Lista de 5.000 canciones. Tiempos medidos con `medicion.py` en una sola
ejecución representativa, en microsegundos (µs) por operación. Cada operación se
repite varias veces y se promedia. `obtener` y `eliminar` se miden en la mitad
de la lista (posición 2.500), igual en las dos estructuras. Los tiempos varían
entre ejecuciones (entre 5 % y 20 %), por eso se repitió la medición varias
veces y las conclusiones se mantienen: el total del día fue siempre menor para
la enlazada (entre 14,5 y 15,8 ms) que para el arreglo (entre 16,5 y 16,9 ms).

## Resultado de pasar `test_lista.py`

`test_lista.py` (la prueba de la semana 4) corre con las dos listas y no se
modificó, salvo el `import` y la lista `IMPLEMENTACIONES`. Las dos pasan las 7
pruebas (14 ejecuciones). El contrato estaba bien escrito.

Con el esqueleto original de la lista enlazada, que define su propio
`PosicionInvalidaError`, `test_posicion_invalida` fallaba para la enlazada (1
falla y 13 pasan). El defecto estaba en la implementación y no en el contrato:
la prueba captura el error definido en `lista_arreglo.py` y la enlazada lanzaba
otro con el mismo nombre. Se corrigió importando ese mismo error en
`lista_enlazada.py`, sin tocar la prueba.

## 1. Tabla resumen: costo teórico y medido

| Operación | Arreglo teórico | Arreglo medido | Enlazada teórico | Enlazada medido |
|---|---|---|---|---|
| Insertar al principio | O(n) | 335,01 µs | O(1) | 0,60 µs |
| Recorrer toda la lista | O(n) | 240,95 µs | O(n) | 198,06 µs |
| Ir a la canción N (mitad) | O(1) | 0,32 µs | O(p) | 64,83 µs |
| Borrar la canción actual (mitad) | O(n) | 162,30 µs | O(p) | 66,12 µs |
| Insertar al final (no está en el perfil de la emisora) | O(1) amortizado | no medido | O(1) con `_cola` (O(n) sin ella) | no medido |

**Decisión de diseño: `_cola`.** La lista enlazada guarda un puntero al último nodo (`_cola`). Con él, añadir al final cuesta O(1); sin él costaría O(n), porque habría que recorrer toda la cadena. La emisora nunca añade al final, así que esta decisión no cambia ninguna cifra de esta comparación, y por eso esa fila no se mide. Sí obliga a actualizar `_cola` al borrar el último o el único elemento, casos cubiertos por CA-10 y CA-12.

**Lectura de la tabla**

- **Insertar al principio:** el arreglo corre las 5.000 canciones y la enlazada
  solo cambia la cabeza. La enlazada es unas 560 veces más rápida.
- **Ir a la canción N:** el arreglo va directo y la enlazada camina unos 2.500
  nodos. El arreglo es unas 200 veces más rápido.
- **Borrar la canción actual:** la enlazada camina hasta el nodo anterior
  (por eso cuesta casi lo mismo que `obtener`, 66 µs); el arreglo mueve las
  canciones posteriores. La enlazada gana por un factor de 2,5.
- **Recorrer:** teóricamente son iguales (O(n)). La enlazada salió algo más
  rápida por la forma en que Python ejecuta cada recorrido, no por un cambio de
  complejidad. Es la única diferencia entre teoría y medición que hay que
  explicar, y no cambia ninguna conclusión.

Las mediciones coinciden con la teoría de `plan.md`, así que no hizo falta
corregirlo.

## 2. Costo de un día de emisión

Costo = veces al día × tiempo de una ejecución.

| Operación | Veces al día | Arreglo | Enlazada |
|---|---|---|---|
| Insertar al principio | 40 | 40 × 335,01 µs = 13,400 ms | 40 × 0,60 µs = 0,024 ms |
| Recorrer toda la lista | 3 | 3 × 240,95 µs = 0,723 ms | 3 × 198,06 µs = 0,594 ms |
| Ir a la canción N | 200 | 200 × 0,32 µs = 0,063 ms | 200 × 64,83 µs = 12,967 ms |
| Borrar la canción actual | 15 | 15 × 162,30 µs = 2,434 ms | 15 × 66,12 µs = 0,992 ms |
| **Total del día** | | **16,621 ms** | **14,577 ms** |

Cada estructura tiene una operación que domina su día:

- **Arreglo:** insertar al principio pesa 13,4 ms de 16,6 ms.
- **Enlazada:** ir a la canción N pesa 13,0 ms de 14,6 ms.

## 3. Recomendación

**Con las frecuencias dadas, se recomienda `ListaEnlazada`:** cuesta 14,58 ms al
día frente a 16,62 ms del arreglo, unos 2 ms menos (alrededor de un 12 %).

La razón sale de los números y no de que "las enlazadas sean mejores para
insertar". Las 40 inserciones al principio le cuestan mucho al arreglo, y las
200 consultas por posición le cuestan mucho a la enlazada. En este perfil, lo
que la enlazada ahorra (unos 14,9 ms entre inserciones, borrados y recorridos)
supera a lo que pierde en las consultas (unos 12,9 ms). La diferencia es
pequeña, y por eso más abajo se dice con qué margen se sostiene.

**Advertencia honesta.** Los dos costos son minúsculos en términos absolutos:
menos de 20 milisegundos por día de emisión. En la práctica cualquiera de las
dos estructuras sirve para 5.000 canciones. La recomendación se basa en la
medición, pero la ventaja es estrecha.

## 4. Qué tendría que cambiar para que la recomendación cambiara

La diferencia entre estructuras, en microsegundos por día, es:

```
arreglo − enlazada = veces_insertar × 334,41
                   + veces_recorrer × 42,89
                   − veces_saltar   × 64,51
                   + veces_borrar   × 96,18
```

Si el resultado es positivo, gana la enlazada; si es negativo, el arreglo.
Cambiando una frecuencia a la vez y dejando las demás como están:

| Cambio | Valor actual | Valor que invierte la recomendación |
|---|---|---|
| Suben los saltos a la canción N | 200 al día | unos **232 al día** o más (solo un 16 % más) |
| Bajan las inserciones al principio | 40 al día | unas **34 al día** o menos (un 15 % menos) |

Es decir, el arreglo pasa a ser mejor si la emisora salta más de unas 230
veces al día, o si mete canciones de última hora menos de unas 34 veces al día.

Un cambio así de pequeño invierte la recomendación porque los dos costos
grandes (insertar en el arreglo y saltar en la enlazada) están casi
equilibrados. Si el perfil se mueve mucho hacia un lado, la decisión deja de
ser ajustada:

- Si casi no se saltara y se insertara mucho al principio, la enlazada ganaría
  con holgura.
- Si se saltara mucho y casi no se insertara ni borrara, el arreglo ganaría con
  holgura.

## 5. Cómo reproducir las mediciones

```bash
python medicion.py
```
