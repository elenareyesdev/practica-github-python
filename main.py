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
    
