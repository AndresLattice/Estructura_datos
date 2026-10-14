from simulacion import simular


def test_simulacion():
    """CA-08: la simulación devuelve media y peor espera, y repite con la misma semilla."""
    media_fifo, peor_fifo = simular(False, 42)
    media_prioridad, peor_prioridad = simular(True, 42)
    assert media_fifo >= 0
    assert peor_fifo >= media_fifo
    assert media_prioridad >= 0
    assert peor_prioridad >= media_prioridad
    assert simular(False, 42) == (media_fifo, peor_fifo)
    assert simular(True, 42) == (media_prioridad, peor_prioridad)
