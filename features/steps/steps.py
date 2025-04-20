from behave import given, when, then, register_type
import re

# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    try:
        return int(palabra)
    except ValueError:
        numeros = {
            "cero": 0, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
            "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
            "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
            "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,
            "treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60, "setenta": 70,
            "ochenta": 80, "noventa": 90, "media": 0.5
        }
        return numeros.get(palabra.lower(), 0)

# Funcion para parsear texto a horas 
def parsear_descripcion_tiempo(descripcion):
    descripcion = descripcion.strip('"').lower()
    descripcion = descripcion.replace('y', ' ')
    descripcion = descripcion.strip()

    if descripcion == 'media hora':
        return 0.5

    pattern = re.compile(
        r'(?:(\w+|\d+(?:\.\d+)?)\s*horas?)?\s*'
        r'(?:(\w+|\d+(?:\.\d+)?)\s*minutos?)?\s*'
        r'(?:(\w+|\d+(?:\.\d+)?)\s*segundos?)?'
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

# Registrar tipo flotante para el paso
def parse_float(text):
    try:
        value = float(text)
        if value < 0:
            raise ValueError("No puedes comer una cantidad negativa de pepinos.")
        return value
    except ValueError:
        raise ValueError(f"No se puede convertir '{text}' a Numero Decimal.")

register_type(float=parse_float)

# Steps
@given('que he comido {cukes:float} pepinos')
def step_given_eaten_cukes(context, cukes):
    context.belly.comer(cukes)

@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    total_time_in_hours = parsear_descripcion_tiempo(time_description)
    context.belly.esperar(total_time_in_hours)

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."
