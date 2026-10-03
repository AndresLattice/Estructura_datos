# Especificación

## Objetivo
En urgencias no se atiende por llegada. Se atiende primero al más grave. La API guarda la fila y dice quién sigue.

## Sistema de atención
1. Triage le asigna un nivel al paciente.
2. Se registra y recibe un turno, por ejemplo `U-7`.
3. El médico atiende al siguiente.
4. Si el paciente se va, se saca de la fila.

## Reglas de priorización
| Nivel | Situación | Tiempo |
|---|---|---|
| 1 | Riesgo vital | Inmediato |
| 2 | Puede empeorar rápido | 30 minutos |
| 3 | Necesita tratamiento en urgencias | Lo define el hospital |
| 4 | Puede complicarse | Lo define el hospital |
| 5 | Sin riesgo | Lo define el hospital |

- Sale primero el nivel más bajo.
- Con igual nivel, sale quien llegó antes.
- Un documento no puede estar dos veces en la fila.

## Historias de usuario
- **HU-01:** Como enfermera, quiero registrar pacientes, para ubicarlos según su gravedad. *CA-15 a CA-18*
- **HU-02:** Como médico, quiero ver quién sigue, para prepararme. *CA-19, CA-20*
- **HU-03:** Como médico, quiero atender al siguiente, para atender primero al más grave. *CA-21, CA-22*
- **HU-04:** Como admisión, quiero sacar a un paciente, para que la fila esté al día. *CA-23, CA-24*
- **HU-05:** Como coordinador, quiero ver cuántos faltan, para asignar médicos. *CA-25, CA-26*

## Requisitos funcionales
- **RF-01:** CUANDO se registre un paciente, EL SISTEMA DEBE darle un turno y ubicarlo por nivel.
- **RF-02:** SI el nivel no está entre 1 y 5, EL SISTEMA DEBE rechazarlo.
- **RF-03:** SI el documento ya está en espera, EL SISTEMA DEBE rechazarlo.
- **RF-04:** EL SISTEMA DEBE atender primero el nivel más bajo y, con igual nivel, al que llegó antes.
- **RF-05:** CUANDO se consulte el siguiente, EL SISTEMA DEBE mostrarlo sin sacarlo.
- **RF-06:** CUANDO se atienda, EL SISTEMA DEBE sacar al siguiente.
- **RF-07:** CUANDO se retire un turno, EL SISTEMA DEBE sacarlo sin cambiar el orden de los demás.
- **RF-08:** CUANDO se consulte el estado, EL SISTEMA DEBE mostrar el total, el conteo por nivel y los atendidos.
- **RF-09:** SI la fila está vacía o el turno no existe, EL SISTEMA DEBE devolver un error.

## Requisitos no funcionales
- **RNF-01:** La fila se hace con nodos propios.
- **RNF-02:** Ver el siguiente y atender son O(1).
- **RNF-03:** GET para leer, POST para crear o actuar, DELETE para quitar.
- **RNF-04:** Los errores son `{"error": "..."}` en español.

## Criterios de aceptación
| ID | Criterio | Prueba |
|---|---|---|
| CA-01 | Cola nueva vacía | `test_cola_nueva_vacia` |
| CA-02 | Sale primero la menor prioridad | `test_orden_por_prioridad` |
| CA-03 | Con empate sale el primero en llegar | `test_empate_es_fifo` |
| CA-04 | Cola vacía devuelve `None` | `test_vacia_devuelve_none` |
| CA-05 | `frente` no saca | `test_frente_no_modifica` |
| CA-06 | Un solo elemento entra y sale bien | `test_un_elemento_entra_y_sale` |
| CA-07 | El más urgente queda de primero | `test_mas_urgente_pasa_a_cabeza` |
| CA-08 | El menos urgente queda de último | `test_menos_urgente_actualiza_cola` |
| CA-09 | Retirar el primero | `test_retirar_cabeza` |
| CA-10 | Retirar el último | `test_retirar_ultimo_actualiza_cola` |
| CA-11 | Retirar del medio | `test_retirar_del_medio_conserva_orden` |
| CA-12 | Retirar uno que no está | `test_retirar_inexistente_devuelve_none` |
| CA-13 | Buscar por documento | `test_buscar_documento` |
| CA-14 | Varias operaciones seguidas | `test_operaciones_mezcladas` |
| CA-15 | Registrar paciente | `test_registrar_paciente` |
| CA-16 | Nivel inválido | `test_registrar_nivel_invalido` |
| CA-17 | Documento repetido | `test_registrar_documento_duplicado` |
| CA-18 | Volver después de atendido | `test_documento_puede_volver_tras_atencion` |
| CA-19 | Ver siguiente sin sacarlo | `test_siguiente_no_modifica` |
| CA-20 | Ver siguiente con fila vacía | `test_siguiente_cola_vacia` |
| CA-21 | Atender en orden | `test_atender_respeta_prioridad_y_llegada` |
| CA-22 | Atender con fila vacía | `test_atender_cola_vacia` |
| CA-23 | Retirar por turno | `test_retirar_paciente` |
| CA-24 | Retirar turno que no existe | `test_retirar_inexistente` |
| CA-25 | Conteo por nivel | `test_estado_conteo` |
| CA-26 | Fila en orden | `test_fila_en_orden` |

## Fuera de alcance
- Base de datos.
- Usuarios y contraseñas.
- Códigos HTTP de error como 404.
