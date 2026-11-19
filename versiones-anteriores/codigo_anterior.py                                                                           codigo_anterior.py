#importamos a este archivo para crear archivos de log
import logging
import math

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


#creamos la clase hija Alquiler Equipo

class AlquilerEquipo(Servicio):
    """Servicio de Alquiler de Equipos"""  
      
    def __init__(self, nombre, precio_base, cantidad_equipos):
        super().__init__(nombre, precio_base)
        if cantidad_equipos <= 0:
            raise ServicioInvalidoError("la cantidad de equipos debe ser mayor que cero")
        self._cantidad_equipos = cantidad_equipos
        
    def calcular_costo(self, horas):
         """Costo del Alquiler de Equipos: precio por hora por cantidad de Equipos."""
         return self._precio_base*horas * self._cantidad_equipos
     
    def describir(self):
         """Describe el alquiler de equipos con su nombre y cantidad de equipos."""
         return f"AlquilerEquipo: {self._nombre}, cantidad_equipos: {self._cantidad_equipos}"
     
     
# prueba 5: AlquilerEquipo
try:
    AlquilerEquipo1 = AlquilerEquipo("Proyector", 20000,3)
    print(AlquilerEquipo1.describir())
    print("Costo por 2 horas:", AlquilerEquipo1.calcular_costo(2))
    logging.info("AlquilerEquipo creado correctamente")
except ServicioInvalidoError as error:
    print("Error de servicio:", error)
    logging.error(f"Error de servicio: {error}")
    
# prueba 6: Alquiler invalido
try:
    AlquilerEquipo2 = AlquilerEquipo("Portatil", 30000,0)
    print(AlquilerEquipo2.describir())
    print("Costo por 2 horas:", AlquilerEquipo2.calcular_costo(2))
    logging.info("AlquilerEquipo creado correctamente")
except ServicioInvalidoError as error:
    print("Error de servicio:", error)
    logging.error(f"Error de servicio: {error}")


#creamos la clase hija Asesoria   
class Asesoria(Servicio):
    """Servicio de Asesoria especializada"""  
      
    def __init__(self, nombre, precio_base, especialista):
        super().__init__(nombre, precio_base)
        if not especialista.strip():
            raise ServicioInvalidoError("El nombre del especialista no puede estar vacío")
        self._especialista = especialista
        
    def calcular_costo(self, horas):
        """Costo de Asesoria: precio * horas ."""
     
        return self._precio_base*horas 
 
    def describir(self):
        """Describe la asesoria con su nombre y especialista."""
        return f"Asesoria: {self._nombre}, especialista: {self._especialista}"
    

# prueba 7: Asesoria valida
try:
    asesoria1 = Asesoria("Python basico", 40000, "Rosa Gomez")
    print(asesoria1.describir())
    print("Costo por 2 horas:", asesoria1.calcular_costo(2))
    logging.info("Asesoria creado correctamente")
except ServicioInvalidoError as error:
    print("Error de servicio:", error)
    logging.error(f"Error de servicio: {error}")
    
    
# prueba 8: asesoría inválida, especialista vacío
try:
    asesoria2 = Asesoria("Python basico", 40000," ")
    print(asesoria2.describir())
    print("Costo por 2 horas:", asesoria2.calcular_costo(2))
    logging.info("Asesoria creada correctamente")
except ServicioInvalidoError as error:
    print("Error de servicio:", error)
    logging.error(f"Error de servicio: {error}")


