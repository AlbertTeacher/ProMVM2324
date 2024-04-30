# Empleats

En una empresa cal gestionar la informació de diferents tipus d'empleats. Cada tipus de treballador té característiques i càlculs de salari específics. Es requereix un sistema Java que permeti representar aquesta informació utilitzant herència.

1. Defineix una classe base anomenada **Empleat** que representi un empleat genèric a l'empresa. Aquesta classe ha de tenir els atributs i mètodes següents:
    - Atributs: **nom** (String) i **salari** (double).
    - Constructor per inicialitzar els atributs.
    - Mètode **imprimirDetalles()** per imprimir els detalls de l'empleat, mostrant el nom i el salari.

2. Crea classes filles per representar diferents tipus d'empleats:
    - **EmpleadoPorHoras**: Representa un empleat que cobra per hores treballades. Ha de tenir els atributs i mètodes addicionals següents:
      - Atributs: **horesTreballades** (int) i **tarifaPorHora** (double).
      - Constructor per inicialitzar els atributs.
      - Mètode **calcularSalario()** per calcular el salari en funció de les hores treballades i la tarifa per hora.

    - **EmpleadoAsalariado**: Representa un empleat que rep un salari fix mensual. No teniu atributs ni mètodes addicionals.

    - **EmpleadoPorComision**: Representa un empleat que rep un salari base més una comissió per vendes realitzades. Ha de tenir els atributs i mètodes addicionals següents:
      - Atributs: **vendesRealizadas** (double) i **comisionPorVenta** (double).
      - Constructor per inicialitzar els atributs.
      - Mètode **calcularSalario()** per calcular el salari en funció de les vendes realitzades i la comissió per venda.

3. Crea una classe principal anomenada **Main** on puguis provar les diferents classes. Crea instàncies de cada tipus d'empleat, calcula'n els salaris utilitzant els mètodes corresponents i mostra els detalls de cada empleat utilitzant el mètode **imprimirDetalles()**.