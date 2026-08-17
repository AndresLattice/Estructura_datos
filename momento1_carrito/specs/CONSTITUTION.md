# Constitucion del proyecto - Carrito

## Principios

1. El contrato del Carrito se implementa al menos dos veces, sobre
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
- Estructuras internas permitidas para el Carrito: list, dict (son la
  comparacion pedida por el ejercicio, no un sustituto de ella)
- Entorno: debe ejecutarse en una maquina limpia con
  `pip install pytest` y `pytest -v`

## Definicion de terminado

- [ ] Los criterios de aceptacion tienen prueba y pasan
- [ ] Las dos implementaciones pasan la misma bateria sin modificarla
- [ ] spec.md, plan.md y tasks.md reflejan el estado real

## Uso de asistentes de IA

Permitido para: redactar y estructurar spec.md, plan.md, tasks.md, las
pruebas y las implementaciones a partir de decisiones que toma el autor
del proyecto.

No permitido para: entregar codigo o decisiones que el autor no pueda
explicar en la sustentacion.
