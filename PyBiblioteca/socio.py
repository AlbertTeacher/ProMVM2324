from libro import Libro
from prestamo import Prestamo

class Socio:
    def __init__(self, nombre: str, apellido: str, identificador: int):
        self.nombre = nombre
        self.apellido = apellido
        self.identificador = identificador

    def solicitar_prestamo(self, libro: Libro, fecha_prestamo: str):
        print(f"Prestamo solicitado por {self.nombre} {self.apellido}, id: {self.identificador}")
        prestamo: Prestamo(libro, self)
        prestamo.registrar_prestamo(fecha_prestamo)

    def devolver_prestamo(self):
        print(f"Devolucion de prestamo por {self.nombre} {self.apellido}, id: {self.identificador}")
        prestamo: Prestamo(libro, self)
        prestamo.devolver_prestamo()

    def informacion(self):
        print(f"nombre: {self.nombre}, apellido: {self.apellido}, numero de socio: {self.identificador}")
