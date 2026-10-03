# Plan

## Estructura
Lista enlazada ordenada por prioridad. El más urgente está en `cabeza`.

```
cabeza                            cola
  v                                 v
[1, Ana] -> [2, Luis] -> [4, Juan] -> None
```

- `Nodo`: `dato`, `prioridad`, `siguiente`.
- `ColaPrioridad`: `cabeza`, `cola`, `cantidad`.

Se ordena al encolar. Así ver el siguiente y atender son O(1).

## Encolar
1. Vacía: el nuevo es cabeza y cola.
2. Más urgente que la cabeza: entra de primero.
3. Igual o menos urgente que la cola: entra de último. Así se respeta la llegada.
4. En el medio: primero el nuevo apunta al siguiente, luego el anterior apunta al nuevo.

## Complejidad
| Operación | Costo |
|---|---|
| encolar | O(n) |
| desencolar | O(1) |
| frente | O(1) |
| retirar_turno | O(n) |
| buscar_documento | O(n) |
| tamaño | O(1) |

## API
| Operación | Método | Ruta |
|---|---|---|
| Registrar | POST | `/pacientes` |
| Ver fila | GET | `/cola` |
| Ver siguiente | GET | `/cola/siguiente` |
| Atender | POST | `/cola/atender` |
| Retirar | DELETE | `/pacientes/{turno}` |
| Cuántos faltan | GET | `/cola/estado` |

## Archivos
- `nodo.py`: clase `Nodo`.
- `cola_prioridad.py`: clase `ColaPrioridad`.
- `urgencias.py`: lógica del hospital.
- `main.py`: rutas de la API.
- `test_cola_prioridad.py` y `test_urgencias.py`: pruebas.

## Cómo correrlo
```bash
pip install fastapi uvicorn pytest
pytest -v
uvicorn main:app --reload
```
