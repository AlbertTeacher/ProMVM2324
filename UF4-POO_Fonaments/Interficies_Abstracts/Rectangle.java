class Rectangle extends Figura2D {
    double base;
    double altura;

    Rectangle(String nom, double base, double altura) {
        super(nom);
        this.base = base;
        this.altura = altura;
    }

    @Override
    public double calcularArea() {
        return base * altura;
    }

    @Override
    public double calcularPerimetre() {
        return 2 * (base + altura);
    }
}