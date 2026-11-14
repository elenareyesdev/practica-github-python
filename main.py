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


# creamos la clase hija sala
class Sala(Servicio):
    """Servicio de reserva de salas."""    
    def __init__(self, nombre, precio_base, capacidad):
        super().__init__(nombre, precio_base)
        if capacidad <= 0:
            raise ServicioInvalidoError("la capacidad debe ser mayor que cero")
                
        self._capacidad = capacidad
    
    def calcular_costo(self, horas):
        """Costo de la sala: precio por hora por cantidad de horas."""
        return self._precio_base*horas
    
    def describir(self):
        """Describe la sala con su nombre y capacidad."""
        return f"Sala: {self._nombre},capacidad: {self._capacidad}"
    
# Prueba 3: sala válida
try:
    sala1 = Sala("Sala Norte", 50000, 10)
    print(sala1.describir())
    print("Costo por 3 horas:", sala1.calcular_costo(3))
    logging.info("Sala creada correctamente")
except ServicioInvalidoError as error:
    print("Error de servicio:", error)
    logging.error(f"Error de servicio: {error}")
    
    # prueba 4: sala inválida
    
try:
    sala2 = Sala("Sala Sur", 50000,0)
    print(sala2.describir())
    print("Costo por 3 horas:", sala2.calcular_costo(3))
    logging.info("Sala creada correctamente")
except ServicioInvalidoError as error:
    print("Error de servicio:", error)
    logging.error(f"Error de servicio: {error}")
            
    
