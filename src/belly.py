class Belly:
    def __init__(self,clock_service=None):
        self.pepinos_comidos = 0.0
        self.tiempo_esperado = 0
        self.clock_service = clock_service 

    def comer(self, pepinos):
        if pepinos < 0:
            raise ValueError("La cantidad de pepinos no puede ser negativa.")
        elif pepinos > 1000:
            raise ValueError("La cantidad de pepinos no puede ser mayor a 100.")
        self.pepinos_comidos += float(pepinos)

    def esperar(self, tiempo_en_horas):
        self.tiempo_esperado += tiempo_en_horas
    
    def esta_gruñendo(self):
        # El estómago gruñe si ha esperado al menos 1.5 horas y ha comido más de 10 pepinos
        return self.tiempo_esperado >= 1.5 and self.pepinos_comidos > 10
