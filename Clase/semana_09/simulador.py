# Código base — Semana 09
# Fuente: 02-Momento-2-Disciplina-y-jerarquia/09-Semana-09-Colas/02-guia-de-laboratorio.html

import random
from cola import ColaEnlazada


class Cliente:
    def __init__(self, id_cliente, minuto_llegada, minutos_atencion):
        self.id = id_cliente
        self.llegada = minuto_llegada
        self.atencion = minutos_atencion
        self.inicio_servicio = None

    @property
    def espera(self):
        return self.inicio_servicio - self.llegada


def simular(minutos, num_servidores, prob_llegada=0.5, semilla=42):
    """Simula una atención en ventanilla minuto a minuto.

    Devuelve (espera_promedio, espera_maxima, atendidos, en_cola_al_final).
    """
    random.seed(semilla)
    cola = ColaEnlazada()
    servidores = [None] * num_servidores      # minuto en que se libera cada uno
    libre_en = [0] * num_servidores
    atendidos = []
    siguiente_id = 1

    for minuto in range(minutos):
        # ¿Llega alguien este minuto?
        if random.random() < prob_llegada:
            cola.encolar(Cliente(siguiente_id, minuto, random.randint(2, 8)))
            siguiente_id += 1

        # ¿Hay servidores libres para atender?
        for s in range(num_servidores):
            if libre_en[s] <= minuto and not cola.esta_vacia():
                cliente = cola.desencolar()
                cliente.inicio_servicio = minuto
                libre_en[s] = minuto + cliente.atencion
                atendidos.append(cliente)

    esperas = [c.espera for c in atendidos]
    promedio = sum(esperas) / len(esperas) if esperas else 0
    return promedio, max(esperas, default=0), len(atendidos), len(cola)


print(f"{'Servidores':>10} {'Espera prom.':>13} {'Espera máx.':>12} "
      f"{'Atendidos':>10} {'En cola':>8}")
for n in [1, 2, 3, 4]:
    prom, maxima, atendidos, en_cola = simular(480, n)   # jornada de 8 horas
    print(f"{n:>10} {prom:>12.1f}m {maxima:>11}m {atendidos:>10} {en_cola:>8}")

# Preguntas para el análisis:
#   1. ¿La espera promedio se reduce a la mitad al duplicar los servidores?
#   2. ¿Hay un punto donde agregar servidores ya no mejora nada? ¿Por qué?
#   3. ¿Qué pasa si prob_llegada = 0.9? ¿Y si es 0.1?
