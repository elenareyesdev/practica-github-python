#importamos a este archivo para crear archivos de log
import logging

# Importamos las herramientas para crear clases abstractas
from abc import ABC, abstractmethod


#creamos la estructura que configura el log
logging.basicConfig(
    filename= "registro.log",  # nombre del archivo donde se escribe
    level= logging.INFO,     # escribe desde INFO hacia arriba (incluye errores)
    format= "%(asctime)s - %(levelname)s - %(message)s",   # fecha - tipo - mensaje
    encoding= "utf-8"     # para que se guarden bien las tildes
)

# Anotamos un evento  en el log.
logging.info("Programa iniciado")

# EXCEPCIONES PERSONALIZADAS
# Son clases normales que heredan de Exception.
# Cada una sirve para identificar de qué parte viene el error
class ClienteInvalidoError(Exception):
    """se usa cuando los datos del cliente no son válidos."""
    pass


class ServicioInvalidoError(Exception):
     """se usa cuando los servicios no son válidos."""
     pass
 

class ServicioNoDisponibleError(Exception):
     """se usa cuando los servicios no están disponibles."""
     pass


 class ReservaInvalidaError(Exception):
     """se usa cuando la reserva no se puede hacer."""
     pass


#creamos Una clase abstracta que represente entidades generales del sistema.
class Entidad(ABC):
    """Clase abstracta general: es la que representa cualquier entidad del sistema."""

    @abstractmethod
    def describir(self):
        """Cada entidad hija debe describirse."""
        pass

# creamos la clase cliente con validaciones 
class Cliente(Entidad):
    """clase cliente con validaciones robustas y encapsulación de datos personales"""

    def __init__(self, nombre, correo, telefono):
        if not nombre.strip():
          raise ClienteInvalidoError("El nombre no puede estar vacío")
        if "@" not in correo:
                  raise ClienteInvalidoError("El correo no puede estar sin el @")
        if not telefono .isdigit():
                  raise ClienteInvalidoError("El teléfono solo debe tener números")
        
        self._nombre = nombre 
        self._correo = correo 
        self._telefono = telefono

    def obtener_nombre(self):
          return self._nombre
        

    def describir(self):
         return f"Cliente: {self._nombre},{self._correo}"
    
    
   # Prueba 1: cliente correcto
try:
    cliente1 = Cliente("Elena", "elena@correo.com", "3001234567")
    print(cliente1.describir())
    logging.info("Cliente creado correctamente")

except ClienteInvalidoError as error:
    print("Error de cliente:", error)
    logging.error(f"Error de cliente: {error}")
    
    
    # Prueba 2: cliente incorrecto
try:
    cliente2 = Cliente("Elena", "elena-correo,com", "3001234567")
    print(cliente2.describir())
    logging.info("Cliente creado correctamente")

except ClienteInvalidoError as error:
    print("Error de cliente:", error)
    logging.error(f"Error de cliente: {error}")


# creamos la clase abstracta servicio   
class Servicio(Entidad):
    """Clase abstracta: molde para todos los servicios de Software FJ."""    

    def __init__(self, nombre, precio_base):
    
        if not nombre.strip():
            raise ServicioInvalidoError("El nombre del servicio no puede estar vacío")
        if precio_base <= 0:
            raise ServicioInvalidoError("El precio debe ser mayor que cero")
    
        self._nombre = nombre 
        self._precio_base =precio_base
        self._disponible = True
    
    @abstractmethod
    def calcular_costo(self, horas):
        """Cada servicio hijo calcula su costo a su manera."""
        pass

# Prueba: Servicio es abstracta, no se puede crear directamente
try:
    servicio = Servicio("Prueba", 1000)
except TypeError as error:
    print("No se puede crear un Servicio directamente:", error)
    
