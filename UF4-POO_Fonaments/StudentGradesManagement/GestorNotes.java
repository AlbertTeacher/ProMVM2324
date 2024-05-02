import java.util.Hashtable;

public class GestorNotes
{
    Hashtable<String, double[]> alumnes = new Hashtable<String, double[]>();

    public void registrarNotes(String nomAlumne, double[] notes) {
        alumnes.put(nomAlumne, notes);
    }

    public double[] obtenirNotes(String nomAlumne) {
        return alumnes.get(nomAlumne);
    }
}
