# Observatori

Es vol fer un gestor de registre de temperatures preses setmanalment per un observatori. 

Es pressuposa que el programa es posa en marxa a l’inici de l’any (1 de gener) i al principi de cada setmana. Al llarg de 52 setmanes que té un any, es van enregistrant les temperatures mesurades cada dia de la setmana anterior (o sigui, set en total cada vegada). 

Cada cop que es fa un registre, sabent que ha passat una setmana, el programa calcula automàticament quin dia i mes és l’actual. A partir d’aquestes dades, és possible consultar en qualsevol moment quina ha estat la temperatura mitjana i la diferència entre el valor màxim i mínim enregistrats. En fer-ho, la data actual també es mostra en pantalla.

Totes aquestes accions es porten a terme usant un menú. 
Evidentment, l’aplicació ha de ser prou robusta com per tractar casos erronis (per exemple, consultar valors quan encara no hi ha cap data enregistrada, o intentar registrar com a temperatura valors de tipus incorrecte).

Per deixar més clar el comportament esperat, tot seguit es mostra un prototip del que s’esperaria mostrar amb la seva execució:


```
Benvingut al registre de temperatures 
------------------------------------- 
[RT] Registrar temperatures setmanals. 
[MJ] Consultar temperatura mitjana. 
[DF] Consultar diferència màxima. 
[FI] Sortir. 
Opció: MJ 
No hi ha temperatures registrades.
``` 
```
 Benvingut al registre de temperatures 
------------------------------------- 
[RT] Registrar temperatures setmanals. 
[MJ] Consultar temperatura mitjana. 
[DF] Consultar diferència màxima. 
[FI] Sortir. 
Opció: RT 
Escriu les temperatures d'aquesta setmana: 
20,5 21,1 21 21,7 20,9 20,6 19,9 
```
```
 Benvingut al registre de temperatures 
------------------------------------- 
[RT] Registrar temperatures setmanals. 
[MJ] Consultar temperatura mitjana. 
[DF] Consultar diferència màxima. 
[FI] Sortir. 
Opció: MJ 
Fins avui 8 de gener la mitjana ha estat de 20.814285 graus. 
```
```
 Benvingut al registre de temperatures 
------------------------------------- 
[RT] Registrar temperatures setmanals. 
[MJ] Consultar temperatura mitjana. 
[DF] Consultar diferència màxima. 
[FI] Sortir. 
Opció: DF 
Fins avui 8 de gener la diferència màxima ha estat de 1.8000011 graus. 
```
```
 Benvingut al registre de temperatures 
------------------------------------- 
[RT] Registrar temperatures setmanals. 
[MJ] Consultar temperatura mitjana. 
[DF] Consultar diferència màxima. 
[FI] Sortir.
Opció: FI
```
