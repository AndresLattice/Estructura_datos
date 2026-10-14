# Constitución del proyecto — Sala de cómputo

## Misión
Software para la sala de cómputo. Atiende turnos por prioridad sin dejar a nadie esperando para siempre. Además responde preguntas sobre el árbol de carpetas de entregas.

## Principios

1. Primero se escribe la especificación y después el código. Si cambia el
   comportamiento, primero cambia el `spec.md`.
2. Toda estructura se construye desde cero con nodos propios. No se usa
   `heapq` ni `collections.deque`.
3. El conteo de entregas y la profundidad máxima se hacen con recursión,
   con un caso base claro.
4. El listado por niveles se hace sin recursión, con un `while` y la cola propia.
5. Cada operación pública tiene su complejidad en el docstring y pruebas
   de caso normal y de casos extremos.
6. Las conclusiones de la simulación salen de los datos medidos, no de
   suposiciones.

## Restricciones

- Python 3.11+ y pytest.
- El proyecto no depende de código de otras carpetas.
- El código usa solo lo visto en clase: clases, listas, ciclos `for` y
  `while`, `if` y recursión.
- Si una cola o pila está vacía, se devuelve `None`. Un dato inválido
  devuelve `False`. No se lanzan excepciones.

## Definición de terminado

- [x] Todos los criterios de aceptación tienen prueba y pasan
- [x] El mecanismo contra la espera indefinida se demuestra con una prueba
- [x] La tabla de la simulación muestra media y peor espera en los dos escenarios
- [x] `recorridos.md` muestra la salida con cola y con pila sobre el mismo árbol
- [x] El árbol de prueba está dibujado para verificar a mano
- [ ] `pytest` pasa en una máquina limpia
- [x] `spec.md`, `plan.md` y `tasks.md` reflejan lo que realmente se hizo

## Uso de asistentes de IA

Permitido para: ayudar a redactar y organizar los documentos, las pruebas y
el código a partir de decisiones del autor.
No permitido para: entregar algo que el autor no pueda explicar.
Todo aporte de IA se revisa contra la especificación antes de integrarse.
