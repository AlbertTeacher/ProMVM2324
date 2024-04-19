import Biblioteca.Libro

fun main() {
    var libro1: Libro = Libro()
    println("Hello World!")
}

fun factorial(num) {
    if(num > 0) {
        num = num * factorial(num - 1)
    } else {
        num = 1
    }
    return num
}
4*6
        3*2
        2*1