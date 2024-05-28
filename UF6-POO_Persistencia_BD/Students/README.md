## Students

### 1. Crear el projecte a VSCode

1. **Crear el Directori del Projecte**:
Crea un directori per al teu projecte, per exemple, `JavaDatabaseExample`.
2. **Configurar l'Estructura del Projecte**:
Crea l'estructura de directoris següent:
    
    ```
    JavaDatabaseExample/
    ├── src/
    │   └── main/
    │       └── java/
    │           └── com/
    │               └── example/
    │                   └── database/
    │                       ├── Main.java
    │                       ├── DatabaseManager.java
    │                       └── models/
    │                           └── Student.java
    └── lib/
    
    ```
    
3. **Afegir el Connector JDBC**:
Col·loca el connector JDBC de PostgreSQL al directori `lib`.

### 2. Escriure el codi Java

### 2.1 Main.java

Aquest serà el punt d'entrada de l'aplicació.

```java
package com.example.database;

public class Main {
    public static void main(String[] args) {
        DatabaseManager dbManager = new DatabaseManager();
        dbManager.connect();

        // Crear un nou estudiant
        Student student = new Student(1, "Joan", "Garcia");
        dbManager.addStudent(student);

        // Recuperar estudiant
        Student retrievedStudent = dbManager.getStudent(1);
        System.out.println(retrievedStudent);

        // Actualitzar estudiant
        student.setLastName("Martínez");
        dbManager.updateStudent(student);

        // Eliminar estudiant
        dbManager.deleteStudent(1);

        dbManager.disconnect();
    }
}

```

### 2.2 DatabaseManager.java

Aquest fitxer gestionarà la connexió a la base de dades i les operacions CRUD.

### 2.3 Student.java

Aquest fitxer definirà la classe `Student`.

### 3. Crear la taula a PostgreSQL

Abans d'executar el codi, necessitaràs crear la taula `students` a la teva base de dades PostgreSQL.

### 4. Executar el projecte

1. **Obrir VSCode i carregar el projecte**.
2. **Compilar i executar el projecte**.

### Com compilar i executar des de CLI

```bash
cd JavaDatabaseExample/src/main/Java
javac -cp ".:../../../lib/postgresql-42.7.3.jar" **/*.java
java -cp ".:../../../lib/postgresql-42.7.3.jar" com.example.database.Main
```