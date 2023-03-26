public class HospitalEmployee {
    protected String name;
    protected int number;

    public HospitalEmployee(String name, int number) {
        this.name = name;
        this.number = number;
    }

    public String getName() { 
        return name; 
    }
    public int getNumber() { 
        return number; 
    }
    public void setName(String name) { 
        this.name = name;
    }
    public void setNumber(int number) { 
        this.number = number;
    }
    public String toString() {
        return name + " " + number;
    }
    public void work() {
        System.out.println(name + " works for the hospital.");
    }
}

class Nurse extends HospitalEmployee {   
    int numOfPatients;

    public Nurse(String name, int number, int numOfPatients) {
        super(name, number);
        this.numOfPatients = numOfPatients;
    }
    public String toString() {
        return name + " " + number + " has " + numOfPatients + " patients.";
    }
    public void work() {
        System.out.println(name + " works for the hospital. " + name + " is a nurse with " + numOfPatients + " patients.");
    }
}

class Doctor extends HospitalEmployee {   
    String specialty;

    public Doctor(String name, int number, String specialty) {
        super(name, number);
        this.specialty = specialty;
    }
    public String toString() {
        return name + " " + number + " " + specialty;
    }
    public void work() {
        System.out.println(name + " works for the hospital. " + name + " is a(n) " + specialty + " doctor.");
    }
}

class Surgeon extends Doctor {
    boolean operating;

    public Surgeon(String name, int number, String specialty, boolean operating) {
        super(name, number, specialty);
        this.operating = operating;
    }

    public String toString() {
        return name + " " + number + " " + specialty + " Operating: " + operating;
    }
    public void work() {
        String isOperating;
        if (operating) isOperating = " is operating now.";
        else isOperating = " is not operating now.";
        System.out.println(name + " works for the hospital. " + name + isOperating);
    }
}
