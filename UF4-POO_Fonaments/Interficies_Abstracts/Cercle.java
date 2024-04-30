import java.utils.Math;

class Cercle extends Figura2D {
    double radi;

    Cercle(String nom, double radi) {
        super(nom);
        this.radi = radi;
    }

    @Override
    public double calcularArea() {
        return radi * radi * Math.PI;
    }

    @Override
    public double calcularPerimetre() {
        return 2 * radi * Math.PI;
    }
}