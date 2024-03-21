import Biblioteca.Libro
import Biblioteca.Socio

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
