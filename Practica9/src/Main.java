import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        ArrayList<Integer> list = new ArrayList<>();
        GestorNumeros lista =  new GestorNumeros(list);
        lista.Agregador(4);
        lista.Agregador(8);
        lista.Agregador(10);

        System.out.println(lista.Suma());

        lista.Mostrar();
    }
}