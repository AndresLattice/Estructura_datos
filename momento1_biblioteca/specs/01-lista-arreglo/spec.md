# Especificacion de ListaArreglo

## 1. Proposito

Catalogo de la biblioteca: registrar elementos, consultar uno por su
posicion y buscarlo por su clave, para poder estudiar el costo de esas
operaciones al crecer de 80.000 a 200.000 registros.

## 2. Fuera de alcance

- Datos reales de un libro: se usan elementos genericos comparables
  (enteros o cadenas) como clave del libro.
- Persistencia, concurrencia y eliminar elementos (no lo exige el
  enunciado).

## 3. Ambiguedades y decision

- **Tipo de dato:** elementos genericos comparables con `<`.
- **`buscar_binaria` sin lista ordenada:** comportamiento indefinido;
  es precondicion que este ordenada, no se valida en runtime (validarlo
  costaria O(n) y anularia el proposito de la busqueda).
- **Elemento no encontrado:** ambas busquedas devuelven -1.
- **`insertar` con posicion fuera de rango:** se rechaza si `pos < 0` o
  `pos > tamaño`. `pos == tamaño` inserta al final.
- **Valores repetidos en `insertar_ordenado`:** se permiten; el nuevo
  queda despues del ultimo igual.
- **`obtener` fuera de rango:** se rechaza si `pos < 0` o
  `pos >= tamaño` (no se devuelve un valor por defecto).

## 4. Operaciones

| Operacion | Precondiciones | Postcondiciones | Errores |
|---|---|---|---|
| `insertar(pos, x)` | `0 <= pos <= tamaño` | `x` queda en `pos`; los siguientes se desplazan uno a la derecha; tamaño +1 | `pos` fuera de rango |
| `insertar_ordenado(x)` | lista ordenada ascendente | `x` queda en la posicion que conserva el orden (tras el ultimo igual); tamaño +1 | ninguno |
| `obtener(pos)` | `0 <= pos < tamaño` | devuelve el elemento en `pos` | `pos` fuera de rango |
| `buscar_lineal(x)` | -- | devuelve la primera posicion de `x`, o -1 | ninguno |
| `buscar_binaria(x)` | lista ordenada ascendente | devuelve una posicion de `x`, o -1 | ninguno |

## 5. Invariantes

- INV-01: `tamaño >= 0` siempre.
- INV-02: recorrer `obtener(0)..obtener(tamaño-1)` visita exactamente
  `tamaño` elementos, en el orden de insercion.

## 6. Criterios de aceptacion

| ID | Criterio | Verificable mediante |
|---|---|---|
| CA-01 | Lista nueva tiene tamaño 0 | test_lista_nueva_esta_vacia |
| CA-02 | Obtener en vacia se rechaza | test_obtener_en_vacia_lanza_error |
| CA-03 | Insertar en vacia deja un elemento | test_insertar_en_lista_vacia |
| CA-04 | Insertar al inicio desplaza lo existente | test_insertar_al_inicio_desplaza |
| CA-05 | Insertar al final no desplaza nada | test_insertar_al_final_no_desplaza |
| CA-06 | Insertar en medio desplaza solo lo posterior | test_insertar_en_medio_desplaza_lo_necesario |
| CA-07 | Insertar con posicion negativa se rechaza | test_insertar_posicion_negativa_lanza_error |
| CA-08 | Insertar con posicion mayor al tamaño se rechaza | test_insertar_posicion_mayor_al_tamano_lanza_error |
| CA-09 | insertar_ordenado en vacia deja un elemento | test_insertar_ordenado_en_vacia |
| CA-10 | insertar_ordenado mantiene el orden | test_insertar_ordenado_mantiene_orden |
| CA-11 | insertar_ordenado con repetidos va despues del ultimo igual | test_insertar_ordenado_con_repetidos |
| CA-12 | obtener devuelve el elemento correcto | test_obtener_devuelve_elemento_correcto |
| CA-13 | obtener con posicion negativa se rechaza | test_obtener_posicion_negativa_lanza_error |
| CA-14 | obtener con posicion fuera de rango se rechaza | test_obtener_posicion_fuera_de_rango_lanza_error |
| CA-15 | buscar_lineal en vacia devuelve -1 | test_buscar_lineal_en_vacia |
| CA-16 | buscar_lineal encuentra el elemento | test_buscar_lineal_encuentra_elemento |
| CA-17 | buscar_lineal con ausente devuelve -1 | test_buscar_lineal_elemento_ausente |
| CA-18 | buscar_binaria en vacia devuelve -1 | test_buscar_binaria_en_vacia |
| CA-19 | buscar_binaria con un elemento | test_buscar_binaria_lista_de_un_elemento |
| CA-20 | buscar_binaria en bordes, tamaño par | test_buscar_binaria_bordes_tamano_par |
| CA-21 | buscar_binaria en bordes, tamaño impar | test_buscar_binaria_bordes_tamano_impar |
| CA-22 | buscar_binaria con ausente devuelve -1 | test_buscar_binaria_elemento_ausente |

## 7. Casos extremos considerados

Vacia, un elemento, insertar al inicio/final, posiciones invalidas,
elemento ausente, valores repetidos, bordes de la busqueda binaria en
tamaño par e impar.

## 8. Historial de cambios

| Version | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-08-25 | Version inicial | -- |
