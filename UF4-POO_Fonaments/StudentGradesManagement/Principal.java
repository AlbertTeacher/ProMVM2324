import java.util.Scanner;

public class Principal
{
    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        // Registrar les notes dels alumnes per a diverses assignatures
        GestorNotes gestor = new GestorNotes();
        obtenerNotas(gestor);
        // Obtenir notes d'un alumne i mostrar per pantalla
        double[] notes = notasDeAlumno(gestor);
        // Calcular mitjana, maxim i minim de les notes d'un alumnes i mostrar
        estadistiques(notes);
        sc.close();
    }

    private static void estadistiques(double[] notes) {
        System.out.println("Nota mitjana:");
        System.out.println(CalculadoraEstadistiques.calcularMitjana(notes));
        System.out.println("Nota maxima:");
        System.out.println(CalculadoraEstadistiques.calcularMaxim(notes));
        System.out.println("Nota minima:");
        System.out.println(CalculadoraEstadistiques.calcularMinim(notes));
    }

    private static double[] notasDeAlumno(GestorNotes gestor) {
        System.out.println("Escriu el nom de l'alumne a veure les notes:");
        String alumne = sc.next();
        double[] notes = gestor.obtenirNotes(alumne);

        for (double nota : notes) {
            System.out.println(nota);
        }

        return notes;
    }

    private static void obtenerNotas(GestorNotes gestor) {
        System.out.println("Quants alumnes vols introduir?");
        int alumnes = sc.nextInt();
        System.out.println("Quantes assignatures hi han?");
        int assingatures = sc.nextInt();

        for (int i = 0; i < alumnes; i++) {
            System.out.println("Nom alumne:");
            String alumne = sc.next();
            double[] notes = new double[assingatures];

            for (int j = 0; j < assingatures; j++) {
                System.out.println("Introdueix la nota:");
                double nota = sc.nextDouble();
                notes[j] = nota;
            }

            gestor.registrarNotes(alumne, notes);
        }
    }
}
