# Sistema de gestió de productes en una botiga

Es demana crear un sistema de gestió de productes per a una botiga que veuen diferents tipus de productes amb característiques i comportaments específics. L'objectiu és implementar aquest sistema a Java utilitzant herència i polimorfisme.

1. Classe base Producte:
    - Defineix una classe base abstracta anomenada `Producte` amb els següents atributs:
      - `codi`: int
      - `nom`: String
      - `preu`: double
    - La classe ha de tenir un constructor per inicialitzar els atributs i un mètode abstracte `calcularPreuFinal()` que calculi el preu final del producte.

2. Classes fills per a tipus específics de productes:
    - Crea les següents classes filles que heretin de la classe `Producte`:
      - `Aliment`: Representa un producte alimentari amb una data de caducitat.
            - Aquesta classe ha de tenir un atribut addicional `dataCaducitat` i un mètode per establir aquesta data.
            - Implementa el mètode `calcularPreuFinal()` per aplicar els descomptes o recàrrecs segons la proximitat a la data de caducitat.
      - Electrodomestic: Representa un electrodomèstic amb una garantia en mesos.
            - Aquesta classe ha de tenir un atribut addicional `mesosGarantia` i un mètode per establir aquesta garantia.
            - Implementa el mètode `calcularPreuFinal()` per aplicar els descomptes o recàrrecs segons la durada de la garantia.
      - `Llibre`: Representa un llibre amb un autor i un nom de pàgines.
            - Aquesta classe ha de tenir atributs addicionals `autor` i `numPagines`.
            - Implementa el mètode `calcularPreuFinal()` per aplicar els descomptes o recàrrecs segons el nom de pàgines.

3. Classe Botiga:
    - Defineix una classe `Botiga` que tingui una llista de productes i mètodes per afegir productes, calcular el preu total i mostrar els detalls de tots els productes.

4. Classe principal `Principal`:
    - A la classe principal, crea una instància de la classe `Botiga`.
    - Afegeix diferents tipus de productes a la botiga.
    - Calcula el preu total de la botiga i mostra els detalls de tots els productes.