# Creamos la clase que sera reserva.
class Reserva:
    """Permite crear, confirmar, cancelar y procesar reservas"""

    # Inicializamos los datos de la reserva
    def __init__(self, cliente, servicio, duracion):
        """Inicializa una reserva y la verificacion de que sus datos sean correctos."""
        
        try:
            # Hacemos la verificacion que el cliente exista
            if cliente is None:
                raise ReservaInvalidaError("El cliente no existe.")
             
            # Hcemos la verificacion que el servicio exista.
            if servicio is None:
                raise ReservaInvalidaError("El servicio no existe.")

            # Hacemos la verificacion que la duracion sea un numero.
            if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
                raise ReservaInvalidaError("La duracion debe ser numerica.")

            # Hacemos la verificacion que la duracion sea positiva y finita
            if not math.isfinite(duracion) or duracion <= 0:
                raise ReservaInvalidaError("La duracion debe ser mayor que cero.")

            # Guardaremos el cliente de la reserva.
            self.cliente = cliente

            # Guardaremos el servicio que fue seleccionado.
            self.servicio = servicio

            # Guardaremos la duracion de la reserva.
            self.duracion = duracion

            # Estableceremos el estado inicial de la reserva.
            self.estado = "pendiente"

            # Registramos la creacion de la reserva.
            logging.info("Reserva creada correctamente.")

        except ReservaInvalidaError:
            # Registramos el error de validacion.
            logging.exception("Error al crear la reserva.")
            raise

        except Exception as error:
            # Registramos cualquier otro error inesperado.
            logging.exception("error inesperado al crear la reserva.")

            # Generamos una excepcion que sera personalizada.
            raise ReservaInvalidaError(
                "No fue posible crear la reserva."
            ) from error
            
# Creamos el metodo para confirmar la reserva.
    def confirmar(self):
        """Confirma una reserva que se va a encontrar pendiente"""

        try:
            # Verificamos que la reserva este pendiente.
            if self.estado != "pendiente":
                raise ReservaInvalidaError(
                    "Solo se podran confirmar reservas pendientes."
                )

            # Cambiaremos el estado de la reserva.
            self.estado = "confirmada"

        except ReservaInvalidaError:
            # Registraremos el error en nuestro archivo de logs.
            logging.exception("Error al confirmar la reserva.")
            raise

        else:
            # Registramos la confirmacion de la reserva.
            logging.info("Reserva confirmada correctamente.")

            # Devolvemos el estado actual.
            return self.estado
#Creamos el metodo para cancelar la reserva.
    def cancelar(self):
        """Cancelar una reserva pendiente o confirmada"""
        try:
            # Verificamos que la reserva se pueda cancelar.
            if self.estado not in ["pendiente", "confirmada"]:
                raise ReservaInvalidaError(
                    "No se puede cancelar una reserva procesada o cancelada."
                )

            # Cambiamos el estado de la reserva a cancelada.
            self.estado = "cancelada"

        except ReservaInvalidaError:
            # Registramos el error en nuestro archivo de logs.
            logging.exception("Error al cancelar la reserva.")
            raise

        else:
            # Registraremos que la cancelacion de la reserva fue exitosa
            logging.info("Reserva cancelada correctamente.")

             # Devolvemos a su estado actual.
            return self.estado

    # Creamos el metodo para poder procesar la reserva.
    def procesar(self):
        """Procesar una reserva que se encuentra confirmada"""
        try:
            # Verificaremos que la reserva este confirmada.
            if self.estado != "confirmada":
                raise ReservaInvalidaError(
                    "Primero se debe confirmar la reserva."
                )

            # Cambiaremos el estado de la reserva.
            self.estado = "procesada"

        except ReservaInvalidaError:
            # Registraremos el error en nuestro archivo de logs.
            logging.exception("Error al procesar la reserva.")
            raise

        else:
            # Registramos que el procesamiento fue exitoso.
            logging.info("Reserva procesada correctamente.")

            # Devolvemos el estado actual.
            return self.estado

        finally:
            # Registramos finalmente la finalizacion del intento de procesamiento.
            logging.info("Finalizo el intento de procesar la reserva.")


