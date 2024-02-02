libros = []
prestecs = []
fin = False

def add_to_list(texto, lista):
    elemento = input(texto)
    lista.append(elemento)

def del_to_lit(texto, lista):
    eliminar = input(texto)
    for elemento in lista:
        if elemento == eliminar:
            lista.remove(elemento)

def print_list(lista):
    for elemento in lista:
        print(elemento)

while fin == False:
    opcion = input("Que deseas hacer? A: Add new book, B: Show all books, C: Delete one book. D: Exit, E: Prestar, F: Mostrar prestamos, G: Devolver\n")
    opcion = opcion.upper()

    if (opcion == 'A'):
        add_to_list("Titulo del libro: ", libros)
    elif (opcion == 'B'):
        print_list(libros)
    elif (opcion == 'C'):
        del_to_lit("Titulo del libro a eliminar: ", libros)
    elif (opcion == 'D'):
        fin = True
    elif (opcion == 'E'):
        add_to_list("Titulo del libro a prestar: ", prestecs)
    elif (opcion == 'F'):
        print_list(prestecs)
    elif (opcion == 'G '):
        del_to_lit("Titulo del libro a devolver: ", prestecs)