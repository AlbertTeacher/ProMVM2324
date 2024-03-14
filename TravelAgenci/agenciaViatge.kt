fun mostrarMenu() {
	println("--- Menu ---")
	println("1. Afegiu un viatge")
	println("2. Consultar viatges")
	println("3. Detalls viatge")
	println("4. Registrar client")
	println("5. Fer reserva")
	println("6. Detalls reserva")
	println("7. Sortir del programa")
}

fun leerOpcio(): Int {
	print("Selecciona una opcio: ")
	val opcio:Int = readLine()?.toIntOrNull()!!

	return opcio
}

fun afegirViatge(viatges: MutableList<Map<String, Double>>) {
	print("Introdueix la destinacio del viatge: ")
	val destinacio: String = readLine()!!
	print("Introudeix el preu del viatge: ")
	val preu: Double = readLine()?.toDoubleOrNull() ?: 0.0
	val viatge: Map<String, Double> = mapOf(destinacio to preu)
	viatges.add(viatge)
}

fun consultarViatges(viatges: MutableList<Map<String, Double>>) {
	println("Llista de viatges:")
	viatges.forEach { viatge ->
		viatge.forEach { (destinacio, preu) ->
			println("Destinacio: ${destinacio}, Preu: ${preu}")
		}
	}
}

fun demanarDestinacio(): String {
	print("Introudueix el desti: ")
	val destinacio: String = readLine()!!

	return destinacio
}

fun detallsViatge(viatges: MutableList<Map<String, Double>>) {
	val destinacio: String = demanarDestinacio()
	val viatge = viatges.find {it.keys.find { it == destinacio } != null} 
	if (viatge != null) {
		println("Detalls del viatge:")
		viatge.forEach { (desti, preu) ->
			println("- Destinacio: ${desti}")
			println("- Preu: ${preu}")
		}
	} else {
		println("No hi ha cap viatge amb aquest desti")
	}
}

fun registrarClient(clients: MutableList<Pair<Int, String>>) {
	print("Introdueix el nom del client: ")
	val nom: String = readLine() ?: ""
	val id: Int = clients.size + 1
	clients.add(id to nom)
}

fun ferReserva() {

}

fun executarOpcio(opcio: Int, viatges: MutableList<Map<String, Double>>, clients: MutableList<Pair<Int, String>>) {
	when (opcio) {
		1 -> afegirViatge(viatges)
		2 -> consultarViatges(viatges)
		3 -> detallsViatge(viatges)
		4 -> registrarClient(clients)
		5 -> ferReserva()
		7 -> println("Sortint de l'aplicacio")
		else -> println("Opcio no valida")
	}
}

fun main() {
	var viatges: MutableList<Map<String, Double>> = mutableListOf<Map<String, Double>>()
	var clients: MutableList<Pair<Int, String>> = mutableListOf<Pair<Int, String>>()
	do {
		mostrarMenu()
		val opcio: Int = leerOpcio()
		executarOpcio(opcio, viatges, clients)
	} while (opcio != 7)
}
