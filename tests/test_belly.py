import pytest
from features.steps.steps import parsear_descripcion_tiempo, parse_float, tiempo_Aleatorio
import logging
import time
from src.belly import Belly 
from unittest.mock import MagicMock

def test_belly_with_mocked_clock():
    # Creamos un reloj simulado que siempre devolverá el mismo valor
    clock = MagicMock()
    clock.return_value = 10000  # Valor fijo para el tiempo

    belly = Belly(clock_service=clock)
    belly.comer(15)  # Comemos 15 pepinos
    belly.esperar(2)  # Esperamos 2 horas

    assert belly.pepinos_comidos == 15
    assert belly.esta_gruñendo() 

# Test predecir Gruñido - Problema12
def test_estomago_predecir_gruñido():
    belly = Belly()
    belly.comer(12)
    belly.esperar(1.5)
    assert belly.esta_gruñendo() == True
# test gruñir
def test_gruñir():
    belly = Belly()
    belly.comer(15)
    belly.esperar(2)
    print(f"Comer 15 pepino y esperamos 2 horas. Esta gruñendo: {belly.esta_gruñendo()}")
    assert belly.esta_gruñendo() == True

# Pruebas para "parsear_descripcion_tiempo"
def test_parsear_descripcion_tiempo():
    assert parsear_descripcion_tiempo("1 hora, 30 minutos y 45 segundos") == 1.5125
    assert parsear_descripcion_tiempo("1 hora ; 30 minutos ; 45 segundos") == 1.5125
    assert parsear_descripcion_tiempo("2 hora") == 2.0
    assert parsear_descripcion_tiempo("media hora") == 0.5
    assert parsear_descripcion_tiempo("una hora") == 1.0
    assert parsear_descripcion_tiempo("dos horas") == 2.0
    assert parsear_descripcion_tiempo("1 hora 30 minutos") == 1.5
    assert parsear_descripcion_tiempo("1 hora y 3600 segundos") == 2.0
    assert parsear_descripcion_tiempo("30 minutos") == 0.5
    assert parsear_descripcion_tiempo("90 minutos") == 1.5
    assert parsear_descripcion_tiempo("1 hora 45 segundos") == 1.0125

# Pruebas para "parse_float"
def test_parse_float():
    assert parse_float("3.14") == 3.14
    assert parse_float("0") == 0.0
    assert parse_float("10") == 10.0
def test_parse_float_negativo():
    with pytest.raises(ValueError, match="No puedes comer una cantidad negativa de pepinos."):
        parse_float("-5")
    with pytest.raises(ValueError, match="No puedes comer una cantidad negativa de pepinos."):
        parse_float("-10.5")    
def test_parse_float_StringInvalido():
    with pytest.raises(ValueError, match="No se puede convertir 'abc' a Numero Decimal."):
        parse_float("abc")

# Prueba para "tiempo_Aleatorio" - usamos seed fija(22)
def test_tiempo_aleatorio():
    print(f"test_tiempo_aleatorio:")
    assert tiempo_Aleatorio(1,2) == 1
    assert tiempo_Aleatorio(0,8) == 2
    assert tiempo_Aleatorio(3,10) == 5
    assert tiempo_Aleatorio(0,2) == 0

# Prueba para medir el tiempo de ejecución de comer 1000 pepinos y esperar 10 horas
def test_escenario_tiempo_ejecucion():
    belly = Belly()

    tiempoInicio = time.time()  

    belly.comer(1000)  
    belly.esperar(10)  

    tiempoFinal = time.time()  
    tiempoEjecucion = tiempoFinal - tiempoInicio  

    print(f"test_escenario_tiempo_ejecucion Tiempo de ejecución: {tiempoEjecucion} segundos")

    # Verificamos que el tiempo de ejecución es menor a 1 segundo
    assert tiempoEjecucion < 1, f"El tiempo de ejecución es demasiado largo: {tiempoEjecucion} segundos"

# Test ejercicio10
def test_pepinos_restantes():
    belly = Belly()
    belly.comer(15)
    assert belly.pepinos_comidos == 15    



