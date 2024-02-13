# Registre de temperatures
temperatures = []
mes = 1
dia = 1
fi = False

# Problema general
def inici():
    while not fi:
        mostrar_menu()
        tractar_opcio()

# Primer nivell de descomposicio
def mostrar_menu():
    print("Benvingut al registre de temperatures")
    print("-------------------------------------")
    print("[RT] Registrar temperatures setmanas.")
    print("[MJ] Consultar temperatura mitjana.")
    print("[DF] Consultar diferencia maxima.")
    print("[FI] Sortir.")

def tractar_opcio():
    opcio = input("Opcio: ")
    if opcio.casefold() == "RT".casefold():
        registre_temperatures_setmanals()
    elif opcio.casefold() == "MJ".casefold():
        mostrar_mitjana()
    elif opcio.casefold() == "DF".casefold():
        mostrar_diferencia()
    elif opcio.casefold() == "FI".casefold():
        finalitzar_execucio()
    else:
        print("Opcio incorrecta!")

# Segon nivell de descomposicio
def registre_temperatures_setmanals():
    if (len(temperatures) + 7) > (52*7):
        print("Ja tenim totes les setmanes introudides no podem introduir mes.")
    else:
        llegir_temperatures_teclat()
        incrementar_data()

def mostrar_mitjana():
    if len(temperatures) > 0:
        mitjana = calcular_mitjana()
        print("Fins avui", end=" ")
        mostrar_data()
        print("la mitjana ha estat de", mitjana, "graus.")
    else:
        print("No hi ha temperatures registrades.")

def mostrar_diferencia():
    if len(temperatures) > 0:
        diferencia = calcular_diferencia()
        print("Fins avui", end=" ")
        mostrar_data()
        print("la diferencia maxima ha estat de", diferencia, "graus.")
    else:
        print("No hi ha temperatures registrades.")

def finalitzar_execucio():
    global fi
    fi = True

# Tercer nivell de descomposicio
def llegir_temperatures_teclat():
    lector = input("Escriu les temperatures d'aquesta setmana:\n")
    for temperatura in lector.split():
        temperatures.append(float(temperatura.replace(',','.')))

def calcular_mitjana():
    suma = 0
    for temperatura in temperatures:
        suma += temperatura
    
    return suma/len(temperatures)

def calcular_diferencia():
    minima = temperatures[0]
    maxima = temperatures[0]

    for temperatura in temperatures:
        if minima > temperatura:
            minima = temperatura
        if maxima < temperatura:
            maxima = temperatura
    
    return maxima - minima

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
    global mes, dia
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

inici()
