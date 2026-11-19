# Importamos esta libreria para crear archivos de log
import logging
import math

# Importamos las herramientas para crear clases abstractas
from abc import ABC, abstractmethod


# Creamos la estructura que configura el log
logging.basicConfig(
    filename="registro.log",  # nombre del archivo donde se escribe
    level=logging.INFO,  # escribe desde INFO hacia arriba (incluye errores)
    format="%(asctime)s - %(levelname)s - %(message)s",  # fecha - tipo - mensaje
    encoding="utf-8"  # para que se guarden bien las tildes
)

# Anotamos un evento en el log.
logging.info("Programa iniciado")


# EXCEPCIONES PERSONALIZADAS
# Son clases normales que heredan de Exception.
# Cada una sirve para identificar de que parte viene el error
class ClienteInvalidoError(Exception):
    """Se usa cuando los datos del cliente no son validos."""
    pass


class ServicioInvalidoError(Exception):
    """Se usa cuando los servicios no son validos."""
    pass


class ServicioNoDisponibleError(Exception):
    """Se usa cuando los servicios no estan disponibles."""
    pass


class ReservaInvalidaError(Exception):
    """Se usa cuando la reserva no se puede hacer."""
    pass


# Creamos una clase abstracta que represente entidades generales del sistema.
class Entidad(ABC):
    """Clase abstracta general: representa cualquier entidad del sistema."""

    @abstractmethod
    def describir(self):
        """Cada entidad hija debe describirse."""
        pass


# Creamos la clase cliente con validaciones
class Cliente(Entidad):
    """Clase cliente con validaciones robustas y encapsulacion de datos personales"""

    def __init__(self, nombre, correo, telefono):
        if not nombre.strip():
            raise ClienteInvalidoError("El nombre no puede estar vacío")
        if "@" not in correo:
            raise ClienteInvalidoError("El correo no puede estar sin el @")
        if not telefono.isdigit():
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

except Exception as error:
    print("Error inesperado:", error)
    logging.error(f"Error inesperado: {error}")


# Prueba 2: cliente incorrecto
try:
    cliente2 = Cliente("Elena", "elena-correo,com", "3001234567")
    print(cliente2.describir())
    logging.info("Cliente creado correctamente")

except ClienteInvalidoError as error:
    print("Error de cliente:", error)
    logging.error(f"Error de cliente: {error}")

except Exception as error:
    print("Error inesperado:", error)
    logging.error(f"Error inesperado: {error}")


# Creamos la clase abstracta servicio
class Servicio(Entidad):
    """Clase abstracta: molde para todos los servicios de Software FJ."""

    def __init__(self, nombre, precio_base):

        if not nombre.strip():
            raise ServicioInvalidoError("El nombre del servicio no puede estar vacío")
        if precio_base <= 0:
            raise ServicioInvalidoError("El precio debe ser mayor que cero")

        self._nombre = nombre
        self._precio_base = precio_base
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
    logging.error(f"No se puede crear un Servicio directamente: {error}")


# Creamos la clase hija sala
class Sala(Servicio):
    """Servicio de reserva de salas."""

    def __init__(self, nombre, precio_base, capacidad):
        super().__init__(nombre, precio_base)
        if capacidad <= 0:
            raise ServicioInvalidoError("la capacidad debe ser mayor que cero")

        self._capacidad = capacidad

    def calcular_costo(self, horas):
        """Costo de la sala: precio por hora por cantidad de horas."""
        return self._precio_base * horas

    def describir(self):
        """Describe la sala con su nombre y capacidad."""
        return f"Sala: {self._nombre},capacidad: {self._capacidad}"


# Prueba 3: sala valida
try:
    sala1 = Sala("Sala Norte", 50000, 10)
    print(sala1.describir())
    print("Costo por 3 horas:", sala1.calcular_costo(3))
    logging.info("Sala creada correctamente")

except ServicioInvalidoError as error:
    print("Error de servicio:", error)
    logging.error(f"Error de servicio: {error}")

except Exception as error:
    print("Error inesperado:", error)
    logging.error(f"Error inesperado: {error}")


# Prueba 4: sala invalida
try:
    sala2 = Sala("Sala Sur", 50000, 0)
    print(sala2.describir())
    print("Costo por 3 horas:", sala2.calcular_costo(3))
    logging.info("Sala creada correctamente")

