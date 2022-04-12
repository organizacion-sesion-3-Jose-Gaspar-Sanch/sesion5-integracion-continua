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
        self.pesos.push(peso);
        self.alturas.push(altura);
        self.fechas.push(fecha);
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
/**
 * Obtener peso medio
 * @returns peso medio
 */
    obtenerPesoMedio()
    {
        return (this.anotaciones==0 ? 0 : (this.pesos.reduce((suma,num)=>suma+num,0)/this.pesos.length).toFixed(1));
    }
/**
 * Obtener Tabla de Pesos HTML
 * @returns HTML table
 */        
    obtenerTablaPesosHTML()
    {
        let tabla="<table><tr><th>FECHA</th>PESOS (kg.)<th></tr>";
        for(let fila=0;fila<this.pesos.length;fila++)
        {
            tabla=tabla+"<tr><td>"+fechas[fila]+"</td>"+
            "<td>"+pesos[fila]+"</td></tr>";
        }
        tabla=tabla+"</table>";
        return tabla;
    }
/**
 * Calcula IMC a partir de la última medición
 * @returns Indice Masa Corporal (IMC)
 */    
    calcularIMC(){
        if(this.anotaciones>=1){
            return ((this.pesos[this.anotaciones-1]/Math.pow(this.alturas[this.anotaciones-1],2)).toFixed(2));
        }else{
            console.error('ERROR: No dispone de registros de altura y peso para calcular el IMC');
            return -1;
        }
    }
/**
 * Descripción del Índice Masa Corporal (IMC)
 * @param {*} imc: decimal indice masa corporal (16.00 - 40.00) 
 * @returns cadena descriptiva del Índice de Masa Corporal
 */
    static describirIMC(imc){
        if(imc<16)
            return "<16.00: Infrapeso (delgadez severa)";
        else if(imc>=16 && imc<17)
            return "16.00 – 16.99: Infrapeso (delgadez moderada)";
        else if(imc>=17 && imc<18.5)
            return "17.00 - 18.49: Infrapeso (delgadez aceptable)";
        else if(imc>=18.5 && imc<25)
            return "18.50 - 24.99: Peso normal";
        else if(imc>=25 && imc<30)
            return "25.00 - 29.99: Sobrepeso";
        else if(imc>=30 && imc<35)
            return "30.00 - 34.99: Obeso (Tipo I)";
        else if(imc>=35 && imc<=40)
            return "35.00 - 40.00: Obeso (Tipo II)";
        else if(imc>40)  
            return ">40.00: Obeso (Tipo III)";
    }