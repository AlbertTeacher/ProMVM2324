fun mostrarMenu() {
	println("---- Menu ----")
	println("1. Afegiu un viatge")
	println("2. Consultar Viatges")
	println("3. Detalls Viatge")
	println("4. Registrar Client")
	println("5. Fer Reserva")
	println("6. Detalls Reserva")
}

fun leerOpcio(): Int {
	print("Selecciona una opcio: ")
	val opcio = readLine()!!.toInt()

	return opcio
}

fun afegirViatge() {
	print("Introdueix la destinacio del viatge: ")
	val destinacio = readLine()
	print("Introdueix el preu del viatge: ")
	val preu: Float = readLine()?.toFloatOrNull() ?: 0.0f
	println(preu)
}

fun executarOpcio(opcio: Int) {
	when (opcio) {
		1 -> afegirViatge()
		else -> println("Opcio no valida")
	}
}

fun main() {
	mostrarMenu()
	val opcio = leerOpcio()
	executarOpcio(opcio)
}
