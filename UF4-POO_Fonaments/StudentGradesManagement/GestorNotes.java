public class GestorNotes
{
    Dictionary<String, double[]> alumnes = new Dictionary<String, double[]>();

    public void registrarNotes(String nomAlumne, double[] notes) {
        alumnes.put(nomAlumne, notes);
    }

    public double[] obtenirNotes(String nomAlumne) {
        return alumnes.get(nomAlumne);
    }
}
