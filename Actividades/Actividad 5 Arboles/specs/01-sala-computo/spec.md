# Especificación — Sala de cómputo

**Versión:** 1.1 · **Fecha:** 2026-10-13 · **Autor:** Andrés

## 1. Propósito
1. Atender turnos de la sala por prioridad, sin que nadie espere para siempre.
2. Consultar el árbol de carpetas de entregas: facultad, programa, curso y semestre.

## 2. Fuera de alcance
- Carpetas reales del disco.
- Varios monitores atendiendo a la vez.

## 3. Niveles y envejecimiento
| Nivel | Situación |
|---|---|
| 1 | Entrega con plazo hoy |
| 2 | Actividades de clases |
| 3 | Uso libre |

- `efectiva = nivel - minutos_esperando // 10`.
- Sale primero la menor efectiva. Con empate, quien llegó antes.

Ejemplo en el minuto 25: Ana es nivel 3 y llegó en el 0. Efectiva 3 - 2 = 1. Luis es nivel 1 y llegó en el 20. Efectiva 1 - 0 = 1. Empatan y sale Ana.

## 4. Operaciones

### Cola de prioridad
- `encolar(nombre, nivel, llegada)`: devuelve `True`. Si el nivel no es 1, 2 o 3, devuelve `False` y no guarda nada.
- `atender(minuto)`: saca y devuelve al estudiante que sigue. Si está vacía, devuelve `None`.
- `esta_vacia()` y `tamaño()`: consultan sin cambiar nada.

### Simulación
- `simular(usar_prioridad, semilla)`: devuelve `(media, peor)` de la espera en minutos. Con la misma semilla, las llegadas son las mismas en los dos escenarios.

### Árbol de carpetas
- `contar(carpeta)`: total de entregas en la carpeta y todo lo que tiene adentro.
- `profundidad(carpeta)`: cantidad de carpetas en la ruta más larga.
- `ruta_mas_profunda(carpeta)`: lista de nombres de esa ruta.
- `por_niveles(raiz)`: nombres de las carpetas, nivel por nivel, de izquierda a derecha.
- `con_pila(raiz)`: el mismo listado, pero sacando primero lo último que entró.

## 5. Invariantes
- INV-01: `tamaño() >= 0` en todo momento.
- INV-02: nadie sale antes que alguien con menor efectiva.
- INV-03: cada carpeta aparece una sola vez en cada listado.

## 6. Criterios de aceptación
| ID | Criterio | Prueba |
|---|---|---|
| CA-01 | Sale primero el nivel 1 | `test_orden_por_nivel` |
| CA-02 | Con empate sale el primero en llegar | `test_empate_es_fifo` |
| CA-03 | Atender con cola vacía devuelve `None` | `test_vacia_devuelve_none` |
| CA-04 | Nivel inválido devuelve `False` | `test_nivel_invalido` |
| CA-05 | Un solo estudiante entra y sale | `test_un_elemento` |
| CA-06 | En el minuto 30, un nivel 3 que llegó en el 0 sale antes que un nivel 1 recién llegado | `test_envejecimiento` |
| CA-07 | Si llega un nivel 1 cada minuto, un nivel 3 sale antes del minuto 30 | `test_no_espera_para_siempre` |
| CA-08 | La simulación devuelve media y peor espera, y repite con la misma semilla | `test_simulacion` |
| CA-09 | `contar`: vacío da 0, un nodo da sus entregas, árbol de prueba da 14 | `test_contar` |
| CA-10 | `profundidad`: vacío da 0, un nodo da 1, árbol de prueba da 4 | `test_profundidad` |
| CA-11 | La ruta más profunda del árbol de prueba es correcta | `test_ruta_mas_profunda` |
| CA-12 | `por_niveles`: vacío da `[]` y el árbol de prueba da el orden esperado | `test_por_niveles` |
| CA-13 | `con_pila` da un orden distinto con las mismas carpetas | `test_con_pila` |

## 7. Casos extremos
- Cola vacía.
- Un solo estudiante.
- Nivel inválido.
- Árbol vacío.
- Árbol de un solo nodo.
