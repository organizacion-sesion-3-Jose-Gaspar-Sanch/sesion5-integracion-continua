from datetime import date, datetime
# Clase Paciente
class Paciente:
    # Constructor
    def __init__(self,nom,ape,strFecha) -> None:
        self.nombre=nom;
        self.apellidos=ape;
        self.registroBascula=[];
        
        fecha=strFecha.split("/");
        anyo=int(fecha[2]);
        mes=int(fecha[1]);
        dia=int(fecha[0]);
        
        self.fechaNacimiento=date(anyo,mes,dia);

    # Método que permite al paciente Saludar
    def saludar(self) -> str :
        return "Hola soy "+self.nombre+" "+self.apellidos;
    
    # Métodos GETTER
    def obtenerNombre(self) -> str :
        return self.nombre;
    
    def obtenerApellidos(self) -> str :
        return self.apellidos;
    
    def obtenerFechaNacimiento(self)->str : 
        aaaa=str(self.fechaNacimiento.year);
        mm=str(self.fechaNacimiento.month);
        dd=str(self.fechaNacimiento.day);
        return dd+"/"+mm+"/"+aaaa;
        
    def obtenerEdad(self) -> int :
        mesNac=self.fechaNacimiento.month;
        diaNac=self.fechaNacimiento.day;
        mesHoy=datetime.now().month;
        diaHoy=datetime.now().day;

        anyoActual=datetime.now().year;
        anyoNacimiento=self.fechaNacimiento.year;
        
        if diaHoy<diaNac and mesHoy<=mesNac :
            return anyoActual-anyoNacimiento-1;
        else :
            return (anyoActual-anyoNacimiento);
        
    # Métodos SETTER
      
    def anyadirBascula(self,_bascula) -> None :
        self.registroBascula.append(_bascula);

    def obtenerRegistrosBascula(self):
        return self.registroBascula;

    def calcularIMC(self) :
        if len(self.registroBascula)!= 0 :
            b=self.registroBascula[len(self.registroBascula)-1]
            return b.calcularIMC();
        else : 
            return -1;
    
    def modificarNombre(self,_nombre) -> None :
        self.nombre=_nombre;

    def modificarApellidos(self,_apellidos) -> None :
        self.apellidos=_apellidos;
    
    def modificarFechaNacimiento(self,_fecha) -> None :
        self.fechaNacimiento=_fecha;

