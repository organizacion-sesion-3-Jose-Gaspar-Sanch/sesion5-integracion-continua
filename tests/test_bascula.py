# Librería pytest para ejecutar tests
from hashlib import new
import pytest

# Importar archivo de ejercicio
from ejercicios.Bascula import Bascula

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para el constructor
    def test_bascula(self):
        print("*** Pruebas Unitarias: Constructor Báscula -- Test Case 1 ***");
        objetoPrueba = Bascula();
        print("obtenerNumeroAnotaciones() == 0");
        assert objetoPrueba.obtenerNumeroAnotaciones () == 0;
        print("obtenerPesoMaximo() = 0");
        assert objetoPrueba.obtenerPesoMaximo() == 0;
        print("obtenerPesoMínimo() = 0");
        assert objetoPrueba.obtenerPesoMinimo() == 0;


