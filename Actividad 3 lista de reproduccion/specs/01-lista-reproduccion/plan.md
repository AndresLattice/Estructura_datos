# Plan Técnico — Lista de reproducción

**Especificación de referencia:** `spec.md` v1.1

## 1. Estructuras elegidas

Se implementa el mismo contrato dos veces para compararlas con datos. Se parte
del código base del curso, copiado en esta carpeta y completado:

- **`ListaArreglo`** (`lista_arreglo.py`, semana 4): guarda las canciones una
  junto a otra en una lista de Python de capacidad fija. Al llenarse, se copia
  a una el doble de grande.
- **`ListaEnlazada`** (`lista_enlazada.py`, semana 6): cada canción vive en un
  nodo (`nodo.py`, semana 5) que apunta al siguiente. Guarda el primer nodo
  (`_cabeza`), el último (`_cola`) y el tamaño. No usa `list` ni `dict`.

`PosicionInvalidaError` se define una sola vez, en `lista_arreglo.py`, y la
lista enlazada lo importa. Así `test_lista.py` reconoce el mismo error en las
dos listas.

## 2. Alternativas descartadas

| Alternativa | Por qué se descartó |
|---|---|
| Enlazada sin `_cola` | El código base y sus pruebas de casos extremos la usan; además agregar al final costaría O(n) |
| Lista doblemente enlazada | Fuera de lo que pide la actividad |
| Envolver una `list` de Python | Prohibido: no sería una lista enlazada |

## 3. Complejidad esperada

`n` = canciones, `p` = posición pedida.

| Operación | Arreglo | Enlazada | Por qué |
|---|---|---|---|
| `insertar(0, x)` | O(n) | O(1) | El arreglo corre todas las canciones; la enlazada solo cambia la cabeza |
| `obtener(p)` | O(1) | O(p) | El arreglo va directo; la enlazada camina p nodos |
| `eliminar(p)` | O(n) | O(p) | El arreglo cierra el hueco; la enlazada camina hasta el nodo anterior. Borrar el primero es O(1) |
| Recorrer todo | O(n) | O(n) | Las dos visitan cada canción una vez |
| `buscar(x)` | O(n) | O(n) | Se revisa una por una |
| `tamaño()` | O(1) | O(1) | Se guarda un contador |

## 4. Diseño interno

- `ListaArreglo`: `_datos` (lista de Python), `_capacidad` y `_tamaño`.
  Siempre `0 <= _tamaño <= _capacidad`.
- `ListaEnlazada`: `_cabeza`, `_cola` y `_tamaño`. Siempre:
  - la cabeza y la cola son `None` solo cuando el tamaño es 0 (IR-01);
  - la cola no tiene siguiente (IR-02);
  - caminar desde la cabeza llega a la cola en exactamente `_tamaño` pasos (IR-03).

## 5. Riesgos

| Riesgo | Mitigación |
|---|---|
| Cambiar un enlace antes de guardar el siguiente nodo pierde el resto de la lista | Guardar primero el siguiente; se explica en `nodos_a_mano.md` |
| Al borrar el único elemento o el último, la cola queda apuntando a un nodo ya borrado | Pruebas CA-10 y CA-12 |
| Cada archivo del curso define su propio `PosicionInvalidaError`; las pruebas no reconocerían el de la enlazada | Definirlo solo en `lista_arreglo.py` e importarlo. Si `test_lista.py` fallara, el defecto sería de la implementación, no del contrato |
| Medir en una posición que favorezca a una estructura | Medir `obtener` y `eliminar` en la mitad de la lista, igual en ambas |
