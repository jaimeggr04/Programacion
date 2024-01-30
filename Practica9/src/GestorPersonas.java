import java.util.HashMap;
import java.util.Map;

public class GestorPersonas {

    //Aqui creamos el mapa, esto es el atributo
    private Map<String, Integer> mapaPersonas;
    //Constructor
    public GestorPersonas(){
        this.mapaPersonas = new HashMap<>();
    }

    //Este es el metodo para agregar persona
    public void agregarPersona(String Nombre, Integer Edad){
        mapaPersonas.put(Nombre, Edad);
        System.out.println("Persona "+ Nombre + "a ingresado con exito");
    }

    //Metodo para mostrar

    public void mostrarInfoPersona(String Nombre){
        if(mapaPersonas.containsKey(Nombre)) {
            int Edad = mapaPersonas.get(Nombre);
            System.out.println("Nombre:"+Nombre+"Edad: "+Edad);
        }else{
          System.out.println("La persona que ha introducido no existe en el mapa");
        }
    }
    //Metodo para verificar si una persiona existe en el mapa
    public boolean verificarPersona(String nombre) {
        return mapaPersonas.containsKey(nombre);
    }
    public static void main(String[] args) {

        GestorPersonas gestor = new GestorPersonas();

        // Agregar personas al mapa
        gestor.agregarPersona("Jaime ",  25);
        gestor.agregarPersona("Pablo ",  30);

        // Mostrar información de personas
        gestor.mostrarInfoPersona("Jaime ");
        gestor.mostrarInfoPersona("Pablo ");

        // Verificar la existencia de personas en el mapa
        System.out.println("¿Jaime existe en el mapa? " + gestor.verificarPersona("Jaime "));
        System.out.println("¿Pablo existe en el mapa? " + gestor.verificarPersona("Pablo "));
    }
}