except ServicioInvalidoError as error:
    print("Error de servicio:", error)
    logging.error(f"Error de servicio: {error}")

except Exception as error:
    print("Error inesperado:", error)
    logging.error(f"Error inesperado: {error}")


# Creamos la clase hija Alquiler Equipo
class AlquilerEquipo(Servicio):
    """Servicio de Alquiler de Equipos"""

    def __init__(self, nombre, precio_base, cantidad_equipos):
        super().__init__(nombre, precio_base)
        if cantidad_equipos <= 0:
            raise ServicioInvalidoError("la cantidad de equipos debe ser mayor que cero")
        self._cantidad_equipos = cantidad_equipos

    def calcular_costo(self, horas):
        """Costo del Alquiler de Equipos: precio por hora por cantidad de equipos."""
        return self._precio_base * horas * self._cantidad_equipos

    def describir(self):
        """Describe el alquiler de equipos con su nombre y cantidad de equipos."""
        return f"AlquilerEquipo: {self._nombre}, cantidad_equipos: {self._cantidad_equipos}"


# Prueba 5: AlquilerEquipo valido
try:
    AlquilerEquipo1 = AlquilerEquipo("Proyector", 20000, 3)
    print(AlquilerEquipo1.describir())
    print("Costo por 2 horas:", AlquilerEquipo1.calcular_costo(2))
    logging.info("AlquilerEquipo creado correctamente")

except ServicioInvalidoError as error:
    print("Error de servicio:", error)
    logging.error(f"Error de servicio: {error}")

except Exception as error:
    print("Error inesperado:", error)
    logging.error(f"Error inesperado: {error}")


# Prueba 6: Alquiler invalido
try:
    AlquilerEquipo2 = AlquilerEquipo("Portatil", 30000, 0)
    print(AlquilerEquipo2.describir())
    print("Costo por 2 horas:", AlquilerEquipo2.calcular_costo(2))
    logging.info("AlquilerEquipo creado correctamente")

except ServicioInvalidoError as error:
    print("Error de servicio:", error)
    logging.error(f"Error de servicio: {error}")

except Exception as error:
    print("Error inesperado:", error)
    logging.error(f"Error inesperado: {error}")


# Creamos la clase hija Asesoria
class Asesoria(Servicio):
    """Servicio de Asesoria especializada"""

    def __init__(self, nombre, precio_base, especialista):
        super().__init__(nombre, precio_base)
        if not especialista.strip():
            raise ServicioInvalidoError("El nombre del especialista no puede estar vacío")
        self._especialista = especialista

    def calcular_costo(self, horas):
        """Costo de Asesoria: precio * horas."""
        return self._precio_base * horas

    def describir(self):
        """Describe la asesoria con su nombre y especialista."""
        return f"Asesoria: {self._nombre}, especialista: {self._especialista}"


# Prueba 7: Asesoria valida
try:
    asesoria1 = Asesoria("Python basico", 40000, "Rosa Gomez")
    print(asesoria1.describir())
    print("Costo por 2 horas:", asesoria1.calcular_costo(2))
    logging.info("Asesoria creada correctamente")

except ServicioInvalidoError as error:
    print("Error de servicio:", error)
    logging.error(f"Error de servicio: {error}")

except Exception as error:
    print("Error inesperado:", error)
    logging.error(f"Error inesperado: {error}")


# Prueba 8: asesoria invalida, especialista vacio
try:
    asesoria2 = Asesoria("Python basico", 40000, " ")
    print(asesoria2.describir())
    print("Costo por 2 horas:", asesoria2.calcular_costo(2))
    logging.info("Asesoria creada correctamente")

except ServicioInvalidoError as error:
    print("Error de servicio:", error)
    logging.error(f"Error de servicio: {error}")

except Exception as error:
    print("Error inesperado:", error)
    logging.error(f"Error inesperado: {error}")


