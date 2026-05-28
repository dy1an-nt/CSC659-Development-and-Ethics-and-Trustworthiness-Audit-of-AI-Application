public class Car {
    private String model;
    private int year;
    public Car(String model, int year) {
        this.model = model;
        this.year = year;
    }
    public void displayInfo() {
        System.out.println("Car Model: " + model + " | Year: " + year);
    }
    public static void main(String[] args) {
        Car car1 = new Car("Toyota Camry", 2022);
        Car car2 = new Car("Ford Mustang", 1969);
        car1.displayInfo();
        car2.displayInfo();
    }
}
