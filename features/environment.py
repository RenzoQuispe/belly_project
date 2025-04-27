from src.belly import Belly
'''
    Behave automáticamente busca los hooks en el archivo environment.py y los ejecuta en el momento adecuado.
'''
def before_scenario(context, scenario):
    from unittest.mock import MagicMock
    from src.belly import Belly
    
    fake_clock = MagicMock()
    fake_clock.return_value = 10000  # tiempo fijo
    context.belly = Belly(clock_service=fake_clock)

