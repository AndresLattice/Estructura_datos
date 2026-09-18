# Nodos a mano — la cadena y la pérdida de referencia

Un nodo es un par: un **dato** y una **referencia al siguiente nodo**. Aquí se
construyen sin clases ni funciones auxiliares, solo con diccionarios de Python,
para ver exactamente qué pasa con los enlaces. (Este código es una demostración
y no forma parte de `ListaEnlazada`, que no usa diccionarios.)

## 1. La cadena construida a mano

```python
n1 = {"dato": "A", "siguiente": None}
n2 = {"dato": "B", "siguiente": None}
n3 = {"dato": "C", "siguiente": None}

n1["siguiente"] = n2
n2["siguiente"] = n3
# n3["siguiente"] ya es None: marca el final

cabeza = n1

actual = cabeza
while actual is not None:
    print(actual["dato"])
    actual = actual["siguiente"]
```

Imprime `A`, `B`, `C`.

```
cabeza
  |
  v
[A | *]--->[B | *]--->[C | None]
```

El bucle empieza en `cabeza` y avanza con `actual = actual["siguiente"]`
hasta llegar a `None`. Solo se puede llegar a un nodo desde el nodo anterior:
**la única forma de encontrar B es a través del enlace de A**.

## 2. Qué pasa si se reasigna el enlace del primer nodo antes de guardar el segundo

Objetivo: insertar un nodo nuevo `X` entre `A` y `B`, para obtener `A → X → B → C`.

Aquí solo existe `cabeza` como referencia a la cadena (como en una lista real,
que solo recuerda su primer nodo):

```python
cabeza = {"dato": "A", "siguiente": {"dato": "B", "siguiente": {"dato": "C", "siguiente": None}}}
nuevo = {"dato": "X", "siguiente": None}
```

### Orden incorrecto

```python
cabeza["siguiente"] = nuevo          # 1. se reasigna el enlace de A
nuevo["siguiente"] = cabeza["siguiente"]   # 2. ¡ya no apunta a B!
```

Estado tras el paso 1:

```
cabeza
  |
  v
[A | *]--->[X | None]        [B | *]--->[C | None]
                              ^
                              |
                        nadie apunta aquí
```

`B` solo era alcanzable por el enlace de `A`. Al sobrescribirlo, `B` y `C`
quedan **sin ninguna referencia**: siguen en memoria un instante, pero el
programa ya no tiene cómo llegar a ellos (Python los libera después).

Y el paso 2 empeora el error: `cabeza["siguiente"]` ahora es `X`, así que
`X` se apunta a sí mismo:

```
cabeza
  |
  v
[A | *]--->[X | *]--+
             ^      |
             +------+
```

Recorrer esa lista ya no termina. Aun corrigiendo el paso 2 poniendo `None`,
la lista quedaría `A → X` y se habrían perdido `B` y `C`.

### Orden correcto

```python
nuevo["siguiente"] = cabeza["siguiente"]   # 1. primero se guarda B en X
cabeza["siguiente"] = nuevo                # 2. después se cambia el enlace de A
```

```
Tras el paso 1:                     Tras el paso 2:

cabeza                              cabeza
  |                                   |
  v                                   v
[A | *]--->[B | *]--->[C | None]    [A | *]--->[X | *]--->[B | *]--->[C | None]
             ^
             |
          [X | *]
```

Después del paso 1, `B` tiene dos referencias (la de `A` y la de `X`), así que
sobrescribir el enlace de `A` en el paso 2 ya no pierde nada.

## 3. La regla

> **Primero se guarda lo que se va a perder; después se sobrescribe.**
> El nodo nuevo debe apuntar al resto de la cadena **antes** de que la cadena
> existente deje de apuntar a ese resto.

Es la misma regla en todos los casos:

| Operación | Primero (guardar) | Después (reasignar) |
|---|---|---|
| Insertar en medio | `nuevo.siguiente = anterior.siguiente` | `anterior.siguiente = nuevo` |
| Insertar al principio | `nuevo.siguiente = cabeza` | `cabeza = nuevo` |
| Eliminar un nodo | leer `anterior.siguiente` para devolver su dato | `anterior.siguiente = anterior.siguiente.siguiente` |

Insertar al principio con el orden invertido (`cabeza = nuevo` primero) pierde
toda la lista, porque la cabeza era la única referencia a `A`.
