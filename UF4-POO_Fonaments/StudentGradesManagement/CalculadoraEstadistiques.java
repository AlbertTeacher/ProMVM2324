import java.util.Arrays;

public class CalculadoraEstadistiques
{
    public static double calcularMitjana(double[] notes) {
        double suma = 0.0;

        for (double nota : notes) {
            suma += nota;
        }

        return suma / notes.length;
    }

    public static double calcularMaxim(double[] notes) {
        Arrays.sort(notes);

        return notes[notes.length - 1];
    }

    public static double calcularMinim(double[] notes) {
        Arrays.sort(notes);

        return notes[0];
    }
}
