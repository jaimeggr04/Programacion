import java.util.HashMap;
import java.util.Map;

class Empleado {
    private String nombre;
    private double salario;

    // Constructor
    public Empleado(String nombre, double salario) {
        this.nombre = nombre;
        this.salario = salario;
    }

    @Override
    public String toString() {
        return "Empleado [Nombre=" + nombre + ", Salario=" + salario + "]";
    }
}

public class GestorEmpleados {

    private Map<String, Empleado> mapaEmpleados;

    // Constructor
    public GestorEmpleados() {
        this.mapaEmpleados = new HashMap<>();
    }

    // Método para agregar empleados al mapa
    public void agregarEmpleado(String nombre, double salario) {
        Empleado empleado = new Empleado(nombre, salario);
        mapaEmpleados.put(nombre, empleado);
    }

    // Método para mostrar la información de un empleado
    public void mostrarInformacionEmpleado(String nombre) {
        Empleado empleado = mapaEmpleados.get(nombre);
        if (empleado != null) {
            System.out.println(empleado);
        } else {
            System.out.println("El empleado " + nombre + " no existe en el mapa.");
        }
    }

    // Método para verificar si un empleado específico existe en el mapa
    public boolean empleadoExiste(String nombre) {
        return mapaEmpleados.containsKey(nombre);
    }

    public static void main(String[] args) {
        // Crear una instancia de GestorEmpleados
        GestorEmpleados gestor = new GestorEmpleados();

        // Agregar empleados al mapa
        gestor.agregarEmpleado("Jaime García", 77777);
        gestor.agregarEmpleado("Pablo galve", 605750);

        // Mostrar la información de un empleado
        gestor.mostrarInformacionEmpleado("Jaime García");
        gestor.mostrarInformacionEmpleado("Pablo Galve");

        // Verificar la existencia de un empleado en el mapa
        System.out.println("¿Jaime GArcía existe en el mapa? " + gestor.empleadoExiste("Jaime García"));
        System.out.println("¿Carlos Martin existe en el mapa? " + gestor.empleadoExiste("Carlos Matinez"));
    }
}
