public interface Vehicle {
    // Métode per augmentar la velocidat del vehícle a la velocidat especificada en kilómetres per hora.
    public void accelerar(int velocidat);

    // Métode per reduir la velocitat del vehícle
    public void frenar();

    // Métode per obtenir la velocitat actual del vehícle en kilómetres per hora.
    public void obtenerVelocidadActual();
}
