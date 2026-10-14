import random
from cola import Cola
from cola_prioridad import ColaPrioridad

MINUTOS = 480            # jornada de 8 horas
PROB_LLEGADA = 0.25      # probabilidad de que llegue alguien cada minuto


def crear_llegadas(semilla):
    """Lista de llegadas: [minuto, nivel, minutos_de_atencion]."""
    random.seed(semilla)
    llegadas = []
    for minuto in range(MINUTOS):
        if random.random() < PROB_LLEGADA:
            nivel = random.randint(1, 3)
            atencion = random.randint(2, 6)
            llegadas.append([minuto, nivel, atencion])
    return llegadas


def correr(usar_prioridad, semilla):
    """Simula la jornada con un monitor. Devuelve una lista de [nivel, espera]."""
    llegadas = crear_llegadas(semilla)
    if usar_prioridad:
        fila = ColaPrioridad()
    else:
        fila = Cola()

    resultados = []
    libre_en = 0     # minuto en que el monitor queda libre
    siguiente = 0    # posición de la próxima llegada
    minuto = 0

    while siguiente < len(llegadas) or not fila.esta_vacia():
        # Entran a la fila los que llegan en este minuto.
        # El nombre del estudiante es su posición en la lista de llegadas.
        while siguiente < len(llegadas) and llegadas[siguiente][0] == minuto:
            nivel = llegadas[siguiente][1]
            if usar_prioridad:
                fila.encolar(siguiente, nivel, minuto)
            else:
                fila.encolar({"nombre": siguiente, "nivel": nivel, "llegada": minuto})
            siguiente = siguiente + 1

        # Si el monitor está libre, atiende al que sigue.
        if libre_en <= minuto and not fila.esta_vacia():
            if usar_prioridad:
                estudiante = fila.atender(minuto)
            else:
                estudiante = fila.desencolar()
            espera = minuto - estudiante["llegada"]
            resultados.append([estudiante["nivel"], espera])
            atencion = llegadas[estudiante["nombre"]][2]
            libre_en = minuto + atencion

        minuto = minuto + 1
    return resultados


def media_y_peor(resultados, nivel):
    """(media, peor) de la espera. Con nivel 0 se toman todos los niveles."""
    suma = 0
    cuantos = 0
    peor = 0
    for fila in resultados:
        if nivel == 0 or fila[0] == nivel:
            suma = suma + fila[1]
            cuantos = cuantos + 1
            if fila[1] > peor:
                peor = fila[1]
    if cuantos == 0:
        return 0, 0
    return round(suma / cuantos, 1), peor


def simular(usar_prioridad, semilla):
    """Devuelve (media, peor) de la espera en minutos, de todos los estudiantes."""
    return media_y_peor(correr(usar_prioridad, semilla), 0)


# Ejecutar: python simulacion.py
print("Escenario, nivel, media, peor")
for usar_prioridad in [False, True]:
    resultados = correr(usar_prioridad, 42)
    for nivel in [1, 2, 3, 0]:
        media, peor = media_y_peor(resultados, nivel)
        if usar_prioridad:
            escenario = "Prioridad"
        else:
            escenario = "FIFO"
        if nivel == 0:
            print(escenario, "todos", media, peor)
        else:
            print(escenario, nivel, media, peor)
