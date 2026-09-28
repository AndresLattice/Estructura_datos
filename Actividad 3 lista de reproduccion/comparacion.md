# Comparación: ListaArreglo frente a ListaEnlazada

Lista de 5.000 canciones. Tiempos medidos con `medicion.py` en una sola
ejecución representativa, en microsegundos (µs) por operación. Cada operación se
repite varias veces y se promedia. `obtener` y `eliminar` se miden en la mitad
de la lista (posición 2.500), igual en las dos estructuras. Los tiempos varían
entre ejecuciones, por eso se repitió la medición varias veces y las
conclusiones se mantienen: el total del día fue siempre menor para la enlazada
(entre 14,3 y 18,1 ms) que para el arreglo (entre 23,0 y 25,2 ms).

## Resultado de las pruebas

`test_lista.py` y `test_extremos.py` corren con las dos listas. Las dos pasan
todas las pruebas (23 ejecuciones en total).

## 1. Tabla resumen: costo teórico y medido

| Operación | Arreglo teórico | Arreglo medido | Enlazada teórico | Enlazada medido |
|---|---|---|---|---|
| Insertar al principio | O(n) | 460,33 µs | O(1) | 0,42 µs |
| Recorrer toda la lista | O(n) | 247,69 µs | O(n) | 188,16 µs |
| Ir a la canción N (mitad) | O(1) | 0,14 µs | O(p) | 63,59 µs |
| Borrar la canción actual (mitad) | O(n) | 274,14 µs | O(p) | 64,22 µs |
| Insertar al final (no está en el perfil de la emisora) | O(1) amortizado | no medido | O(1) con `cola` (O(n) sin ella) | no medido |

**Decisión de diseño: `cola`.** La lista enlazada guarda una referencia al último nodo (`cola`). Con ella, añadir al final cuesta O(1); sin ella costaría O(n), porque habría que recorrer toda la cadena. La emisora nunca añade al final, así que esta decisión no cambia ninguna cifra de esta comparación, y por eso esa fila no se mide. Sí obliga a actualizar `cola` al borrar el último o el único elemento, casos cubiertos por CA-10 y CA-12.

**Lectura de la tabla**

- **Insertar al principio:** el arreglo corre las 5.000 canciones una por una y
  la enlazada solo cambia la cabeza. La enlazada es unas 1.100 veces más rápida.
- **Ir a la canción N:** el arreglo va directo y la enlazada camina unos 2.500
  nodos. El arreglo es unas 450 veces más rápido.
- **Borrar la canción actual:** la enlazada camina hasta el nodo anterior
  (por eso cuesta casi lo mismo que `obtener`, 64 µs); el arreglo mueve las
  canciones posteriores una por una. La enlazada gana por un factor de 4,3.
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
| Insertar al principio | 40 | 40 × 460,33 µs = 18,413 ms | 40 × 0,42 µs = 0,017 ms |
| Recorrer toda la lista | 3 | 3 × 247,69 µs = 0,743 ms | 3 × 188,16 µs = 0,564 ms |
| Ir a la canción N | 200 | 200 × 0,14 µs = 0,028 ms | 200 × 63,59 µs = 12,718 ms |
| Borrar la canción actual | 15 | 15 × 274,14 µs = 4,112 ms | 15 × 64,22 µs = 0,963 ms |
| **Total del día** | | **23,297 ms** | **14,263 ms** |

Cada estructura tiene una operación que domina su día:

- **Arreglo:** insertar al principio pesa 18,4 ms de 23,3 ms.
- **Enlazada:** ir a la canción N pesa 12,7 ms de 14,3 ms.

## 3. Recomendación

**Con las frecuencias dadas, se recomienda `ListaEnlazada`:** cuesta 14,26 ms al
día frente a 23,30 ms del arreglo, unos 9 ms menos (alrededor de un 39 %).

La razón sale de los números y no de que "las enlazadas sean mejores para
insertar". Las 40 inserciones al principio le cuestan mucho al arreglo, y las
200 consultas por posición le cuestan mucho a la enlazada. En este perfil, lo
que la enlazada ahorra (unos 21,7 ms entre inserciones, borrados y recorridos)
supera con claridad a lo que pierde en las consultas (unos 12,7 ms).

**Advertencia honesta.** Los dos costos son minúsculos en términos absolutos:
menos de 30 milisegundos por día de emisión. En la práctica cualquiera de las
dos estructuras sirve para 5.000 canciones. La recomendación se basa en la
medición.

## 4. Qué tendría que cambiar para que la recomendación cambiara

La diferencia entre estructuras, en microsegundos por día, es:

```
arreglo − enlazada = veces_insertar × 459,91
                   + veces_recorrer × 59,53
                   − veces_saltar   × 63,45
                   + veces_borrar   × 209,92
```

Si el resultado es positivo, gana la enlazada; si es negativo, el arreglo.
Cambiando una frecuencia a la vez y dejando las demás como están:

| Cambio | Valor actual | Valor que invierte la recomendación |
|---|---|---|
| Suben los saltos a la canción N | 200 al día | unos **343 al día** o más (un 71 % más) |
| Bajan las inserciones al principio | 40 al día | unas **20 al día** o menos (la mitad) |

Es decir, el arreglo pasa a ser mejor si la emisora salta más de unas 340
veces al día, o si mete canciones de última hora menos de unas 20 veces al día.

Hace falta un cambio grande en el perfil para invertir la recomendación, porque
insertar al principio en el arreglo cuesta bastante más de lo que cuesta saltar
en la enlazada. Si el perfil se mueve mucho hacia un lado:

- Si casi no se saltara y se insertara mucho al principio, la enlazada ganaría
  con más holgura todavía.
- Si se saltara mucho y casi no se insertara ni borrara, el arreglo ganaría.

## 5. Cómo reproducir las mediciones

```bash
python medicion.py
```
