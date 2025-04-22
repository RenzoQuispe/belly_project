# language: es
Característica: Característica del estómago

  @español
  Escenario: Manejar tiempos complejos
    Dado que he comido 50 pepinos
    Cuando espero "1 hora, 30 minutos y 45 segundos"
    Entonces mi estómago debería gruñir
  @español
  Escenario: Manejar tiempos complejos
    Dado que he comido 20 pepinos
    Cuando espero "1 hora ; 30 minutos ; 1 segundos"
    Entonces mi estómago debería gruñir

  @español
  Escenario: Comer 1000 pepinos y esperar 10 horas
    Dado que he comido 1000 pepinos
    Cuando espero 10 horas
    Entonces mi estómago debería gruñir

  @español
  Escenario: Manejar una cantidad negativa de pepinos 
    Dado que he comido -5 pepinos
    Entonces deberia ocurrir un error de cantidad negativa.
  @español
  Escenario: Manejar una cantidad mayor a 100 de pepinos
    Dado que he comido 1200 pepinos
    Entonces deberia ocurrir un error de muchos pepinos.

  @español
  Escenario: Comer pepinos y esperar un tiempo aleatorio
    Dado que he comido 25 pepinos
    Cuando espera un tiempo aleatorio entre 1 y 2 horas
    Entonces mi estómago no debería gruñir
  @español
  Escenario: Comer pepinos y esperar un tiempo aleatorio
    Dado que he comido 25 pepinos
    Cuando espera un tiempo aleatorio entre 0 y 8 horas
    Entonces mi estómago debería gruñir

  @ingles
  Escenario: Esperar usando horas en inglés
    Dado que he comido 20 pepinos
    Cuando espero "two hours and thirty minutes"
    Entonces mi estómago debería gruñir
  @ingles
  Escenario: Esperar media hora en inglés
    Dado que he comido 1 pepinos
    Cuando espero "half hour"
    Entonces mi estómago no debería gruñir

  @español
  Escenario: Comer una cantidad fraccionaria de pepinos
    Dado que he comido 9.99 pepinos
    Cuando espero 3 horas
    Entonces mi estómago no debería gruñir
  @español
  Escenario: Comer una cantidad fraccionaria de pepinos
    Dado que he comido 0.5 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir
  @español
  Escenario: Comer una cantidad fraccionaria de pepinos
    Dado que he comido 10.5 pepinos
    Cuando espero 3 horas
    Entonces mi estómago debería gruñir  
  @español
  Escenario: Comer pepinos y esperar  segundos
    Dado que he comido 15 pepinos
    Cuando espero "7200 segundos"
    Entonces mi estómago debería gruñir
  @español
  Escenario: Comer pepinos y esperar en minutos y segundos
    Dado que he comido 35 pepinos
    Cuando espero "1 hora y 30 minutos y 45 segundos"
    Entonces mi estómago debería gruñir
  @español
  Escenario: comer muchos pepinos y gruñir
    Dado que he comido 42 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir
  @español
  Escenario: comer pocos pepinos y no gruñir
    Dado que he comido 10 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir
  @español
  Escenario: comer muchos pepinos y esperar menos de una hora
    Dado que he comido 50 pepinos
    Cuando espero media hora
    Entonces mi estómago no debería gruñir
  @español
  Escenario: comer pepinos y esperar en minutos
    Dado que he comido 30 pepinos
    Cuando espero 90 minutos
    Entonces mi estómago debería gruñir
  @español
  Escenario: comer pepinos y esperar en diferentes formatos
    Dado que he comido 25 pepinos
    Cuando espero "dos horas y treinta minutos"
    Entonces mi estómago debería gruñir
  
  @español
  Escenario: test gruñir basico
    Dado que he comido 15 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir 



