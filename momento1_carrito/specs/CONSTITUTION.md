# Constitucion del proyecto - Carrito

## Principios

1. El contrato del carrito se implementa al menos dos veces, sobre
   estructuras internas distintas, y una unica bateria de pruebas
   verifica ambas sin modificarse.
2. No se usa collections.Counter como sustituto del conteo de cantidades.
3. La especificacion va antes que el codigo. Si cambia el comportamiento,
   primero cambia spec.md.
4. Ninguna operacion publica se considera terminada sin pruebas de caso
   normal y de casos extremos pasando.

## Restricciones

- Lenguaje: Python 3.11+
- Dependencias permitidas: pytest
- Estructuras internas permitidas para el Carrito: list, dict

## Definicion de terminado

- [x] Los criterios de aceptacion tienen prueba y pasan
- [x] Las dos implementaciones pasan la misma bateria sin modificarla
- [x] spec.md, plan.md y tasks.md reflejan el estado real

## Uso de asistentes de IA

Permitido para: redactar explicaciones, y ayudar a estructurar archivos como CONSTITUTION.md, spec.md, plan.md, tasks.md, las pruebas y las implementaciones a partir de decisiones que toma el autor (Yo) del proyecto.
Tambien se uso para verificar que la estructura general del proyecto se alineara con la metodologia SDD, y para entender las alternativas de diseno antes de decidir cual usar.

No permitido para: Tomar decisiones completamente de manera autonoma sin autorizacion
