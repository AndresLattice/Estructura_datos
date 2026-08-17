# Plan Tecnico - Carrito

**Especificacion de referencia:** `spec.md` v1.0

**Nota:** este documento se redacto con ayuda de una IA (Claude), tanto
para entender las alternativas de diseño como para redactar el
contenido a partir de las decisiones tomadas por el autor. Ver
`CONSTITUTION.md` para el detalle del uso permitido.

## 1. Estructura de datos elegida

Se implementa el mismo contrato dos veces, sobre dos estructuras
distintas, para comparar sus costos: una lista de pares
`[producto, cantidad]` (`carrito_lista.py`) y un diccionario
`producto -> cantidad` (`carrito_dict.py`). La bateria de pruebas de
`spec.md` corre sin modificarse contra ambas.

No se usa `collections.Counter` por restriccion explicita de la
constitucion del proyecto.

## 2. Alternativas consideradas

| Alternativa | Ventaja | Por que se descarto |
|---|---|---|
| Lista de pares `[producto, cantidad]` | Simple de recorrer; no requiere que el producto sea hashable | Buscar, agregar o quitar un producto cuesta O(n) porque hay que recorrer la lista |
| Diccionario `producto -> cantidad` | Buscar, agregar o quitar cuesta O(1) en promedio | Exige que `producto` sea hashable (en la practica no es una limitacion real, ya que se usan strings) |
| `collections.Counter` | Resolveria directamente la acumulacion de cantidades | Prohibido por la constitucion del proyecto |

Ambas alternativas viables (lista y diccionario) se implementan para
comparar su complejidad.

## 3. Complejidad esperada

| Operacion | Lista de pares | Diccionario | Justificacion |
|---|---|---|---|
| `agregar` | O(n) | O(1) amortizado | La lista debe recorrerse para saber si el producto ya existe; el diccionario resuelve la busqueda por hash |
| `quitar` | O(n) | O(1) amortizado | Misma razon que `agregar`: localizar el producto es lo que domina el costo |
| `cantidad_de` | O(n) | O(1) amortizado | Busqueda por recorrido frente a busqueda por hash |
| `total` | O(n) | O(n) | Ambas deben sumar la cantidad de cada producto registrado |
| `esta_vacio` | O(1) | O(1) | Ambas consultan directamente el tamano de su estructura interna |

`n` es la cantidad de productos distintos registrados en el carrito.

## 4. Diseno interno

### `carrito_lista.Carrito`

- `_items`: lista de pares `[producto, cantidad]`. Cada producto aparece
  a lo sumo una vez.
- Invariante de representacion: no hay dos pares con el mismo
  `producto`; ningun par tiene `cantidad <= 0`.

### `carrito_dict.Carrito`

- `_cantidades`: diccionario `producto -> cantidad`.
- Invariante de representacion: ninguna clave tiene valor `<= 0`.

## 5. Riesgos tecnicos

| Riesgo | Impacto | Mitigacion |
|---|---|---|
| Compartir por referencia la estructura interna entre dos instancias de `Carrito` (ej. un valor por defecto mutable en `__init__`) | Dos carritos distintos terminarian modificandose mutuamente | Cada instancia crea su propia estructura interna dentro de `__init__` |
| Que las pruebas dependan de detalles de una sola implementacion | El archivo de pruebas tendria que modificarse entre implementaciones | Las pruebas solo llaman a las operaciones del contrato, nunca a `_items` ni `_cantidades` directamente |
