frase_actual = ''
frase_mes_as = ''
max_as = 0
fi = False

def inici():
    while not fi:
        processar_frase()
        mostrar_resultat_actual()
    print("(El programa acaba)")

def processar_frase():
    global frase_actual, fi
    frase_actual = input('Escriu una frase:\n> ')
    if frase_actual == 'fi':
        fi = True
    else:
        comparar_as()

def mostrar_resultat_actual():
    print("La frase amb mes a's es: \"", frase_mes_as, "\"", sep="")
    print("Te", max_as, " a's.")

def comparar_as():
    global frase_mes_as, max_as
    num_as = frase_actual.casefold().count('a')

    if num_as > max_as:
        max_as = num_as
        frase_mes_as = frase_actual

inici()