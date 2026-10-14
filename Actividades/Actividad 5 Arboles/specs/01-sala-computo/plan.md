# Plan

## Cola de prioridad
- Estudiante: `{"nombre", "nivel", "llegada"}`.
- Encolar pone al estudiante al final. O(1).
- Atender recorre los nodos y saca al de menor efectiva. O(n).
- Solo cambia de candidato si encuentra uno menor. Así el empate lo gana quien llegó antes.

## Simulación
- Un monitor. Llegadas al azar con semilla fija.
- Los dos escenarios usan las mismas llegadas: `Cola` contra `ColaPrioridad`.

## Árbol de prueba
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

- `Carpeta`: `nombre`, `entregas` y lista `hijos`.
- `contar` y `profundidad`: recursivas. Caso base `None` da 0.
- `por_niveles`: `while` con `Cola`. `con_pila`: el mismo código con `Pila`.
- Todas son O(n).

## Archivos
- `nodo.py`, `cola.py`, `pila.py`, `cola_prioridad.py`.
- `simulacion.py` y `simulacion.md`.
- `arbol_carpetas.py` y `recorridos.md`.
- `test_*.py`.
