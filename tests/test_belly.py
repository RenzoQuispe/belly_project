import pytest
from features.steps.steps import parsear_descripcion_tiempo

@pytest.mark.parametrize("descripcion, valorEsperado", [
    ("1 hora", 1.0),
    ("media hora", 0.5),
    ("una hora", 1.0),
    ("dos horas", 2.0),
    ("1 hora 30 minutos", 1.5),
    ("1 hora y 3600 segundos", 2.0),
    ("30 minutos", 0.5),
    ("90 minutos", 1.5),
    ("1 hora 45 segundos", 1.0125),
])
def test_parsear_descripcion_tiempo(descripcion, valorEsperado):
    resultado = parsear_descripcion_tiempo(descripcion)
    assert resultado == valorEsperado