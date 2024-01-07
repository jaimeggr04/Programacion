import java.util.Scanner;

public class Hospital {

    protected String CIF;
    protected String Location;
    protected String Name;


    public Hospital(String CIF, String location, String name) {
        this.CIF = CIF;
        Location = location;
        Name = name;

    }

    public String getCIF() {
        return CIF;
    }

    public void setCIF(String CIF) {
        this.CIF = CIF;
    }

    public String getLocation() {
        return Location;
    }

    public void setLocation(String location) {
        Location = location;
    }

    public String getName() {
        return Name;
    }

    public void setName(String name) {
        Name = name;
    }

    @Override
    public String toString() {
        return "Hospital{" +
                "CIF='" + CIF + '\'' +
                ", Location='" + Location + '\'' +
                ", Name='" + Name + '\'' +
                '}';
    }

    public static Hospital createHospital(){
        Scanner s = new Scanner(System.in);
        String hospitalCIF = s.nextLine();
        String hospitalLocation = s.nextLine();
        String hospitalName = s.nextLine();

        return new Hospital(hospitalCIF, hospitalLocation, hospitalName );

    }
}
