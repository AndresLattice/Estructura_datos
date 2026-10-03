# Constitución

## Misión
API para la fila de urgencias de un hospital. Se atiende por nivel de triage y, con igual nivel, por llegada.

## Reglas
1. La fila usa una `ColaPrioridad` propia hecha con nodos.
2. No se usa `list`, `dict`, `deque` ni `heapq` para guardar pacientes.
3. Triage del 1 al 5, según la Resolución 5596 de 2015. El 1 es el más urgente.
4. Solo se usa lo visto en clase.
5. Cada criterio de aceptación tiene una prueba.
