fun leerOperacion(): String {
    return "+"
}

fun leerNumero(): Int {
    return 7
}

fun sumar(primerNumero: Int, segundoNumero: Int) {
    val resultado: Int = primerNumero + segundoNumero

    println(resultado)
}

fun resta(primerNumero: Int, segundoNumero: Int) {
    val resultado: Int = primerNumero - segundoNumero

    println(resultado)
}

fun multiplicacion(primerNumero: Int, segundoNumero: Int) {
    val resultado: Int = primerNumero * segundoNumero

    println(resultado)
}

fun division(primerNumero: Int, segundoNumero: Int) {
    var resultado: Int = 0

    if (segundoNumero == 0) {
        println("No se puede dividir entre 0")
    } else {
        resultado = primerNumero / segundoNumero

        println(resultado)
    }
}

fun usandoIFELSE(operacion: String, primerNumero: Int, segundoNumero: Int) {
    println("Prueba con IF ELSE")
    if (operacion == "+") {
        sumar(primerNumero, segundoNumero)
    } else if (operacion == "-") {
        resta(primerNumero, segundoNumero)
    } else if (operacion == "*") {
        multiplicacion(primerNumero, segundoNumero)
    } else if (operacion == "/") {
        division(primerNumero, segundoNumero)
    } else {
        println("Invalid operacion")
    }
}

fun usandoSWITHCASE(operacion: String, primerNumero: Int, segundoNumero: Int) {
    println("Prueba con SWITCH CASE")
    when (operacion) {
        "+" -> sumar(primerNumero, segundoNumero)
        "-" -> resta(primerNumero, segundoNumero)
        "*" -> multiplicacion(primerNumero, segundoNumero)
        "/" -> division(primerNumero, segundoNumero)
        else -> {
            println("Invalid operacion")
        }
    }
}

fun main() {
   // Debemos leer que operacion hacer
   val operacion: String = leerOperacion()
   // Debemos leer cual es el primer numero
   val primerNumero: Int = leerNumero()
   // Debemos leer cual es el segundo numero
   val segundoNumero: Int = leerNumero()
   // Deberiamos tener un selector que escoja la operacion a invocar
   /*
    * Tenemos dos opciones hacer un grupo de if / else
    * O podriamos hacer un switch
    */
    usandoIFELSE(operacion, primerNumero, segundoNumero)
    usandoSWITHCASE(operacion, primerNumero, segundoNumero)
}