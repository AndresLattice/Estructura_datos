# Recorridos del árbol de carpetas

Ejecutar: `python arbol_carpetas.py`

## Árbol de prueba
Entre paréntesis van las entregas de cada carpeta.

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

Para verificar a mano:
- Total de entregas: 5 + 3 + 4 + 2 = **14**.
- Profundidad máxima: **4**.
- Ruta más profunda: Ingeniería → Sistemas → Estructuras de Datos → 2026-1.

## Las dos salidas
El código es el mismo. Solo cambia `Cola` por `Pila`.

| Paso | Con cola | Con pila |
|---|---|---|
| 1 | Ingeniería | Ingeniería |
| 2 | Sistemas | Civil |
| 3 | Civil | Sistemas |
| 4 | Estructuras de Datos | Programación |
| 5 | Programación | 2026-1 |
| 6 | 2026-1 | Estructuras de Datos |
| 7 | 2026-2 | 2026-2 |
| 8 | 2026-1 | 2026-1 |

## Paso a paso
En cada vuelta se saca uno, se anota y se meten sus hijos de izquierda a derecha.

**Con cola, sale el primero que entró:**
| Sale | Entran | Cola después |
|---|---|---|
| Ingeniería | Sistemas, Civil | Sistemas, Civil |
| Sistemas | Estructuras, Programación | Civil, Estructuras, Programación |
| Civil | nada | Estructuras, Programación |
| Estructuras | 2026-1, 2026-2 | Programación, 2026-1, 2026-2 |
| Programación | 2026-1 | 2026-1, 2026-2, 2026-1 |

**Con pila, sale el último que entró:**
| Sale | Entran | Pila después, tope a la derecha |
|---|---|---|
| Ingeniería | Sistemas, Civil | Sistemas, Civil |
| Civil | nada | Sistemas |
| Sistemas | Estructuras, Programación | Estructuras, Programación |
| Programación | 2026-1 | Estructuras, 2026-1 |
| 2026-1 | nada | Estructuras |
| Estructuras | 2026-1, 2026-2 | 2026-1, 2026-2 |

## Por qué difieren
La causa es el orden en que salen los pendientes.

- **La cola** saca primero lo que entró primero. Los hijos de un nivel entran antes que los nietos, entonces se termina un nivel antes de bajar al siguiente. Eso es el recorrido por niveles.
- **La pila** saca primero lo último que entró. Apenas entran los hijos de una carpeta, se saca el último de ellos y se baja por esa rama hasta el fondo. Eso es un recorrido en profundidad.
- Además, la pila invierte el orden de los hermanos. Civil sale antes que Sistemas porque entró después.

Las dos salidas tienen las mismas 8 carpetas. Solo cambia el orden.
