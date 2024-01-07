public class Person implements Human {

    // Escribimos los parametros de persona

    protected String name;
    protected String DNI;
    protected String sex;
    protected Integer age;

    public Person(String name, String DNI, String sex, Integer age) {
        this.name = name;
        this.DNI = DNI;
        this.sex = sex;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDNI() {
        return DNI;
    }

    public void setDNI(String DNI) {
        this.DNI = DNI;
    }

    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return "Persona{" +
                "name='" + name + '\'' +
                ", DNI='" + DNI + '\'' +
                ", sex='" + sex + '\'' +
                ", age=" + age +
                '}';
    }



}


