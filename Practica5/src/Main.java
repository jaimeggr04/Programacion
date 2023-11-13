
public class Main {
    public static void main(String[] args){
    //Creamos dos nuevos objetos "newUser1 y newUser2" con el constructor.
    Usuario  newUser1 = new Usuario("Jaime", "García", 41920, "Avenida Clara Campoamor 45", "jaimegarciagr@gmail.com", "jaime1234");
    Usuario newUser2 = new Usuario("Pablo", "Ramirez", 41013, "Aevnida de la borbolla", "pabloramirez@gmail.com", "pablo1234");
    //Imprimimos todos los valores de los usuarios
    System.out.println(newUser1.getName()+", "+newUser1.getSubName()+", "+newUser1.getPCode()+", "+newUser1.getAddress()+", "+newUser1.getEmail()+", "+newUser1.getPassword());
    System.out.println(newUser2.getName()+", "+newUser2.getSubName()+", "+newUser2.getPCode()+", "+newUser2.getAddress()+", "+newUser2.getEmail()+", "+newUser2.getPassword());
    newUser1.check();
    newUser2.check();
    }
}

