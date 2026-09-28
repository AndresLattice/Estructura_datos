# Plan Técnico — Lista de reproducción

**Especificación de referencia:** `spec.md` v1.3

## 1. Estructuras elegidas

Se implementa el mismo contrato dos veces para compararlas con datos. Las dos
listas están escritas a mano, solo con clases, listas, ciclos `for` y `while`
e `if`:

- **`ListaArreglo`** (`lista_arreglo.py`, semana 4): guarda las canciones una
  junto a otra en una lista de Python de capacidad fija. Al llenarse, se copia
  a una el doble de grande. Para abrir o cerrar un hueco se mueven las
  canciones una por una con un `while`.
- **`ListaEnlazada`** (`lista_enlazada.py`, semana 6): cada canción vive en un
  nodo (`nodo.py`) que apunta al siguiente. Guarda el primer nodo (`cabeza`),
  el último (`cola`) y la cantidad. No usa `list` ni `dict` para guardar las
  canciones; solo `a_lista()` arma una lista de Python para entregarlas en orden.

La "actividad anterior" del enunciado es la `ListaArreglo` y el archivo de
pruebas `test_lista.py` de la guía de laboratorio de la semana 4. Ese contrato
y esas pruebas son la referencia de esta actividad.

Una posición inválida no lanza errores: `insertar` devuelve `False`, y
`obtener` y `eliminar` devuelven `None`. Las dos listas lo hacen igual, así
que las mismas pruebas sirven para las dos.

## 2. Alternativas descartadas

| Alternativa | Por qué se descartó |
|---|---|
| Enlazada sin `cola` | Agregar al final costaría O(n); las pruebas de casos extremos revisan la `cola` |
| Lista doblemente enlazada | Fuera de lo que pide la actividad |
| Envolver una `list` de Python | Prohibido: no sería una lista enlazada |

## 3. Complejidad esperada

`n` = canciones, `p` = posición pedida.

| Operación | Arreglo | Enlazada | Por qué |
|---|---|---|---|
| `insertar(final, x)` | O(1) amortizado | O(1) | La enlazada lo logra gracias a `cola`; sin ella sería O(n) (hay que recorrer hasta el último nodo). Es una decisión de diseño |
| `insertar(0, x)` | O(n) | O(1) | El arreglo corre todas las canciones; la enlazada solo cambia la cabeza |
| `obtener(p)` | O(1) | O(p) | El arreglo va directo; la enlazada camina p nodos |
| `eliminar(p)` | O(n) | O(p) | El arreglo cierra el hueco; la enlazada camina hasta el nodo anterior. Borrar el primero es O(1) |
| Recorrer todo | O(n) | O(n) | Las dos visitan cada canción una vez |
| `buscar(x)` | O(n) | O(n) | Se revisa una por una |
| `tamaño()` | O(1) | O(1) | Se guarda un contador |

## 4. Diseño interno

- `ListaArreglo`: `datos` (lista de Python), `capacidad` y `cantidad`.
  Siempre `0 <= cantidad <= capacidad`.
- `ListaEnlazada`: `cabeza`, `cola` y `cantidad`. Siempre:
  - la cabeza y la cola son `None` solo cuando el tamaño es 0 (IR-01);
  - la cola no tiene siguiente (IR-02);
  - caminar desde la cabeza llega a la cola en exactamente `cantidad` pasos (IR-03).

## 5. Riesgos

| Riesgo | Mitigación |
|---|---|
| Cambiar un enlace antes de guardar el siguiente nodo pierde el resto de la lista | Guardar primero el siguiente; se explica en `nodos_a_mano.md` |
| Al borrar el único elemento o el último, la cola queda apuntando a un nodo ya borrado | Pruebas CA-10 y CA-12 |
| Que una lista devuelva `None` o `False` en un caso distinto que la otra | Las dos revisan la posición con la misma condición; CA-05 y CA-08 corren con las dos |
| Medir en una posición que favorezca a una estructura | Medir `obtener` y `eliminar` en la mitad de la lista, igual en ambas |
