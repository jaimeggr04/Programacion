import java.util.HashSet;
import java.util.Set;

class Estudiante {
    private String nombre;
    private int numeroIdentificacion;

    // Constructor
    public Estudiante(String nombre, int numeroIdentificacion) {
        this.nombre = nombre;
        this.numeroIdentificacion = numeroIdentificacion;
    }

    // Método equals y hashCode para verificar la igualdad en el conjunto
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Estudiante estudiante = (Estudiante) obj;
        return numeroIdentificacion == estudiante.numeroIdentificacion;
    }

    @Override
    public int hashCode() {
        return Integer.hashCode(numeroIdentificacion);
    }

    // Método toString
    @Override
    public String toString() {
        return "Estudiante [Nombre=" + nombre + ", Número de Identificación=" + numeroIdentificacion + "]";
    }
}

public class GestorEstudiantes {

    private Set<Estudiante> conjuntoEstudiantes;

    // Constructor
    public GestorEstudiantes() {
        this.conjuntoEstudiantes = new HashSet<>();
    }

    // Método para agregar estudiantes al conjunto
    public void agregarEstudiante(Estudiante estudiante) {
        conjuntoEstudiantes.add(estudiante);
    }

    // Método para mostrar la lista de estudiantes
    public void mostrarListaEstudiantes() {
        System.out.println("Lista de Estudiantes:");
        for (Estudiante estudiante : conjuntoEstudiantes) {
            System.out.println(estudiante);
        }
    }

    // Método para verificar si un estudiante específico existe en el conjunto
    public boolean estudianteExiste(Estudiante estudianteBuscado) {
        for (Estudiante estudiante : conjuntoEstudiantes) {
            if (estudiante.equals(estudianteBuscado)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        // Crear GestorEstudiantes
        GestorEstudiantes gestor = new GestorEstudiantes();

        // Agregar estudiantes al conjunto
        Estudiante estudiante1 = new Estudiante("Jaime García", 30290434);
        Estudiante estudiante2 = new Estudiante("Pablo Galve", 6789044);

        gestor.agregarEstudiante(estudiante1);
        gestor.agregarEstudiante(estudiante2);

        // Mostrar la lista de estudiantes
        gestor.mostrarListaEstudiantes();

        // Verificar la existencia de un estudiante en el conjunto
        Estudiante estudianteBuscado = new Estudiante("Jaime García", 30290434);
        System.out.println("¿Estudiante existe en el conjunto? " + gestor.estudianteExiste(estudianteBuscado));
    }
}