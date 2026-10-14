# Simulación de la sala de cómputo

Ejecutar: `python simulacion.py`

## Condiciones
- Jornada de 480 minutos con un monitor.
- Cada minuto llega alguien con probabilidad 0,25.
- Nivel al azar entre 1 y 3. Atención al azar entre 2 y 6 minutos.
- Semilla 42. Los dos escenarios reciben las mismas llegadas.
- Prioridad usa envejecimiento: cada 10 minutos de espera la prioridad sube un nivel.

## Resultados (espera en minutos)
| Escenario | Nivel | Media | Peor |
|---|---|---|---|
| FIFO | 1 | 22,3 | 48 |
| FIFO | 2 | 22,4 | 51 |
| FIFO | 3 | 22,9 | 48 |
| FIFO | Todos | 22,5 | 51 |
| Prioridad | 1 | 17,6 | 47 |
| Prioridad | 2 | 22,6 | 54 |
| Prioridad | 3 | 29,5 | 52 |
| Prioridad | Todos | 23,0 | 54 |

## Análisis
- **La prioridad no reduce el trabajo, solo lo reparte.** El monitor atiende a las mismas personas. Por eso la media total casi no cambia: 22,5 contra 23,0.
- **El nivel 1 gana.** Su media baja de 22,3 a 17,6. Es justo lo que se buscaba: las entregas de hoy esperan menos.
- **El nivel 3 paga.** Su media sube de 22,9 a 29,5. Cada vez que alguien urgente se adelanta, el de uso libre espera más.
- **El peor caso empeora.** Pasa de 51 a 54. En FIFO nadie se adelanta, así que la espera depende solo de cuánta gente llegó antes. Con prioridad, a alguien le pueden pasar adelante varias veces.
- **El envejecimiento pone un límite.** Sin él, un nivel 3 podría no salir nunca. Con él, después de 30 minutos ya le gana a cualquier recién llegado. Por eso su peor espera es 52 y no crece sin control.

## Conclusión
La cola de prioridad conviene si lo importante es que las entregas de hoy salgan rápido. FIFO conviene si lo importante es que nadie espere mucho más que los demás.
