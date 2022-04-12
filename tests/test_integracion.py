# Librería pytest para ejecutar tests
import pytest

# Pruebas de INTEGRACIÓN: Paciente - Báscula
# Importar archivo de ejercicio
from ejercicios.Paciente import Paciente
from ejercicios.Bascula import Bascula

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para el constructor
    def test_integracion(self):
        print('Integration Suite -- Integración Paciente-Bascula - Test Case 1')
        objPaciente=Paciente('Pedro','Ruiz del Castillo','16/02/1983');
        saludo=objPaciente.saludar();
        assert saludo.isprintable() == True;
        objBascula=Bascula();
        objBascula.anotarPeso(95.5,1.83);
        assert objBascula.obtenerNumeroAnotaciones() == 1;
        assert objPaciente.calcularIMC() == -1;
        objPaciente.anyadirBascula(objBascula);
        assert objPaciente.calcularIMC() == 28.52;
