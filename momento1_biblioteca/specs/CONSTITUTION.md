# Constitucion del proyecto - Catalogo de biblioteca

## Principios

1. El arreglo se implementa desde cero. No se usa `list.sort()`, `bisect`
   ni el operador `in` para buscar: es justamente lo que se reimplementa.
2. La especificacion va antes que el codigo. Si cambia el comportamiento,
   primero cambia spec.md.
3. La prediccion de complejidad (prediccion.md) se escribe y se
   commitea antes de medir nada. El commit de prediccion.md debe tener
   fecha anterior al commit de medicion.py/resultados.csv.
4. Ninguna operacion publica se considera terminada sin pruebas de caso
   normal y de casos extremos (vacia, un elemento, inicio, final).
5. Toda recomendacion en decision.md debe citar numeros propios,
   obtenidos con las mediciones de este proyecto. No se aceptan
   afirmaciones sin una cifra al lado.

## Restricciones

- Lenguaje: Python 3.11+
- Dependencias permitidas: pytest, matplotlib
- No usar `list.sort()`, `bisect`, ni `in` para buscar
- Las mediciones se repiten al menos 5 veces y se usa la mediana

## Definicion de terminado

- [ ] Los criterios de aceptacion tienen prueba y pasan
- [ ] La complejidad real coincide con la declarada en plan.md/prediccion.md
- [ ] spec.md, plan.md y tasks.md reflejan el estado real
- [ ] decision.md cita numeros propios de resultados.csv

## Uso de asistentes de IA

Permitido para: redactar explicaciones, y ayudar a estructurar archivos
como CONSTITUTION.md, spec.md, plan.md, tasks.md, las pruebas y las
implementaciones a partir de decisiones que toma el autor (Yo) del
proyecto. Tambien se uso para verificar que la estructura general del
proyecto se alineara con la metodologia SDD, y para entender las
alternativas de diseño antes de decidir cual usar.

No permitido para: tomar decisiones de diseño completamente de manera
autonoma sin autorizacion.
