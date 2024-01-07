import java.time.LocalDate;
import java.util.Scanner;

public class Doctor extends Person {

    //Escribimos los parametros de medico

    protected Area area;
    protected LocalDate startingDate;
    protected Double salary;
    protected Location location;

    //Constructor


    public Doctor(String name, String DNI, String sex, Integer age, Area area, LocalDate startingDate, Double salary, Location location) {
        super(name, DNI, sex, age);
        this.area = area;
        this.startingDate = startingDate;
        this.salary = salary;
        this.location = location;
    }

    //Escribimos los metodos Getter y setter

    public Area getArea() {
        return area;
    }

    public void setArea(Area area) {
        this.area = area;
    }

    public LocalDate getStartingDate() {
        return startingDate;
    }

    public void setStartingDate(LocalDate startingDate) {
        this.startingDate = startingDate;
    }

    public Double getSalary() {
        return salary;
    }

    public void setSalary(Double salary) {
        this.salary = salary;
    }

    public Location getLocation() {
        return location;
    }

    public void setLocation(Location location) {
        this.location = location;
    }

    @Override
    public String toString() {
        return "Doctor{" +
                "area=" + area +
                ", startingDate=" + startingDate +
                ", salary=" + salary +
                ", location=" + location +
                ", name='" + name + '\'' +
                ", DNI='" + DNI + '\'' +
                ", sex='" + sex + '\'' +
                ", age=" + age +
                '}';
    }

    public Doctor creaDoctor(){
        System.out.println("Insert Doctor: DNI, name, age, sex");
        Scanner s = new Scanner(System.in);
        String dniDoctor = s.nextLine();
        String nDoctor = s.nextLine();
        Integer aDoctor = s.nextInt();
        String sDoctor = s.nextLine();
        Double saDoctor = s.nextDouble();
        LocalDate dDoctor =LocalDate.of(s.nextInt(),s.nextInt(),s.nextInt());
        Area area = Area.createArea();
        Location location = Location.createLocation();
        return new Doctor(nDoctor, dniDoctor, sDoctor, aDoctor, area, dDoctor, saDoctor, location);

    }

    public Double NetSalary(Double percentage){
        Double retain = this.salary*percentage;
        return this.salary-retain;
    }

    public Integer years(){
       return this.startingDate.getYear()-LocalDate.now().getYear();

    }

}





