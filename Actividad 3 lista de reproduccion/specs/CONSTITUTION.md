# Constitución del proyecto — Lista de reproducción

## Principios

1. El mismo contrato se implementa dos veces: `ListaArreglo` y `ListaEnlazada`.
   Las dos pasan las mismas pruebas.
2. `ListaEnlazada` se construye con nodos propios. No usa `list`, `dict`,
   `set` ni `deque` por dentro.
3. Primero se escribe la especificación y después el código.
4. Cada operación pública tiene su complejidad en el docstring y pruebas
   de caso normal y de casos extremos.
5. La recomendación final sale de las frecuencias dadas y de tiempos
   medidos, no de suposiciones.

## Restricciones

- Python 3.11+ y pytest.
- El proyecto no depende de código de otras carpetas.
- `test_lista.py` no se modifica, salvo la lista `IMPLEMENTACIONES` que se
  amplía con `ListaEnlazada`.

## Definición de terminado

- [x] Todos los criterios de aceptación tienen prueba y pasan
- [x] Las dos listas pasan las mismas pruebas
- [x] La comparación muestra el costo teórico y el medido
- [x] `spec.md`, `plan.md` y `tasks.md` reflejan lo que realmente se hizo

## Uso de asistentes de IA

Permitido para: ayudar a redactar y organizar los documentos, las pruebas y
el código a partir de decisiones del autor.
No permitido para: entregar algo que el autor no pueda explicar.

## Cambios a la constitución

| Fecha | Cambio | Motivo |
|---|---|---|
