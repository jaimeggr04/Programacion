import java.awt.*;
import java.time.LocalDate;
import java.util.ArrayList;

public class Contrato {

    protected LocalDate creationDate;
    protected Doctor doctorData;
    protected Hospital hospital;

    public Contrato(LocalDate creationDate, Doctor doctorData, Hospital hospital) {
        this.creationDate = creationDate;
        this.doctorData = doctorData;
        this.hospital = hospital;
    }

    public LocalDate getCreationDate() {
        return creationDate;
    }

    public void setCreationDate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }

    public Doctor getDoctorData() {
        return doctorData;
    }

    public void setDoctorData(Doctor doctorData) {
        this.doctorData = doctorData;
    }

    public Hospital getHospital() {
        return hospital;
    }

    public void setHospital(Hospital hospital) {
        this.hospital = hospital;
    }

    @Override
    public String toString() {
        return "Contrato{" +
                "creationDate=" + creationDate +
                ", doctorData=" + doctorData +
                ", hospital=" + hospital +
                '}';
    }

    public static ArrayList<Contrato> contrato23(ArrayList <Contrato> a) {

        ArrayList<Contrato> c = new ArrayList<>();
        for (Contrato d : a) {
            if (d.getCreationDate().getYear() == 2023) {
                c.add(d);
            }
        }
        return c;
    }
}
