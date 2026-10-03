# Autopsia: dos cajas comparten el mismo carrito

> **Nota:** Hice uso de la IA (Claude) para ayudarme en la redaccion y organizacion 
> de este archivo. no se conto con el fragmento de codigo real del profesor.
> El codigo de abajo es un fragmento representativo del bug clasico de
> alias en Python (Idea de Claude)(una caja registradora que hereda el carrito de otra
> por compartir el mismo objeto lista). La causa raiz de este tipo de
> bug es siempre la misma: una referencia compartida.

## El fragmento con el bug

```python
class Caja:
    def __init__(self, carrito=[]):
        self.carrito = carrito

    def agregar(self, producto, cantidad):
        self.carrito.append((producto, cantidad))


caja1 = Caja()
caja2 = Caja()

caja1.agregar("manzana", 3)

print(caja2.carrito)
```

## Diagnostico

La causa no es una copia mal hecha. Es que `caja1.carrito` y
`caja2.carrito` nunca fueron dos listas: son dos nombres distintos que
apuntan al mismo objeto lista en memoria.

Esto pasa por el error clasico del argumento por defecto mutable:
`def __init__(self, carrito=[])` evalua la lista `[]` una sola vez, en
el momento en que se define la funcion `__init__`, no cada vez que se
llama. Esa unica lista queda guardada como el valor por defecto del
parametro `carrito` para siempre. Como `caja1 = Caja()` y
`caja2 = Caja()` no pasan un argumento explicito, ambas llamadas reciben
la misma lista por defecto, y `self.carrito = carrito` hace que
`caja1.carrito` y `caja2.carrito` sean dos referencias a ese unico
objeto.

Cuando `caja1.agregar(...)` hace `self.carrito.append(...)`, no crea una
lista nueva: muta el objeto lista compartido. Como `caja2.carrito`
apunta al mismo objeto, el cambio es visible tambien desde `caja2`,
aunque nadie le haya pedido nada a `caja2`.

Diferencia entre mutar y reasignar:
- `self.carrito.append(x)` muta el objeto al que apunta `self.carrito`.
  Todo el que tenga una referencia a ese mismo objeto ve el cambio.
- `self.carrito = self.carrito + [x]` reasigna `self.carrito` a un
  objeto lista nuevo. Otras referencias que apunten al objeto viejo no
  ven el cambio.

## Diagrama de memoria - ANTES de `caja1.agregar("manzana", 3)`

```
Variables/atributos                Objetos en memoria

caja1  ---------> [Caja @0x100] ---.
                                     \
                                      +--> carrito ---> [ ] (lista vacia @0x200)
                                     /
caja2  ---------> [Caja @0x101] ---'
```

`caja1.carrito` y `caja2.carrito` son dos flechas distintas que apuntan
al mismo objeto lista `@0x200`. Solo existe una lista en memoria.

## Diagrama de memoria - DESPUES de `caja1.agregar("manzana", 3)`

```
Variables/atributos                Objetos en memoria

caja1  ---------> [Caja @0x100] ---.
                                     \
                                      +--> carrito ---> [("manzana", 3)]  (@0x200, MUTADA)
                                     /
caja2  ---------> [Caja @0x101] ---'
```

El objeto `@0x200` sigue siendo el mismo (misma direccion), pero ahora
tiene un elemento adentro. Como `caja2.carrito` sigue apuntando a
`@0x200`, `caja2.carrito` tambien "tiene" la manzana, sin que nadie se
la haya agregado directamente a `caja2`.

## La correccion

```python
class Caja:
    def __init__(self, carrito=None):
        self.carrito = carrito if carrito is not None else []

    def agregar(self, producto, cantidad):
        self.carrito.append((producto, cantidad))


caja1 = Caja()
caja2 = Caja()

caja1.agregar("manzana", 3)

print(caja2.carrito)
```

### Por que funciona, en terminos de memoria

El valor por defecto ya no es un objeto mutable compartido: es `None`,
que es inmutable y no representa ningun estado que se pueda alterar por
accidente. La linea `self.carrito = carrito if carrito is not None else []`
se ejecuta cada vez que se llama a `__init__`, asi que cada instancia
sin argumento explicito recibe una lista nueva y propia.

```
caja1  ---------> [Caja @0x100] --> carrito ---> [ ] (lista @0x300, propia de caja1)

caja2  ---------> [Caja @0x101] --> carrito ---> [ ] (lista @0x301, propia de caja2)
```

Ahora `caja1.carrito` y `caja2.carrito` apuntan a objetos distintos.
Mutar uno con `.append(...)` no afecta al otro, porque ya no hay alias
entre ellos.

Esta es la misma razon, vista desde la memoria, por la que el TAD
Carrito de este proyecto (`carrito_lista.py`, `carrito_dict.py`) nunca
comparte su lista o diccionario interno con nadie desde afuera: cada
`Carrito()` crea su propia estructura en `__init__`
(`self._items = []` / `self._cantidades = {}`), evitando que dos
instancias terminen apuntando, sin querer, al mismo objeto.
