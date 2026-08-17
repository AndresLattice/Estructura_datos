# Especificacion del carrito

## 1. Proposito

La tienda del campus (basicamente la cafeteria del piso 10) 
necesita reemplazar un carrito de compras manejado a mano
en un archivo de texto. El Carrito debe permitir registrar productos
que un cliente quiere comprar, quitarlos si cambia de decision, consultar
cuantas unidades de un producto lleva y conocer el total de unidades en
todo momento.

## 2. Fuera de alcance

- Precios, impuestos o cualquier calculo monetario real.
- Persistencia (guardar el carrito en disco o base de datos).
- Concurrencia: el Carrito no esta disenado para ser modificado por dos
  procesos al mismo tiempo.
- Catalogo de productos validos: el Carrito no valida que un producto
  exista en un inventario externo, solo administra cantidades.

## 3. Ambiguedades del requisito original y decision

El requisito entregado -- "necesito poder meter productos, sacar
productos, saber cuantos hay de cada uno y cuanto llevo en total" -- no
responde varias preguntas. Cada una se decidio antes de escribir
cualquier operacion.

### 3.1 ¿Se puede quitar un producto que no esta en el carrito?

**Decision:** no. Se rechaza con un error.

**Razon:** un carrito real no permite "quitar" algo que nunca existio
en el carrito.

### 3.2 ¿Que pasa si la cantidad indicada es cero?

**Decision:** tanto agregar como quitar rechazan cantidad 0 con un error.

**Razon:** operar con cero unidades no tiene sentido.

### 3.3 ¿El carrito admite cantidades negativas?

**Decision:** no. La cantidad de cualquier operacion debe ser un entero
mayor que 0. "Restar" se expresa quitando, no agregando una cantidad
negativa.

**Razon:** permitir negativos en la operacion de agregar crearia dos
formas distintas de lograr lo mismo (agregar -3 frente a quitar 3)
y abre la puerta a inconsistencias.

### 3.4 ¿Que devuelve "cuanto llevo en total" si el carrito esta vacio?

**Decision:** 0.

**Razon:** es el valor neutro de la suma y evita que quien use el
carrito tenga que tratar None como caso especial antes de sumar o
mostrar el total. (Sugerencia de la IA)

### 3.5 ¿Que pasa si se pide quitar mas cantidad de la que hay?

**Decision:** se rechaza con un error; no se quita "lo que haya y
listo".

**Razon:** pedir quitar mas de lo que existe casi siempre delata que
quien llama al carrito perdio la cuenta de las unidades disponibles. Es
ademas coherente con 3.3: el carrito nunca debe quedar con una cantidad
negativa de un producto.

### 3.6 ¿Los nombres de producto distinguen mayusculas de minusculas?

**Decision:** si, la comparacion es exacta, sin normalizar mayusculas ni
espacios.

**Razon:** normalizar cadenas es responsabilidad de la capa que captura
el dato (un formulario, un lector de codigo de barras), no del Carrito,
que solo administra cantidades.

## 4. Operaciones

### `agregar(producto, cantidad)`

- **Proposito:** registrar unidades de un producto en el carrito.
- **Precondiciones:** `cantidad` es un entero mayor que 0.
- **Postcondiciones:** si `producto` ya estaba en el carrito, su
  cantidad aumenta en `cantidad`; si no estaba, queda registrado con esa
  cantidad.
- **Errores:** se rechaza si `cantidad` no es un entero mayor que 0.

### `quitar(producto, cantidad)`

- **Proposito:** quitar unidades de un producto ya registrado.
- **Precondiciones:** `cantidad` es un entero mayor que 0; `producto`
  esta en el carrito con una cantidad disponible mayor o igual a
  `cantidad`.
- **Postcondiciones:** la cantidad de `producto` disminuye en
  `cantidad`; si llega a 0, el producto deja de estar registrado en el
  carrito.
- **Errores:** se rechaza si `cantidad` no es un entero mayor que 0, si
  `producto` no esta en el carrito, o si se pide quitar mas cantidad de
  la disponible.

### `cantidad_de(producto)`

