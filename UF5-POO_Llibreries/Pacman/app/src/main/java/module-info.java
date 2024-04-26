module pacman {
    requires javafx.controls;
    requires javafx.fxml;
    requires transitive javafx.graphics;

    opens com.example.pacman to javafx.fxml;

    exports com.example.pacman;
}