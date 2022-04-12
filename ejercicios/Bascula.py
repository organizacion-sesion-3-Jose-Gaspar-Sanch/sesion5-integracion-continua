from datetime import date;
# Clase Báscula
class Bascula:
    # Constructor
    def __init__(self) -> None:
        self.pesos=[ ];
        self.alturas=[ ];
        self.fechas=[ ];
        self.anotaciones=0;


    # Obtener Numero de Anotaciones
    def obtenerNumeroAnotaciones(self) -> int :
        return self.anotaciones;
    
    
    # Anota una nueva pesada
    def anotarPeso(self, peso,altura=1,fecha=date.today) :
        self.pesos.append(peso);
        self.alturas.append(altura);
        self.fechas.append(fecha);
        self.anotaciones=self.anotaciones+1;

    # Obtener peso máximo
    def obtenerPesoMaximo(self) -> float:
        pesoMaximo=0;
        for num in self.pesos : 
            if num > pesoMaximo :
                pesoMaximo=num;
        
        return pesoMaximo;

    # Obtener peso mínimo
    def obtenerPesoMinimo(self) -> float:
        if self.anotaciones == 0 :
            pesoMinimo=0;
        else :
            pesoMinimo=self.pesos[0];
            for num in self.pesos : 
                if num < pesoMinimo :
                    pesoMinimo=num;

        return pesoMinimo

    # Obtener peso medio
    def obtenerPesoMedio(self) -> float :
        suma=0;
        if self.anotaciones!=0 :
            for p in self.pesos :
                suma=suma+p;
            return round(suma / self.anotaciones,2);
        else :
            return 0;

    # Obtener Tabla de Pesos HTML
    def obtenerTablaPesosHTML(self) -> str :
        tabla="<table><tr><th>FECHA</th>PESOS (kg.)<th></tr>";
        for fila in range(0,self.anotaciones,1) :
            tabla=tabla+"<tr><td>"+self.fechas[fila]+"</td><td>"+self.pesos[fila]+"</td></tr>";
        tabla=tabla+"</table>";
        return tabla;
        
    # Calcula IMC a partir de la última medición
    def calcularIMC(self) -> float :
        if self.anotaciones>=1 :
            return round(self.pesos[self.anotaciones-1]/pow(self.alturas[self.anotaciones-1],2),2);
        else :
            print('ERROR: No dispone de registros de altura y peso para calcular el IMC');
            return -1;

    # Descripción del Índice Masa Corporal (IMC)
    @staticmethod
    def describirIMC(imc) -> str :
        if imc<16 :
            return "<16.00: Infrapeso (delgadez severa)";
        elif imc>=16 and imc<17 : 
            return "16.00 – 16.99: Infrapeso (delgadez moderada)";
        elif imc>=17 and imc<18.5 :
            return "17.00 - 18.49: Infrapeso (delgadez aceptable)";
        elif imc>=18.5 and imc<25 :
            return "18.50 - 24.99: Peso normal";
        elif imc>=25 and imc<30 :
            return "25.00 - 29.99: Sobrepeso";
        elif imc>=30 and imc<35 :
            return "30.00 - 34.99: Obeso (Tipo I)";
        elif imc>=35 and imc<=40 :
            return "35.00 - 40.00: Obeso (Tipo II)";
        elif imc>40 :
            return ">40.00: Obeso (Tipo III)";
            