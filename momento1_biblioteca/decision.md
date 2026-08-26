# Decision: ¿conviene mantener el catalogo ordenado?

Todos los tiempos son la mediana de 5 repeticiones de `resultados.csv`.

## Costo total por escenario

Costo = (busquedas × tiempo de busqueda) + (1 × tiempo de insertar).

- **Desordenado:** `busqueda = buscar_lineal`, `insertar = insertar_al_final`.
- **Ordenado:** `busqueda = buscar_binaria`, `insertar = insertar_ordenado`.

| n | Escenario | 5 busquedas | 50 busquedas | 300 busquedas |
|---|---|---|---|---|
| 80.000 | Desordenado | 0.019207 s | 0.192052 s | 1.152302 s |
| 80.000 | Ordenado | 0.005721 s | 0.005874 s | 0.006724 s |
| 200.000 | Desordenado | 0.046415 s | 0.464141 s | 2.784841 s |
| 200.000 | Ordenado | 0.014153 s | 0.014576 s | 0.015954 s |

(Ejemplo de calculo, 80.000, 50 busquedas, ordenado:
`50 × 0.0000034 + 0.0057039 = 0.005874` s.)

## Punto de equilibrio

Igualando los dos costos totales y despejando la cantidad de busquedas
`r` por insercion:

`r × buscar_lineal + insertar_al_final = r × buscar_binaria + insertar_ordenado`

`r = (insertar_ordenado - insertar_al_final) / (buscar_lineal - buscar_binaria)`

- n = 80.000: `r = (0.0057039 - 0.0000016) / (0.0038410 - 0.0000034) ≈ 1.49`
- n = 200.000: `r = (0.0141064 - 0.0000012) / (0.0092828 - 0.0000094) ≈ 1.52`

## Recomendacion

Con las mediciones propias, mantener el catalogo ordenado es mejor en
los tres escenarios del enunciado (5, 50 y 300 busquedas por
insercion), para 80.000 y para 200.000 registros: el costo ordenado es
entre 30 y 190 veces menor que el desordenado en esos casos.

La razon no cambia con la epoca del año en este caso: el punto de
equilibrio medido es de apenas ~1,5 busquedas por insercion (en ambos
tamanos), y el escenario mas exigente para el orden -- vacaciones, con
5 busquedas por insercion -- ya esta muy por encima de ese equilibrio.
Solo si la proporcion cayera por debajo de ~1,5 busquedas por
insercion convendria dejar el catalogo desordenado.
