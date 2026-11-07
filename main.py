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

