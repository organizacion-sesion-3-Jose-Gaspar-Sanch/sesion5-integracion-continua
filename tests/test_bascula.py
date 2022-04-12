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
        print("obtenerTablaPesosHTML().isString()");
        print(objetoPrueba.obtenerTablaPesosHTML())
        assert objetoPrueba.obtenerTablaPesosHTML().isprintable()==True;
    # Test 2
    def test_bascula2(self):
        print("** Pruebas Unitarias: Báscula -- Test Case 2")
        objetoPrueba = Bascula();
        print("anotarPeso(70)");
        objetoPrueba.anotarPeso(70);
        assert objetoPrueba.obtenerNumeroAnotaciones() == 1;
        assert objetoPrueba.obtenerPesoMaximo() == 70;
        assert objetoPrueba.obtenerPesoMinimo() == 70;
        assert objetoPrueba.obtenerPesoMedio() == 70;
    # Test 3
    def test_bascula3(self):
        print("Pruebas Unitarias: Báscula -- Test Case 3")
        objetoPrueba = Bascula();
        print("anotarPeso(70,30)");
        objetoPrueba.anotarPeso(70);
        objetoPrueba.anotarPeso(30);
        assert objetoPrueba.obtenerNumeroAnotaciones() == 2;
        assert objetoPrueba.obtenerPesoMaximo() == 70;
        assert objetoPrueba.obtenerPesoMinimo() == 30;
        assert objetoPrueba.obtenerPesoMedio() == 50;
    # Test 4
    def test_bascula4(self):
        print("Pruebas Unitarias: Báscula -- Test Case 4")
        objetoPrueba = Bascula();
        print("anotarPeso(85,95,91)");
        objetoPrueba.anotarPeso(85);
        objetoPrueba.anotarPeso(95);
        objetoPrueba.anotarPeso(91);
        assert objetoPrueba.obtenerNumeroAnotaciones() == 3;
        assert objetoPrueba.obtenerPesoMaximo() == 95;
        assert objetoPrueba.obtenerPesoMinimo() == 85;
        assert objetoPrueba.obtenerPesoMedio() == 90.33;
    # Test 5
    def test_bascula5(self):
        print("Pruebas Unitarias: Báscula -- Test Case 5")
        objetoPrueba = Bascula();
        print("anotarPeso(85,95,91-1.83)");
        objetoPrueba.anotarPeso(85);
        objetoPrueba.anotarPeso(95);
        objetoPrueba.anotarPeso(91,1.83);
        assert objetoPrueba.obtenerNumeroAnotaciones() == 3;
        assert objetoPrueba.obtenerPesoMaximo() == 95;
        assert objetoPrueba.obtenerPesoMinimo() == 85;
        assert objetoPrueba.obtenerPesoMedio() == 90.33;
        assert objetoPrueba.calcularIMC() == 27.17;
    # Test 6
    def test_bascula6(self):
        print("Pruebas Unitarias: Báscula -- Test Case 6")
        assert Bascula.describirIMC(0).isprintable() == True;
        assert Bascula.describirIMC(1) == "<16.00: Infrapeso (delgadez severa)";
        assert Bascula.describirIMC(16.5) == "16.00 – 16.99: Infrapeso (delgadez moderada)"; 
        assert Bascula.describirIMC(17.5) == "17.00 - 18.49: Infrapeso (delgadez aceptable)"; 
        assert Bascula.describirIMC(19) == "18.50 - 24.99: Peso normal";
        assert Bascula.describirIMC(25) == "25.00 - 29.99: Sobrepeso";
        assert Bascula.describirIMC(33) == "30.00 - 34.99: Obeso (Tipo I)";
        assert Bascula.describirIMC(40) == "35.00 - 40.00: Obeso (Tipo II)";
        assert Bascula.describirIMC(40.5) == ">40.00: Obeso (Tipo III)";
         
         


