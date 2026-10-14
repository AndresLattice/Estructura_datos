# Especificación

## Objetivo
1. Atender turnos de la sala por prioridad, sin espera indefinida.
2. Consultar el árbol de carpetas de entregas.

## Cola de prioridad
| Nivel | Situación |
|---|---|
| 1 | Entrega con plazo hoy |
| 2 | Actividades de clases |
| 3 | Uso libre |

- Sale primero la menor prioridad efectiva.
- Con empate, sale quien llegó antes.
- Envejecimiento: `efectiva = nivel - minutos_esperando // 10`.

Ejemplo en el minuto 25: Ana es nivel 3 y llegó en el minuto 0. Su efectiva es 3 - 2 = 1. Luis es nivel 1 y llegó en el minuto 20. Su efectiva es 1 - 0 = 1. Empatan y sale Ana, que llegó antes.

## Requisitos
- **RF-01:** La cola atiende por prioridad efectiva y, con empate, por llegada.
- **RF-02:** Cola vacía devuelve `None`. Nivel inválido devuelve `False`.
- **RF-03:** La simulación compara FIFO contra prioridad con los mismos estudiantes. Mide espera media y peor espera.
- **RF-04:** Conteo de entregas y profundidad máxima con recursión.
- **RF-05:** Listado por niveles con la cola propia, y el mismo recorrido con pila.

## Criterios de aceptación
| ID | Criterio | Prueba |
|---|---|---|
| CA-01 | Sale primero el nivel 1 | `test_orden_por_nivel` |
| CA-02 | Con empate sale el primero en llegar | `test_empate_es_fifo` |
| CA-03 | Cola vacía devuelve `None` | `test_vacia_devuelve_none` |
| CA-04 | Nivel inválido devuelve `False` | `test_nivel_invalido` |
| CA-05 | Un nivel 3 que espera mucho sale antes que un nivel 1 recién llegado | `test_envejecimiento` |
| CA-06 | La simulación devuelve media y peor espera | `test_simulacion` |
| CA-07 | Conteo con árbol vacío, un nodo y árbol de prueba | `test_contar` |
| CA-08 | Profundidad con árbol vacío, un nodo y árbol de prueba | `test_profundidad` |
| CA-09 | Listado por niveles correcto | `test_niveles` |
| CA-10 | Con pila el orden es distinto | `test_pila_da_otro_orden` |

## Fuera de alcance
- Carpetas reales del disco.
- Varios monitores atendiendo a la vez.
