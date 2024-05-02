# Gestió de notes dels alumnes

Es demana desenvolupar un programa en Java per gestionar les notes dels alumnes d'una classe. 
El programa ha de permetre registrar les notes dels alumnes per a diferents assignatures i calcular estadístiques sobre aquestes notes.

**Registre de notes:**  
Crea una classe anomenada `GestorNotes` amb els següents mètodes:
- `registrarNotes(String nomAlumne, double[] notes)`: Aquest mètode ha de permetre registrar les notes d'un alumne per a una assignatura. El paràmetre nomAlumne indica el nom de l'alumne i el paràmetre notes és un array de tipus double que conté les notes de l'alumne per a l'assignatura.
- `obtenirNotes(String nomAlumne)`: Aquest mètode ha de permetre obtenir les notes d'un alumne registrades anteriorment. Ha de retornar un array de tipus double amb les notes de l'alumne.

**Càlcul d'estadístiques:**  
Crea una classe anomenada CalculadoraEstadistiques amb els següents mètodes:
- `calcularMitjana(double[] notes)`: Aquest mètode ha de calcular la mitjana de les notes donades en l'array notes.
- `calcularMaxim(double[] notes)`: Aquest mètode ha de calcular la nota màxima de les notes donades en l'array notes.
- `calcularMinim(double[] notes)`: Aquest mètode ha de calcular la nota mínima de les notes donades en l'array notes.

**Classe principal Principal:**  
En aquesta classe, crea una instància de `GestorNotes` per gestionar les notes dels alumnes.
- Registra les notes d'alumnes per a diverses assignatures utilitzant el mètode `registrarNotes`.
- Utilitza el mètode `obtenirNotes` per obtenir les notes d'un alumne i mostra-les per pantalla.
- Utilitza els mètodes de la classe `CalculadoraEstadistiques` per calcular la mitjana, el màxim i el mínim de les notes d'un alumne i mostra els resultats per pantalla.