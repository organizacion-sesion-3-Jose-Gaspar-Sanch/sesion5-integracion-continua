# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import espar

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación espar
    def test_espar(self):
        assert espar(0) == True
        assert espar(1) == False
        assert espar(2) == True
        assert espar(3) == False
        assert espar(4) == True
        assert espar(5) == False
        assert espar(6) == True
        assert espar(10) == True
        assert espar(25) == False
        assert espar(-1) == False
