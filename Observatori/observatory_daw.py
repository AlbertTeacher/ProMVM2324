# Registre de temperatures
temperatures = []
mes = 1
dia = 1

# Problema general
def inici():
    ...

# Primer nivell de descomposicio
def mostrar_menu():
    ...

def tractar_opcio():
    ...

# Segon nivell de descomposicio
def registre_temperatures_setmanals():
    ...

def mostrar_mitjana():
    ...

def mostrar_diferencia():
    ...

def finalitzar_execucio():
    ...

# Tercer nivell de descomposicio
def llegir_temperatures_teclat():
    lector = input("Escriu les temperatures d'aquesta setmana: ")
    for temperatura in lector.split():
        temperatures.append(float(temperatura.replace(',','.')))

def calcular_mitjana():
    suma = 0
    for temperatura in temperatures:
        suma += temperatura
    
    return suma/len(temperatures)

def calcular_diferencia():
    # temperatura minima
    #temepratura maxima
    # recorrer todas las temperaturas e ir modificando

def mostrar_data():
    print(dia, "de", end=' ')
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
    dies_mes_actual = 0
    if mes == 2:
        dies_mes_actual = 28
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dies_mes_actual = 30
    else:
        dies_mes_actual = 31
    dia += 7
    if dia > dies_mes_actual:
        dia -= dies_mes_actual
        mes += 1
        if mes > 12:
            mes = 1

mostrar_data()
