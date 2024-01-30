import java.util.ArrayList;

public class GestorNumeros {
    private ArrayList<Integer> NumerosEnteros;

    public GestorNumeros(ArrayList numerosEnteros) {
        this.NumerosEnteros = numerosEnteros;

    }


    public ArrayList<Integer> getNumerosEnteros() {
        return NumerosEnteros;
    }

    public void setNumerosEnteros(ArrayList<Integer> numerosEnteros) {
        NumerosEnteros = numerosEnteros;
    }

    //Creamos el metodo Agreagador
    public void Agregador(Integer n){

        this.NumerosEnteros.add(n);
    }

    //Creamos el metodo Mostrar

    public void Mostrar(){
        System.out.println(this.NumerosEnteros);
    }

    //Creamos el metodo suma
    public Integer Suma(){
        int res = 0;
        for (int i = 0; i < this.NumerosEnteros.size(); i++){
            res = res + this.NumerosEnteros.get(i);
        }
    return res;
    }

}
