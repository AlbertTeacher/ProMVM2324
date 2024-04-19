package Biblioteca 

class Prestamo(val libro: Libro, val socio: Socio)
{
    fun registrarPrestamo(fechaPrestamo: String) {
        println("Préstamo registrado - Libro: ${libro.titulo}, Socio: ${socio.nombre} ${socio.apellido}, Fecha: $fechaPrestamo")
        libro.prestar()
    }

    fun devolverPrestamo() {
        println("Devolución de préstamo - Libro: ${libro.titulo}, Socio: ${socio.nombre} ${socio.apellido}")
        libro.devolver()
    }

    fun informacion() {
        println("Libro: ${libro.titulo}, Socio: ${socio.nombre} ${socio.apellido}")
    }
}
