# ¿Pila o cola?

## La diferencia en una línea
- **Pila (LIFO):** lo último que entró es lo primero que sale.
- **Cola (FIFO):** lo primero que entró es lo primero que sale.

## Seis escenarios: elige y justifica
| # | Escenario | ¿Pila o cola? | Por qué |
|---|-----------|---------------|---------|
| 1 | Deshacer las últimas acciones de un editor | | |
| 2 | Atender solicitudes de soporte por orden de llegada | | |
| 3 | Evaluar una expresión con paréntesis anidados | | |
| 4 | Enviar trabajos a una impresora compartida | | |
| 5 | Explorar un laberinto probando caminos y retrocediendo | | |
| 6 | Notificaciones que se muestran en el orden en que ocurrieron | | |

## El caso ambiguo
El escenario 5 se puede resolver con pila (DFS) o con cola (BFS), y dan
resultados DISTINTOS. ¿Cuál encuentra el camino más corto? ¿Cuál usa
menos memoria? <Responde; lo confirmaremos en la semana 13.>

## Regla práctica
<Escribe en dos líneas cómo decides. Pista: pregúntate si el problema
tiene naturaleza de «retroceder» o de «hacer fila».>