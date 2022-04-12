# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.Paciente import Paciente

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para el constructor
    def test_paciente(self):
        print("*** Pruebas Unitarias: Constructor Paciente -- Test Case 1 ***");
        objetoPrueba = Paciente('Pedro','Ruiz del Castillo','16/02/1983');
        print('Constructor Paciente (Pedro, Ruiz del Castillo, 16/03/1983) y ¡Saludar!')
        r=objetoPrueba.saludar();
        assert r == "Hola soy Pedro Ruiz del Castillo";

        print('Clase Paciente -- Test Case 2 - obtenerNombre()')
        r=objetoPrueba.obtenerNombre();
        assert r =="Pedro";
        print('Clase Paciente -- Test Case 3 - modificarNombre(Andrés)')
        objetoPrueba.modificarNombre('Andrés');
        r=objetoPrueba.obtenerNombre();
        assert r =="Andrés";
        print('Clase Paciente -- Test Case 4 - obtenerApellidos()')
        r=objetoPrueba.obtenerApellidos();
        assert r == "Ruiz del Castillo";
        print('Clase Paciente -- Test Case 5 - modificarApellidos(Rodríguez Mas)')
        objetoPrueba.modificarApellidos('Rodríguez Mas');
        r=objetoPrueba.obtenerApellidos();
        assert r=="Rodríguez Mas";
        print('Clase Paciente -- Test Case 6 - obtenerFechaNacimiento() = 16/2/1983');
        r=objetoPrueba.obtenerFechaNacimiento();
        assert r=="16/2/1983";
        print("Clase Paciente -- Test Case 7 - obtenerEdad() = 39");
        ed=objetoPrueba.obtenerEdad();
        assert ed == 39;

    # Test 8
    def test_paciente8(self):
        print('Clase Paciente -- Test Case 8 - obtenerFechaNacimiento() = 25/12/1995')
        u2=Paciente('Jesús','Puente Colgante','25/12/1995');
        fn=u2.obtenerFechaNacimiento();
        assert fn == "25/12/1995"
    # Test 9
    def test_paciente9(self):
        print('Clase Paciente -- Test Case 9')
        u2=Paciente('Almudena','Puente Colgante','20/08/1990');
        print('u2.obtenerFechaNacimiento() = 20/8/1990');
        fn=u2.obtenerFechaNacimiento();
        assert fn=="20/8/1990"
        print('u2.obtenerEdad() = 31')
        edad=u2.obtenerEdad();
        assert edad == 31;
        
