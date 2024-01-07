import java.util.Scanner;

public class Location {
    protected String street;
    protected Integer number;
    protected Integer postalCode;
    protected String province;
    protected String Place;


    public Location(String street, Integer number, Integer postalCode, String province, String place) {
        this.street = street;
        this.number = number;
        this.postalCode = postalCode;
        this.province = province;
        Place = place;
    }

    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }

    public Integer getNumber() {
        return number;
    }

    public void setNumber(Integer number) {
        this.number = number;
    }

    public Integer getPostalCode() {
        return postalCode;
    }

    public void setPostalCode(Integer postalCode) {
        this.postalCode = postalCode;
    }

    public String getProvince() {
        return province;
    }

    public void setProvince(String province) {
        this.province = province;
    }

    public String getPlace() {
        return Place;
    }

    public void setPlace(String place) {
        Place = place;
    }


    @Override
    public String toString() {
        return "Location{" +
                "street='" + street + '\'' +
                ", number=" + number +
                ", postalCode=" + postalCode +
                ", province='" + province + '\'' +
                ", Place='" + Place + '\'' +
                '}';
    }

    public static Location createLocation(){
        Scanner s = new Scanner(System.in);
        String locationStreet = s.nextLine();
        Integer locationNumber = s.nextInt();
        Integer locationPostalCode = s.nextInt();
        String locationProvince = s.nextLine();
        String locationPlace = s.nextLine();

        return new Location(locationStreet, locationNumber, locationPostalCode, locationProvince, locationPlace);

    }

}
