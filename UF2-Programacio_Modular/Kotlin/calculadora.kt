// PRE: El usuario elige que operacion quiere hacer y que valores se van a calcuar
fun pedirOperacion(): String {
	println("Que operacion quieres hacer? '+', '-', '*', '/':")
	var operacion: String? = readLine()

	if (operacion == null) {
		operacion = ""
	}

	return operacion
}

fun pedirNumero(): Int {
	print("Introduce un numero: ")
	var numero: Int = readLine()!!.toInt()

	return numero
}

fun sumar(primerOperando: Int, segundoOperando: Int): Int {
	var resultado: Int = primerOperando + segundoOperando

	return resultado
}

fun resta(primerOperando: Int, segundoOperando: Int): Int {
	var resultado: Int = primerOperando - segundoOperando

	return resultado
}

fun multiplicar(primerOperando: Int, segundoOperando: Int): Int {
	var resultado: Int = primerOperando * segundoOperando

	return resultado
}

fun dividir(primerOperando: Int, segundoOperando: Int): Int {
	var resultado: Int = 0

	if (segundoOperando == 0) {
		println("No se puede dividir entre zero")
	} else {
		resultado = primerOperando / segundoOperando
	}

	return resultado
}

fun selecConIFELSE(operacion: String, primerOperando: Int, segundoOperando: Int): Int {
	println("Selecciono con un IF ELSE")
	var resultado: Int = 0

	if (operacion == "+") {
		resultado = sumar(primerOperando, segundoOperando)
	} else if (operacion == "-") {
		resultado = resta(primerOperando, segundoOperando)
	} else if (operacion == "*") {
		resultado = multiplicar(primerOperando, segundoOperando)
	} else if (operacion == "/") {
		resultado = dividir(primerOperando, segundoOperando)
	} else {
		println("Operacion no permitida")
	}

	return resultado
}

fun selecConSWITCH(operacion: String, primerOperando: Int, segundoOperando: Int): Int {
	println("Selecciono con un SWITCH")
	var resultado: Int = 0

	when(operacion) {
		"+" -> resultado = sumar(primerOperando, segundoOperando)
		"-" -> resultado = resta(primerOperando, segundoOperando)
		"*" -> resultado = multiplicar(primerOperando, segundoOperando)
		"/" -> resultado = dividir(primerOperando, segundoOperando)
	}

	return resultado
}

fun main() {
	/*
	 * Primero le preguntaremos al usuario que operacion quiere hacer
	 */
	val operacion: String = pedirOperacion()

	// Le pediremos que nos introduzca un numero
	val primerOperando: Int = pedirNumero()

	// Le pediremos que nos introduzca un segundo numero
	val segundoOperando: Int = pedirNumero()

	// Escogeremos que accion debemos ejecutar segun la operacion deseada
	val resultado1: Int = selecConIFELSE(operacion, primerOperando, segundoOperando)
	val resultado2: Int = selecConSWITCH(operacion, primerOperando, segundoOperando)

	// Imprimiremos el resultado
	println(resultado1)
	println(resultado2)
}
// POST: Retorna el resultado de la operacion realizada
