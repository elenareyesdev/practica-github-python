# Software FJ - Sistema de gestión de clientes, servicios y reservas

Ejercicio colaborativo del curso Programación, Fase 4.
Universidad Nacional Abierta y a Distancia (UNAD).

## Archivo principal
`main.py` es el programa final. Los demás archivos son versiones anteriores y documentos compartidos del trabajo.

## Cómo ejecutarlo
1. Instalar Python.
2. Descargar `main.py`.
3. Abrir una terminal en la carpeta del archivo y ejecutar: `python main.py`
4. Se crea el archivo `registro.log` con los eventos y errores.

## contiene
- Clases abstractas `Entidad` y `Servicio`
- Clases `Cliente`, `Sala`, `AlquilerEquipo`, `Asesoria` y `Reserva`
- Excepciones personalizadas y manejo con try/except/else/finally y encadenamiento
- Registro de eventos y errores en `registro.log`
- Listas internas de clientes, servicios y reservas y la clase `SistemaSoftwareFJ`
- 11 simulaciones, válidas e inválidas

## Estructura del repositorio
- `main.py`: programa final
- `versiones-anteriores/`: código de etapas previas
- `trabajo colaborativo programacion/`: primer borrador de la clase Reserva
- Documento de avances del trabajo (Word)

## Integrantes
- **elenareyesdev**: log, excepciones, `Entidad`, `Cliente`, `Servicio` y servicios hijos, pruebas 1 a 8 y 11, correcciones e integración
- **villegascamilo70-ctrl**: clase `Reserva`, listas internas y pruebas 9 y 10