# La clase para administrar nuestro sistema de software FJ.
class SistemaSoftwareFJ:
    """Administra los clientes, servicios y reservas del sistema."""

    def __init__(self):
        """Se crea las listas donde se guardan los datos del sistema."""

        # La lista para guardar los clientes.
        self.clientes = []

        # La lista para guardar los servicios.
        self.servicios = []

        # La lista para guardar las reservas.
        self.reservas = []

    # Utilizaremos un metodo para agregar diferentes elementos al sistema.
    def agregar(self, elemento, servicio=None, duracion=None):
        """Agregar un cliente, servicio o reserva segun sea los argumentos."""

        # Con los tres argumentos se va a crear una reserva.
        if servicio is not None or duracion is not None:

            # Hacemos la verificacion de que el cliente sea valido.
            if not isinstance(elemento, Cliente):
                raise ReservaInvalidaError(
                    "El cliente de la reserva no es valido."
                )

            # Hacemos la verificacion de que el servicio sea valido.
            if not isinstance(servicio, Servicio):
                raise ReservaInvalidaError(
                    "El servcio de la reserva no es valido."
                )

            # Hacemos la verificacion para que se indique la duracion.
            if duracion is None:
                raise ReservaInvalidaError(
                    "Debe indicar la duracion de la reserva."
                )

            # Hacemos la creacion de la nueva reserva.
            nueva_reserva = Reserva(elemento, servicio, duracion)

            # Guardaremos la reserva en la lista.
            self.reservas.append(nueva_reserva)

            logging.info("Reserva agregada al sistema.")

            return nueva_reserva

        # Si sera un cliente, lo guardaremos en su lista.
        if isinstance(elemento, Cliente):
            self.clientes.append(elemento)
            logging.info("El cliente agregado al sistema.")


        # Si sera un servicio, lo guardaremos en su lista.
        elif isinstance(elemento, Servicio):
            self.servicios.append(elemento)
            logging.info("El servicio sera agregado al sistema.")

        # Si sera una reserva existente, la guardaremos.
        elif isinstance(elemento, Reserva):
            self.reservas.append(elemento)
            logging.info("La reeserva sera agregada al sistema.")

        else:
            raise ValueError(
                "Solo se podran agregar clientes, servicios o reservas."
            )

    # El metodo para consultar los elementos que fueron guardados.
    def mostrar(self, tipo=None):
        """Devuelve todas las listas o la lista que sera indicada."""

        # Si son se indica el tipo, devolvera todas las listas.
        if tipo is None:
            return {
                "clientes": self.clientes,
                "servcios": self.servicios,
                "reservas": self.reservas
            }

        # Devolvera la lista de los clientes.
        elif tipo == "clientes":
            return self.clientes

        # Devolvera la lista de servicios
        elif tipo == "servicios":
            return self.servicios

        # Devolvera la lista de reservas
        elif tipo == "reservas":
            return self.reservas

        else:
            raise ValueError("El tipo de lista no existira.")

    # Ahora se desarrollara las pruebas 9 y 10: reservas.

    # Ahora hacemos la creacion del administrador del sistema.
sistema = SistemaSoftwareFJ()

# Ahora agregaremos el cliente y el servicio a sus listas.
sistema.agregar(cliente1)
sistema.agregar(sala1)

# Se hara la prueba 9: Creara una reserva valida.
try:
   print("\nPRUEBA 9: Reserva valida")

   # Se hace la creacion de una reserva con el cliente, servicio y duracion.
   reserva1 = sistema.agregar(cliente1, sala1, 3)

   # Se confirma la reserva.
   print("El estado de la reserva:", reserva1.confirmar())

   logging.info("La prueba 9 se realizo correctamente.")

except ReservaInvalidaError as error:
    print("Error en la prueba 9.", error)
    logging.error("Error en la prueba 9: %s", error)

# Se hara la prueba 10: Creara una reserva invalida.
try:
    print("\nPRUEBA 10: Reserva invalida")

    # Se intentara la creacion de una reserva con duracion igual a cero.
    reserva2 = sistema.agregar(cliente1, sala1, 0)

    print("Estado de la reserva:", reserva2.estado)

except ReservaInvalidaError as error:
    print("El error en la prueba 10:", error)
    logging.error("El error en la prueba 10: %s", error)


# Se hace la verificacion de las listas internas.

print("\nRegistros del sistema")

# Se consultara la cantidad de clientes.
print("La cantidad de clientes:", len(sistema.mostrar("clientes")))

# Se consultara la cantidad de servicios.
print("La cantidad de servicios:", len(sistema.mostrar("servicios")))

# Se consultara la cantidad de reservas.
print("La cantidad de reservas:", len(sistema.mostrar("reservas")))

logging.info("Se hace la verificacion de las listas finalizadas.")


    