- **Proposito:** consultar cuantas unidades de un producto lleva el
  carrito.
- **Postcondiciones:** devuelve la cantidad registrada de `producto`, o
  0 si el producto no esta en el carrito.
- **Errores:** ninguno; es una consulta y nunca falla.

### `total()`

- **Proposito:** conocer cuantas unidades hay en total en el carrito.
- **Postcondiciones:** devuelve la suma de las cantidades de todos los
  productos registrados, o 0 si el carrito esta vacio.

### `esta_vacio()`

- **Proposito:** saber si el carrito no tiene ningun producto
  registrado.
- **Postcondiciones:** devuelve verdadero si no hay productos
  registrados, falso en caso contrario.

## 5. Invariantes

- INV-01: todo producto registrado en el carrito tiene una cantidad
  entera mayor que 0. No existen productos con cantidad 0 o negativa.
- INV-02: `total()` es siempre igual a la suma de `cantidad_de(p)` para
  todo producto `p` alguna vez agregado y no retirado por completo.

## 6. Criterios de aceptacion

| ID | Criterio | Verificable mediante |
|----|----------|----------------------|
| CA-01 | Un carrito recien creado esta vacio | test_carrito_nuevo_esta_vacio |
| CA-02 | El total de un carrito vacio es 0 | test_total_de_carrito_vacio_es_cero |
| CA-03 | Consultar la cantidad de un producto ausente en un carrito vacio devuelve 0 | test_cantidad_de_producto_ausente_en_carrito_vacio_es_cero |
| CA-04 | Quitar de un carrito vacio se rechaza | test_quitar_de_carrito_vacio_lanza_error |
| CA-05 | Agregar un producto nuevo lo deja registrado con esa cantidad | test_agregar_un_producto_nuevo |
| CA-06 | Agregar el mismo producto dos veces acumula la cantidad | test_agregar_el_mismo_producto_dos_veces_acumula |
| CA-07 | Agregar productos distintos los mantiene separados y el total los suma | test_agregar_productos_distintos |
| CA-08 | Agregar cantidad 0 se rechaza | test_agregar_cantidad_cero_lanza_error |
| CA-09 | Agregar cantidad negativa se rechaza | test_agregar_cantidad_negativa_lanza_error |
| CA-10 | Agregar una cantidad no entera se rechaza | test_agregar_cantidad_no_entera_lanza_error |
| CA-11 | Los nombres de producto distinguen mayusculas de minusculas | test_nombres_de_producto_distinguen_mayusculas |
| CA-12 | Quitar una cantidad parcial reduce lo registrado | test_quitar_parcialmente |
| CA-13 | Quitar toda la cantidad de un producto lo elimina del carrito | test_quitar_todo_elimina_el_producto |
| CA-14 | Quitar un producto no registrado se rechaza | test_quitar_producto_inexistente_lanza_error |
| CA-15 | Quitar mas cantidad de la disponible se rechaza y no altera el carrito | test_quitar_mas_de_lo_que_hay_lanza_error |
| CA-16 | Quitar cantidad 0 se rechaza | test_quitar_cantidad_cero_lanza_error |
| CA-17 | Quitar cantidad negativa se rechaza | test_quitar_cantidad_negativa_lanza_error |
| CA-18 | El total suma las cantidades de todos los productos registrados | test_total_suma_todos_los_productos |
| CA-19 | El total refleja correctamente una operacion de quitar posterior | test_total_despues_de_quitar |

## 7. Casos extremos considerados

- Carrito vacio (CA-01, CA-02, CA-03, CA-04).
- Quitar un producto que no esta (CA-04, CA-14).
- Cantidad cero al agregar o quitar (CA-08, CA-16).
- Cantidad negativa al agregar o quitar (CA-09, CA-17).
- Cantidad no entera al agregar (CA-10).
- Quitar mas de lo disponible (CA-15).
- Quitar exactamente toda la cantidad disponible (CA-13).
- Sensibilidad a mayusculas/minusculas en el nombre del producto (CA-11).

## 8. Historial de cambios

| Version | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-08-17 | Version inicial | -- |
