import pytest
from features.steps.steps import parsear_descripcion_tiempo, parse_float

# Pruebas para "parsear_descripcion_tiempo"
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

# Pruebas para "parse_float"
def test_parse_float():
    assert parse_float("3.14") == 3.14
    assert parse_float("0") == 0.0
    assert parse_float("10") == 10.0
def test_parse_float_negativo():
    with pytest.raises(ValueError, match="No puedes comer una cantidad negativa de pepinos."):
        parse_float("-5")
def test_parse_float_StringInvalido():
    with pytest.raises(ValueError, match="No se puede convertir 'abc' a Numero Decimal."):
        parse_float("abc")
