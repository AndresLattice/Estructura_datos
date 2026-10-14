# Plan — Sala de cómputo

**Especificación de referencia:** `spec.md` v1.1

## 1. Estructuras elegidas
- **Cola de prioridad:** nodos enlazados en orden de llegada. Al atender se busca al mejor.
- **Cola y pila:** nodos enlazados, como en clase.
- **Árbol:** cada `Carpeta` tiene `nombre`, `entregas` y una lista `hijos`.
- **Conteo y profundidad:** con recursión. Caso base: carpeta `None`.
- **Por niveles:** un `while` con la cola. `con_pila` es el mismo código con la pila.

## 2. Alternativas consideradas
| Alternativa | Ventaja | Por qué se descartó |
|---|---|---|
| Ordenar al encolar | Atender es O(1) | La efectiva cambia con el tiempo y el orden se daña |
| Una cola por nivel | Fácil de leer | Igual hay que comparar las tres para envejecer |
| `heapq` | Rápido | Prohibido por la actividad |

## 3. Complejidad
| Operación | Tiempo | Espacio | Justificación |
|---|---|---|---|
| encolar | O(1) | O(1) | Entra al final por `cola` |
| atender | O(n) | O(1) | Recorre todos para calcular la efectiva |
| contar | O(n) | O(h) | Visita cada carpeta una vez. `h` es la altura por la recursión |
| profundidad | O(n) | O(h) | Igual que contar |
| por_niveles | O(n) | O(n) | Cada carpeta entra y sale de la cola una vez |

## 4. Diseño interno
- `Nodo`: `dato`, `siguiente`.
- `ColaPrioridad`: `cabeza`, `cola`, `cantidad`. El dato es `{"nombre", "nivel", "llegada"}`.
- Al atender, solo se cambia de candidato si hay uno estrictamente menor. Así el empate lo gana el primero.
- IR-01: `cabeza` es `None` si y solo si `cola` es `None`.
- IR-02: `cantidad` es igual al número de nodos.

## 5. Árbol de prueba
```
Ingeniería (0)
├── Sistemas (0)
│   ├── Estructuras de Datos (0)
│   │   ├── 2026-1 (5)
│   │   └── 2026-2 (3)
│   └── Programación (0)
│       └── 2026-1 (4)
└── Civil (2)
```

## 6. Riesgos
| Riesgo | Impacto | Mitigación |
|---|---|---|
| Olvidar mover `cola` al sacar el último | Se pierden encolados | Prueba que saca el último y vuelve a encolar |
| Recursión sin caso base | Error al llegar a `None` | Pruebas con árbol vacío y un nodo |
| Simulación al azar | Resultados distintos cada vez | Semilla fija |
