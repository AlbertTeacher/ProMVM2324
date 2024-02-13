#Registre de temperatures
temperatures = []
dia = 1
mes = 1

def mostrar_menu():
    ...

def tractar_opcio():
    ...

def resgistre_temperatures_setmanas():
    if len(temperatures) >= (52 * 7):
        print("Ja tenim totes les temperatures apuntades.")
    else:
        llegir_temperatures_teclat()
        incrementar_data()
        
def mostrar_mitjana():
    ...

def mostrar_diferencia():
    ...

def finalitzar_execucio():
    ...

def llegir_temperatures_teclat():
    lector = input("Escriu les temperatures d'aquesta setmana: ")
    for temperatura in lector.split():
        temperatures.append(float(temperatura.replace(',','.')))

def calcula_diferencia():
    maxima = temperatures[0]
    minima = temperatures[0]

    for temperatura in temperatures:
        if temperatura < minima:
            minima = temperatura
        if temperatura > maxima:
            maxima = temperatura
    
    return maxima - minima

def calcular_mitjana():
    suma = 0
    for temperatura in temperatures:
        suma += temperatura
    return suma / len(temperatures)

def mostrar_data():
    print(dia, "de", end=" ")
    if mes == 1:
        print("Gener")
    elif mes == 2:
        print("Febrer")
    elif mes == 3:
        print("Març")
    elif mes == 4:
        print("Abril")
    elif mes == 5:
        print("Maig")
    elif mes == 6:
        print("Juny")
    elif mes == 7:
        print("Juliol")
    elif mes == 8:
        print("Agost")
    elif mes == 9:
        print("Setembre")
    elif mes == 10:
        print("Octubre")
    elif mes == 11:
        print("Novembre")
    elif mes == 12:
        print("Desembre")

def incrementar_data():
    diesAquestMes = 0

    if mes == 2:
        diesAquestMes = 28
    elif mes in [4, 6, 9, 11]:
        diesAquestMes = 30
    else:
        diesAquestMes = 31

    dia += 7

    if dia > diesAquestMes:
        dia = dia - diesAquestMes
        mes += 1

        if mes > 12:
            mes = 1
