import javax.print.Doc;
import java.time.LocalDate;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

    Location location1 = new Location("Calle FuenteVieja", 13,41920, "Sevilla", "Sevilla") ;
    Location location2 = new Location("Calle Huracan", 66,41921, "Sevilla", "Sevilla")  ;
    Hospital SantaLucia = new Hospital("34552D", "Sevilla","SantaLucia");
    Area area1 = new Area("Psicologia", 2,112, SantaLucia);
    Doctor Jaime = new Doctor("Jaime García","30290434D", "Masculino", 19, area1, LocalDate.of(2023, 10, 15), 2006.5, location1);
    System.out.println(Jaime.toString());
    System.out.println(Jaime.years());
    System.out.println(Jaime.NetSalary(0.2));

    ArrayList<Area>Areas = new ArrayList<Area>();
    ArrayList<Contrato>Contratos = new ArrayList<Contrato>();
    ArrayList<Doctor>Doctores = new ArrayList<Doctor>();
    ArrayList<Location>Locations = new ArrayList<Location>();
    ArrayList<Hospital>Hospitals = new ArrayList<Hospital>();


    }
}