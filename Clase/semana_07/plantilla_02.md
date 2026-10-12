# Tabla de decisión: ¿qué variante de lista usar?

## Comparación de complejidad
| Operación               | Arreglo | Simple | Doble | Circular |
|-------------------------|---------|--------|-------|----------|
| obtener(i)              | O(1)    | O(n)   | O(n)  | O(n)     |
| insertar al inicio      | O(n)    | O(1)   | O(1)  | O(1)     |
| insertar al final       | O(1)*   | O(1)** | O(1)  | O(1)     |
| eliminar al inicio      | O(n)    | O(1)   | O(1)  | O(n)     |
| eliminar al final       | O(1)    | O(n)   | O(1)  | O(n)     |
| eliminar nodo conocido  | O(n)    | O(n)   | O(1)  | O(n)     |
| recorrido inverso       | O(n)    | imposible | O(n) | imposible |
| memoria por elemento    | 1 ref   | 2 ref  | 3 ref | 2 ref    |

*  amortizado   ** con referencia a la cola

## Seis casos de uso: elige y justifica
| # | Caso de uso | Variante | Por qué |
|---|-------------|----------|---------|
| 1 | Historial del navegador con botones atrás y adelante | | |
| 2 | Cola de impresión: entra al final, sale del inicio | | |
| 3 | Catálogo de 10.000 productos que se consulta por índice y casi nunca cambia | | |
| 4 | Turnos de jugadores en una partida por rondas | | |
| 5 | Lista de reproducción con repetición infinita | | |
| 6 | Editor de texto con deshacer y rehacer ilimitados | | |

## Conclusión
<Tres líneas: cuál es el criterio general para elegir. Pista: no depende
de la estructura, depende de QUÉ OPERACIÓN vas a hacer con más frecuencia.>