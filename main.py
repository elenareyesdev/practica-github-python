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

