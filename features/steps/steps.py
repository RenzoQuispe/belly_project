from behave import given, when, then, register_type
import re
import random
import logging


# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    try:
        return int(palabra)
    except ValueError:
        numeros = {
            # Español
            "cero": 0, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
            "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
            "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
            "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,
            "treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60, "setenta": 70,
            "ochenta": 80, "noventa": 90, "media": 0.5,
            # Inglés
            "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
            "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
            "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
            "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "half": 0.5
        }
        return numeros.get(palabra.lower(), 0)

# Funcion para parsear texto a horas 
def parsear_descripcion_tiempo(descripcion):
    descripcion = descripcion.strip('"').lower()
    descripcion = descripcion.replace('y', ' ')
    descripcion = descripcion.replace(',', ' ')
    descripcion = descripcion.replace(';', ' ')
    descripcion = descripcion.strip()

    if descripcion in ['media hora', 'half hour']:
        return 0.5

    # 👇 Aquí agregamos una detección rápida de casos como "1.5 horas"
    horas_decimal = re.compile(r'^(\d+(?:\.\d+)?)\s*(horas?|hours?)$')
    match_decimal = horas_decimal.fullmatch(descripcion)
    if match_decimal:
        return float(match_decimal.group(1))

    # Si no es decimal simple, usar el patrón normal
    pattern = re.compile(
        r'(?:(\w+|\d+(?:\.\d+)?)\s*(?:horas?|hours?))?\s*'
        r'(?:(\w+|\d+(?:\.\d+)?)\s*(?:minutos?|minutes?))?\s*'
        r'(?:(\w+|\d+(?:\.\d+)?)\s*(?:segundos?|seconds?))?'
    )
    match = pattern.match(descripcion)

    if match:
        hours_word = match.group(1) or "0"
        minutes_word = match.group(2) or "0"
        seconds_word = match.group(3) or "0"

        hours = convertir_palabra_a_numero(hours_word)
        minutes = convertir_palabra_a_numero(minutes_word)
        seconds = convertir_palabra_a_numero(seconds_word)

        return hours + (minutes / 60) + (seconds / 3600)
    else:
        raise ValueError(f"No se pudo interpretar la descripción del tiempo: {descripcion}")
# Funcion para parsear dos numeros y devolver uno aleatorio, usa seed fija 
def tiempo_Aleatorio(inicio, fin):
    random.seed(22)  # ← SEED FIJA aquí, sin necesidad de pasarla como parámetro
    horas = random.randint(inicio, fin)
    print(f"tiempo aleatorio: {horas} horas")
    return horas

# Registrar tipo flotante para el paso
def parse_float(text):
    try:
        value = float(text)
    except ValueError:
        raise ValueError(f"No se puede convertir '{text}' a Numero Decimal.")
    
    if value < 0:
        raise ValueError("No puedes comer una cantidad negativa de pepinos.")
    if value > 1000:
        raise ValueError("La cantidad de pepino no puede ser muy grande")    
    
    return value

register_type(float=parse_float)

# Steps
@given('que he comido {cukes} pepinos')
def step_given_eaten_cukes(context, cukes):
    try:
        cukes = float(cukes)
        if cukes < 0:
            raise ValueError("Cantidad negativa de pepinos no permitida.")
        elif cukes > 1000:
            raise ValueError("Demasiados pepinos, se puede comer menos de 100")
        context.belly.comer(cukes)
        context.error = None
    except ValueError as e:
        context.error = str(e)

@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    total_time_in_hours = parsear_descripcion_tiempo(time_description)
    context.belly.esperar(total_time_in_hours)

@when('espera un tiempo aleatorio entre {inicio:d} y {fin:d} horas')
def step_when_wait_time_aleatorio(context, inicio, fin):
    tiempoAleatorio = tiempo_Aleatorio(inicio,fin)
    context.belly.esperar(tiempoAleatorio)

@when('pregunto cuántos pepinos más puedo comer')    
def pasar(context):
    pass 

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."

@then('deberia ocurrir un error de cantidad negativa.')
def step_then_error_cantidad_negativa(context):
    assert context.error is not None, "Se esperaba un error pero no ocurrió."
    assert "negativa" in context.error, f"Mensaje de error inesperado: {context.error}"

@then('deberia ocurrir un error de muchos pepinos.')
def step_then_error_muchos_pepinos(context):
    assert context.error is not None, "Se esperaba un error pero no ocurrió."
    assert "Demasiados" in context.error or "muchos" in context.error, f"Mensaje de error inesperado: {context.error}"

@then('deberia haber comido {pepinos} pepinos')
def step_cuantos_pepinos_comi(context, pepinos):
    actual = context.belly.pepinos_comidos
    assert actual == float(pepinos), f"Se esperaban {pepinos} pepinos, pero se han comido {actual}."
@then('debería decirme que puedo comer {pepinos} pepinos más')    
def cuantos_pepinos_puedo_comer_antes_de_que_el_estomago_gruña(context,pepinos):
    pepinos_puedo_comer = 10.0-float(context.belly.pepinos_comidos)
    assert float(pepinos)==pepinos_puedo_comer, f"Se esperaba que se puede comer {pepinos_puedo_comer} antes de que gruñera el estomago."    