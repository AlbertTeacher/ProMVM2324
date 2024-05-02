import java.util.Scanner;

public class Principal
{
    public static void main(String[] args) {
        // Registrar les notes dels alumnes per a diverses assignatures
        GestorNotes gestor = new GestorNotes();
        // Obtenir notes d'un alumne i mostrar per pantalla
        System.out.println("Escriu el nom de l'alumne a veure les notes:");
        String alumne = Scanner(System.in);
        double[] notes = gestor.obtenirNotes(alumne);
        for (double nota : notes) {
            System.out.println(nota);
        }
        // Calcular mitjana, maxim i minim de les notes d'un alumnes i mostrar
    }

    private static obtenerNotas(GestorNotes gestor) {
        System.out.println("Quants alumnes vols introduir?");
        int alumnes = Scanner(System.in);
        System.out.println("Quantes assignatures hi han?");
        int assingatures = Scanner(System.in);
        for (int i = 0; i < alumnes; i++) {
            System.out.println("Nom alumne:");
            String alumne = Scanner(System.in);
            double[] notes = new double[assingatures];
            for (int j = 0; j < assingatures; j++) {
                System.out.println("Introdueix la nota:");
                double nota = Scanner(System.in);
                notes[j] = nota;
            }
            gestor.registrarNotes(alumne, notes);
        }
    }
}