# Creamos la clase que sera reserva.
class Reserva:
    """Permite crear, confirmar, cancelar y procesar reservas"""

    # Inicializamos los datos de la reserva
    def __init__(self, cliente, servicio, duracion):
        """Inicializa una reserva y verifica que sus datos sean correctos."""

        try:
            # Verificamos que el cliente exista
            if cliente is None:
                raise ReservaInvalidaError("El cliente no existe.")

            # Verificamos que el servicio exista.
            if servicio is None:
                raise ReservaInvalidaError("El servicio no existe.")

            # Verificamos que el servicio este disponible.
            if not servicio._disponible:
                raise ServicioNoDisponibleError("El servicio no está disponible.")

            # Verificamos que la duracion sea un numero.
            if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
                raise ReservaInvalidaError("La duracion debe ser numerica.")

            # Verificamos que la duracion sea positiva y finita
            if not math.isfinite(duracion) or duracion <= 0:
                raise ReservaInvalidaError("La duracion debe ser mayor que cero.")

            # Guardamos el cliente de la reserva.
            self.cliente = cliente

            # Guardamos el servicio que fue seleccionado.
            self.servicio = servicio

            # Guardamos la duracion de la reserva.
            self.duracion = duracion

            # Establecemos el estado inicial de la reserva.
            self.estado = "pendiente"

            # Registramos la creacion de la reserva.
            logging.info("Reserva creada correctamente.")

        except (ReservaInvalidaError, ServicioNoDisponibleError):
            # Registramos el error de validacion.
            logging.exception("Error al crear la reserva.")
            raise

        except Exception as error:
            # Registramos cualquier otro error inesperado.
            logging.exception("Error inesperado al crear la reserva.")

            # Generamos una excepcion personalizada.
            raise ReservaInvalidaError(
                "No fue posible crear la reserva."
            ) from error

    # Metodo para confirmar la reserva.
    def confirmar(self):
        """Confirma una reserva que se encuentra pendiente"""

        try:
            # Verificamos que la reserva este pendiente.
            if self.estado != "pendiente":
                raise ReservaInvalidaError(
                    "Solo se podran confirmar reservas pendientes."
                )

            # Cambiamos el estado de la reserva.
            self.estado = "confirmada"

        except ReservaInvalidaError:
            # Registramos el error en nuestro archivo de logs.
            logging.exception("Error al confirmar la reserva.")
            raise

        else:
            # Registramos la confirmacion de la reserva.
            logging.info("Reserva confirmada correctamente.")

            # Devolvemos el estado actual.
            return self.estado

    # Metodo para cancelar la reserva.
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
            # Registramos que la cancelacion fue exitosa
            logging.info("Reserva cancelada correctamente.")

            # Devolvemos el estado actual.
            return self.estado

    # Metodo para procesar la reserva.
    def procesar(self):
        """Procesar una reserva que se encuentra confirmada"""
        try:
            # Verificamos que la reserva este confirmada.
            if self.estado != "confirmada":
                raise ReservaInvalidaError(
                    "Primero se debe confirmar la reserva."
                )

            # Cambiamos el estado de la reserva.
            self.estado = "procesada"

        except ReservaInvalidaError:
            # Registramos el error en nuestro archivo de logs.
            logging.exception("Error al procesar la reserva.")
            raise

        else:
            # Registramos que el procesamiento fue exitoso.
            logging.info("Reserva procesada correctamente.")

            # Devolvemos el estado actual.
            return self.estado

        finally:
            # Registramos la finalizacion del intento de procesamiento.
            logging.info("Finalizo el intento de procesar la reserva.")


