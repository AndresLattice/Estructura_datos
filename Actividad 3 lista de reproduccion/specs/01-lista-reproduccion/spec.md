# Especificación — Lista de reproducción

**Versión:** 1.3 · **Fecha:** 2026-09-18

## 1. Propósito

La emisora universitaria necesita una lista ordenada de canciones para su
reproductor. Con ella se agregan canciones, se salta a la canción número N,
se retira una canción y se recorre todo para generar la parrilla.

Uso real medido en un día:

| Qué hace el reproductor | Operación de la lista | Veces al día |
|---|---|---|
| Canción de última hora | insertar al principio | 40 |
| Generar la parrilla | recorrer toda la lista | 3 |
| Saltar a la canción N | obtener | 200 |
| Se cayó un derecho de emisión | eliminar | 15 |

## 2. Fuera de alcance

- Reproducir audio o guardar datos de la canción (duración, artista).
- Guardar la lista en disco.
- Usarla desde varios procesos a la vez.

## 3. Decisiones sobre casos dudosos

1. **Las posiciones empiezan en 0.** La primera canción está en la posición 0.
2. **Se puede insertar en la posición `tamaño`.** Así se agrega al final.
3. **Una posición inválida lanza `PosicionInvalidaError`.** Incluye negativas y
   cualquier operación sobre una lista vacía. La lista no cambia si hay error.
4. **`eliminar` devuelve la canción retirada.** Así se sabe cuál salió.
5. **`buscar` devuelve la primera posición donde aparece, o `-1`.**

## 4. Operaciones

| Operación | Precondición | Resultado |
|---|---|---|
| `tamaño()` | — | Cantidad de canciones (0 o más) |
| `insertar(posicion, elemento)` | `0 <= posicion <= tamaño` | El elemento queda en `posicion`, el tamaño sube 1 y el orden de las demás se conserva |
| `obtener(posicion)` | `0 <= posicion < tamaño` | Devuelve la canción de esa posición |
| `eliminar(posicion)` | `0 <= posicion < tamaño` | Devuelve la canción retirada, el tamaño baja 1 y el orden de las demás se conserva |
| `buscar(elemento)` | — | Posición de la primera aparición, o `-1` |
| Recorrer | — | Visita todas las canciones en orden, de la 0 a la última |

Si la precondición no se cumple: `PosicionInvalidaError`.

## 5. Invariantes

- INV-01: el tamaño nunca es negativo.
- INV-02: recorrer la lista visita exactamente `tamaño` canciones.
- INV-03: el tamaño es 0 si y solo si la lista está vacía.

## 6. Criterios de aceptación

| ID | Criterio | Prueba | Archivo |
|----|----------|--------|---------|
| CA-01 | Una lista nueva tiene tamaño 0 | `test_lista_vacia` | test_lista.py |
| CA-02 | Insertar en una lista vacía deja tamaño 1 y la canción accesible | `test_insertar_en_vacia` | test_lista.py |
| CA-03 | Insertar al principio conserva el orden de las demás | `test_insertar_inicio` | test_lista.py |
| CA-04 | `eliminar` devuelve la canción y baja el tamaño | `test_eliminar` | test_lista.py |
| CA-05 | Una posición inválida lanza `PosicionInvalidaError` | `test_posicion_invalida` | test_lista.py |
| CA-06 | `buscar` devuelve `-1` si la canción no está | `test_buscar_ausente` | test_lista.py |
| CA-07 | Insertar 100 canciones seguidas no pierde ni desordena ninguna | `test_redimensionamiento` | test_lista.py |
| CA-08 | Lista vacía: `obtener` y `eliminar` lanzan error y el tamaño sigue en 0 | `test_eliminar_de_vacia_lanza` | test_extremos.py |
| CA-09 | Un elemento: insertar el primero deja tamaño 1 | `test_insertar_en_vacia_fija_cabeza_y_cola` | test_extremos.py |
| CA-10 | Un elemento: borrarlo deja la lista vacía, consistente y con tamaño 0 | `test_eliminar_unico_deja_lista_consistente` | test_extremos.py |
| CA-11 | Borrar el primero baja el tamaño y conserva el resto en orden | `test_eliminar_cabeza_con_varios` | test_extremos.py |
| CA-12 | Borrar el último baja el tamaño y conserva el resto en orden | `test_eliminar_ultimo_actualiza_cola` | test_extremos.py |
| CA-13 | Tras muchas inserciones y borrados la lista sigue consistente | `test_insertar_y_eliminar_alternado` | test_extremos.py |
| CA-14 | Recorrer devuelve todas las canciones en orden | `test_recorrer_en_orden` | test_extremos.py |

`test_lista.py` corre con las dos listas. En `test_extremos.py`, CA-08 y CA-14
corren con las dos, y CA-09 a CA-13 verifican la lista enlazada (donde estos
casos fallan con más facilidad).

`test_redimensionamiento` (CA-07) no lleva el identificador en su docstring
porque `test_lista.py` no se puede modificar; su criterio es CA-07.

## 7. Historial de cambios

| Versión | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-09-18 | Versión inicial | — |
| 1.1 | 2026-09-18 | Los criterios de aceptación se alinean con las pruebas del curso (`test_lista.py`, `test_extremos.py`); CA-01 a CA-14 | El autor decidió usar el código base del curso; la spec se corrige antes del código |
| 1.2 | 2026-09-18 | CA-08 exige también `obtener` sobre la lista vacía y corre con las dos listas; se aclara la trazabilidad de CA-07 | Revisión contra el enunciado |
| 1.3 | 2026-09-18 | CA-11 y CA-12 exigen también el tamaño correcto | Segunda revisión contra el enunciado: borrar el primero o el último deja con facilidad un tamaño incorrecto |
