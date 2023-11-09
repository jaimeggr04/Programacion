import java.util.Scanner;
public class Usuario {
    // Parametros
    private String name;
    private String subName;
    private int pCode;
    private String address;
    private String email;
    private String password;

    //Constructor
    public Usuario(String n, String s, int pc, String a, String e, String p){
        this.name = n;
        this.subName = s;
        this.pCode = pc;
        this.address = a;
        this.email = e;
        this.password = p;
    }

    public String getName(){
        return this.name;
    }

    public void setName(String n){
        this.name = n;

    }
    public String getSubName(){
        return this.subName;
    }

    public void setSubName(String s){
        this.subName = s;

    }

    public int getPCode(){
        return this.pCode;
    }

    public void setPCode(int pc){
        this.pCode = pc;

    }

    public String getAddress(){
        return this.address;
    }

    public void setAddress(String a){
        this.address = a;

    }

    public String getEmail(){
        return this.email;
    }

    public void setEmail(String e){
        this.email = e;

    }

    public String getPassword(){
        return this.password;
    }

    public void setPassword(String p){
        this.password = p;

    }

    public void check() {
        String res = "";
        Scanner s = new Scanner(System.in);
        System.out.println("Introduce el usuario: ");
        String userName = s.next();
        System.out.println("Introduce la contraseña: ");
        String Password = s.next();
        if (this.name.equals(userName) && this.password.equals(Password)) {
            res = "Has iniciado sesion";
        }else{
            System.out.println("Error, el usuario o la contraseña no coinciden");
        }
        System.out.println(res);

    }
}
