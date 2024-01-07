import java.util.Scanner;

public class Area {

    //Escribimos los parametros
    protected String name;
    protected Integer floor;
    protected Integer id;
    protected Hospital hospital;
    protected Integer numArea;

    public Area(String name, Integer floor, Integer id, Hospital hospital) {
        this.name = name;
        this.floor = floor;
        this.id = id;
        this.hospital = hospital;
        numArea = 0;

    }


    public Integer getNumArea() {
        return numArea;
    }

    public void setNumArea(Integer numArea) {
        this.numArea = numArea;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getFloor() {
        return floor;
    }

    public void setFloor(Integer floor) {
        this.floor = floor;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Hospital getHospital() {
        return hospital;
    }

    public void setHospital(Hospital hospital) {
        this.hospital = hospital;
    }

    @Override
    public String toString() {
        return "Area{" +
                "name='" + name + '\'' +
                ", floor='" + floor + '\'' +
                ", id=" + id +
                ", hospital='" + hospital + '\'' +
                '}';

    }

    public static Area createArea(){
        Scanner s = new Scanner(System.in);
        String areaName = s.nextLine();
        Integer areaFloor = s.nextInt();
        Integer areaID = s.nextInt();
        Hospital areaHospital = Hospital.createHospital();
        return new Area(areaName, areaFloor, areaID, areaHospital);

    }

    public void moreDoctors(Area a){
        if(this.getNumArea() > a.getNumArea()){
            System.out.println("El primer area tienes mas doctores que la segunda");
        } else if (this.getNumArea() < a.getNumArea()) {
            System.out.println("El segundo tiene mas doctores que el primero");
        }else{
            System.out.println("Ambas areas tiene la misma cantidad de medicos");
        }

    }
}
