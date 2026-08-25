# Plan tecnico - ListaArreglo

**Especificacion de referencia:** `spec.md` v1.0

## 1. Estructura de datos elegida

Un arreglo de capacidad fija: internamente se usa una lista de Python
solo como bloque de memoria (`_datos`), accedida y modificada por
indice. No se usan `append`, `insert`, `remove`, `sort` ni `in`. Cuando
`_tamano == _capacidad`, se crea un bloque del doble de capacidad y se
copian los elementos existentes uno por uno antes de continuar.

## 2. Alternativas consideradas

| Alternativa | Ventaja | Por que se descarto |
|---|---|---|
| Lista de Python con `append`/`insert` de alto nivel | Mucho menos codigo | Prohibido por la constitucion: el ejercicio es reimplementar el arreglo, no usar el de Python |
| Arreglo de capacidad fija sin redimension (tamaño maximo definido al crear) | Mas simple aun | No sirve para las mediciones, que necesitan listas de hasta 200.000 elementos construidas incrementalmente |
| Arreglo con redimension por duplicacion (elegida) | Costo de redimension amortizado, cercano a como funciona una lista dinamica real | Ninguna: es la que mejor equilibra fidelidad al arreglo real y simplicidad |

## 3. Complejidad esperada

Ver `prediccion.md` para el detalle del conteo de operaciones. Resumen:

| Operacion | Tiempo | Espacio extra |
|---|---|---|
| `insertar` | O(n) | O(1) (O(n) solo en la redimension, amortizado) |
| `insertar_ordenado` | O(n) | O(1) |
| `obtener` | O(1) | O(1) |
| `buscar_lineal` | O(n) | O(1) |
| `buscar_binaria` | O(log n) | O(1) |

## 4. Diseño interno

- `_datos`: lista de Python usada como bloque de memoria de tamaño
  `_capacidad`, con posiciones no usadas en `None`.
- `_tamano`: cantidad de elementos realmente guardados (`_tamano <=
  _capacidad`).
- Invariante de representacion: las posiciones `0.._tamano-1` de
  `_datos` contienen los elementos de la lista, en orden; las
  posiciones `_tamano.._capacidad-1` no se usan.
- Redimension: al insertar con `_tamano == _capacidad`, se crea un
  nuevo bloque de `_capacidad * 2` y se copian los `_tamano` elementos
  antes de insertar el nuevo.

## 5. Riesgos tecnicos

| Riesgo | Impacto | Mitigacion |
|---|---|---|
| Confundir la complejidad amortizada de la redimension con la de una insercion individual | La prediccion podria subestimar el costo de una insercion puntual que dispara redimension | prediccion.md declara O(n) para insertar considerando el peor caso de desplazamiento, no solo la redimension |
| Off-by-one en `buscar_binaria` con tamaño par | Fallar en los bordes (CA-20) | Pruebas explicitas con tamaño par e impar antes de medir |
