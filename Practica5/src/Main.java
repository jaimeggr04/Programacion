
public class Main {
    public static void main(String[] args){
    Usuario  newUser1 = new Usuario("Jaime", "García", 41920, "Avenida Clara Campoamor 45", "jaimegarciagr@gmail.com", "jaime1234");
    Usuario newUser2 = new Usuario("Pablo", "Ramirez", 41013, "Aevnida de la borbolla", "pabloramirez@gmail.com", "pablo1234");
    System.out.println(newUser1.getName()+", "+newUser1.getSubName()+", "+newUser1.getPCode()+", "+newUser1.getAddress()+", "+newUser1.getEmail()+", "+newUser1.getPassword());
    System.out.println(newUser2.getName()+", "+newUser1.getSubName()+", "+newUser1.getPCode()+", "+newUser1.getAddress()+", "+newUser1.getEmail()+", "+newUser1.getPassword());
    newUser1.check();
    newUser2.check();
    }




}