# La clase para administrar nuestro sistema de Software FJ.
class SistemaSoftwareFJ:
    """Administra los clientes, servicios y reservas del sistema."""

    def __init__(self):
        """Se crean las listas donde se guardan los datos del sistema."""

        # La lista para guardar los clientes.
        self.clientes = []

        # La lista para guardar los servicios.
        self.servicios = []

        # La lista para guardar las reservas.
        self.reservas = []

    # Metodo para agregar diferentes elementos al sistema.
    def agregar(self, elemento, servicio=None, duracion=None):
        """Agregar un cliente, servicio o reserva segun los argumentos."""

        # Con los tres argumentos se crea una reserva.
        if servicio is not None or duracion is not None:

            # Verificamos que el cliente sea valido.
            if not isinstance(elemento, Cliente):
                raise ReservaInvalidaError(
                    "El cliente de la reserva no es valido."
                )

            # Verificamos que el servicio sea valido.
            if not isinstance(servicio, Servicio):
                raise ReservaInvalidaError(
                    "El servicio de la reserva no es valido."
                )

            # Verificamos que se indique la duracion.
            if duracion is None:
                raise ReservaInvalidaError(
                    "Debe indicar la duracion de la reserva."
                )

            # Creamos la nueva reserva.
            nueva_reserva = Reserva(elemento, servicio, duracion)

            # Guardamos la reserva en la lista.
            self.reservas.append(nueva_reserva)

            logging.info("Reserva agregada al sistema.")

            return nueva_reserva

        # Si es un cliente, lo guardamos en su lista.
        if isinstance(elemento, Cliente):
            self.clientes.append(elemento)
            logging.info("Cliente agregado al sistema.")

        # Si es un servicio, lo guardamos en su lista.
        elif isinstance(elemento, Servicio):
            self.servicios.append(elemento)
            logging.info("Servicio agregado al sistema.")

        # Si es una reserva existente, la guardamos.
        elif isinstance(elemento, Reserva):
            self.reservas.append(elemento)
            logging.info("Reserva agregada al sistema.")

        else:
            raise ValueError(
                "Solo se podran agregar clientes, servicios o reservas."
            )

    # Metodo para consultar los elementos guardados.
    def mostrar(self, tipo=None):
        """Devuelve todas las listas o la lista indicada."""

        # Si no se indica el tipo, devuelve todas las listas.
        if tipo is None:
            return {
                "clientes": self.clientes,
                "servicios": self.servicios,
                "reservas": self.reservas
            }

        # Devuelve la lista de clientes.
        elif tipo == "clientes":
            return self.clientes

        # Devuelve la lista de servicios
        elif tipo == "servicios":
            return self.servicios

        # Devuelve la lista de reservas
        elif tipo == "reservas":
            return self.reservas

        else:
            raise ValueError("El tipo de lista no existe.")


# Ahora se desarrollan las pruebas 9, 10 y 11: reservas.

# Creamos el administrador del sistema.
sistema = SistemaSoftwareFJ()

# Agregamos el cliente y el servicio a sus listas.
sistema.agregar(cliente1)
sistema.agregar(sala1)

# Prueba 9: Crea una reserva valida.
try:
    print("\nPRUEBA 9: Reserva valida")

    # Creamos una reserva con el cliente, servicio y duracion.
    reserva1 = sistema.agregar(cliente1, sala1, 3)

    # Confirmamos la reserva.
    print("El estado de la reserva:", reserva1.confirmar())

    logging.info("La prueba 9 se realizo correctamente.")

except ReservaInvalidaError as error:
    print("Error en la prueba 9:", error)
    logging.error("Error en la prueba 9: %s", error)

except Exception as error:
    print("Error inesperado en la prueba 9:", error)
    logging.error("Error inesperado en la prueba 9: %s", error)


# Prueba 10: Crea una reserva invalida.
try:
    print("\nPRUEBA 10: Reserva invalida")

    # Intentamos crear una reserva con duracion igual a cero.
    reserva2 = sistema.agregar(cliente1, sala1, 0)

    print("Estado de la reserva:", reserva2.estado)

except ReservaInvalidaError as error:
    print("Error en la prueba 10:", error)
    logging.error("Error en la prueba 10: %s", error)

except Exception as error:
    print("Error inesperado en la prueba 10:", error)
    logging.error("Error inesperado en la prueba 10: %s", error)


# Prueba 11: Reserva de un servicio no disponible.
try:
    print("\nPRUEBA 11: Servicio no disponible")

    # Marcamos la sala como no disponible.
    sala1._disponible = False

    reserva3 = sistema.agregar(cliente1, sala1, 2)

    print("Estado de la reserva:", reserva3.estado)

except ServicioNoDisponibleError as error:
    print("Error en la prueba 11:", error)
    logging.error("Error en la prueba 11: %s", error)

except ReservaInvalidaError as error:
    print("Error en la prueba 11:", error)
    logging.error("Error en la prueba 11: %s", error)

except Exception as error:
    print("Error inesperado en la prueba 11:", error)
    logging.error("Error inesperado en la prueba 11: %s", error)

finally:
    # Dejamos la sala disponible otra vez.
    sala1._disponible = True


# Verificamos las listas internas.
print("\nRegistros del sistema")

# Consultamos la cantidad de clientes.
print("La cantidad de clientes:", len(sistema.mostrar("clientes")))

# Consultamos la cantidad de servicios.
print("La cantidad de servicios:", len(sistema.mostrar("servicios")))

# Consultamos la cantidad de reservas.
print("La cantidad de reservas:", len(sistema.mostrar("reservas")))

logging.info("Se hace la verificacion de las listas finalizadas.")
