class Main {
    public static void main(String[] args) {
        // Crear Cercle i crear Rectangle
        Cercle cercle = new Cercle("Cercle", 5);
        Rectangle rectangle = new Rectangle("Rectangle", 4, 3);

        // Mostrar area i perimetre de cada figura
        imprimirDatos(cercle);
        imprimirDatos(rectangle);
    }

    private static void imprimirDatos(Figura2D figura) {
        System.out.println("El area del :" + figura.nom + ": " + figura.calcularArea());
        System.out.println("El perimetro del :" + figura.nom + ": " + figura.calcularPerimetre());
    }
}