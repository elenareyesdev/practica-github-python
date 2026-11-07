# Importamos logging para registrar los eventos y errores
import logging

# Importamos math para validar los numeros.
import math


# Excepcion para indicar que los datos de la reserva no son validos.
class ReservaInvalidaError(Exception):
    pass


# Creamos la clase que sera reserva.
class Reserva:

    # Inicializamos los datos de la reserva
    def __init__(self, cliente, servicio, duracion):

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

    def confirmar(self):

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

    def cancelar(self):

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
