import java.util.HashSet;
import java.util.Set;

public class GestorColores {

    private Set<String> conjuntoColores;

    // Constructor
    public GestorColores() {
        this.conjuntoColores = new HashSet<>();
    }

    // Método para agregar colores al conjunto
    public void agregarColor(String color) {
        conjuntoColores.add(color);
    }

    // Metodo para mostrar la lista de colores. Es lenght porq es una cadena de caracteres
    public void mostrarListaColores() {
        System.out.println("Lista de colores:");
        String[] arrayColores = conjuntoColores.toArray(new String[0]);
        for (int i = 0; i < arrayColores.length; i++) {
            System.out.println(arrayColores[i]);
        }
    }

    // Método para verificar si un color específico existe en el cojunto
    public boolean colorExiste(String color) {
        return conjuntoColores.contains(color);
    }

    public static void main(String[] args) {

        GestorColores gestor = new GestorColores();

        // Agregar colores al conjunto
        gestor.agregarColor("Cian");
        gestor.agregarColor("Amarillo");
        gestor.agregarColor("Morado");

        // Mostrar la lista de colores
        gestor.mostrarListaColores();

        // Verificar la existencia de un color en el conjunto
        System.out.println("¿Cian existe en el conjunto? " + gestor.colorExiste("Cian"));
        System.out.println("¿Marron existe en el conjunto? " + gestor.colorExiste("Marron"));
    }
}
