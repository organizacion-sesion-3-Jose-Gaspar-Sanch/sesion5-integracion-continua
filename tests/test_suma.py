# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import suma

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_suma(self):
        assert suma(4,5) == 9
        assert suma(-1,-2) == -3
        assert suma(-7,5) == -2
        assert suma(-7,9) == 2
