class Libro(val titulo: String, val autor: String, var ejemplaresDisponibles: Int) {

    fun prestar() {
        if (ejemplaresDisponibles > 0) {
            ejemplaresDisponibles--
            println("Libro prestado: $titulo, Autor: $autor")
        } else {
            println("No hay ejemplares disponibles de $titulo")
        }
    }

    fun devolver() {
        ejemplaresDisponibles++
        println("Libro devuelto: $titulo, Autor: $autor")
    }

    fun informacion() {
        println("Título: $titulo, Autor: $autor, Ejemplares Disponibles: $ejemplaresDisponibles")
    }
}

class Socio(val nombre: String, val apellido: String, val numeroSocio: Int) {

    fun solicitarPrestamo(libro: Libro, fechaPrestamo: String) {
        println("Préstamo solicitado por $nombre $apellido, Número de Socio: $numeroSocio")
        val prestamo = Prestamo(libro, this)
        prestamo.registrarPrestamo(fechaPrestamo)
    }

    fun devolverPrestamo(libro: Libro) {
        println("Devolución de préstamo por $nombre $apellido, Número de Socio: $numeroSocio")
        val prestamo = Prestamo(libro, this)
        prestamo.devolverPrestamo()
    }

    fun informacion() {
        println("Nombre: $nombre, Apellido: $apellido, Número de Socio: $numeroSocio")
    }
}

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

class App {
	fun exec() {
		// Crear libros
		var libro1: Libro = Libro("LOTR", "J.R.R. Tolkien", 5)
		var libro2: Libro = Libro("1984", "George Orwell", 3)

		// Crear socios
		val socio1 = Socio("Clark", "Kent", 101)
		val socio2 = Socio("Bruce", "Wayne", 102)

		// Realizar acciones
		libro1.informacion()
		socio1.solicitarPrestamo(libro1, "2024-03-01")
		libro1.informacion()
		libro2.informacion()
		socio2.solicitarPrestamo(libro2, "2024-03-01")
		libro2.informacion()
		libro1.informacion()
		socio1.devolverPrestamo(libro1)
		libro1.informacion()

	}
}

fun main() {
	App().exec()
}
