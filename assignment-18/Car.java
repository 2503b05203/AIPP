public class Car {
    private final String brand;
    private final String model;
    private final int year;

    public Car (String brand, String model, int year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
    }

    public void displayDetails() {
        System.out.println("Car: " + brand + " " + model + " (" + year + ")");
    }

    public static void main(String[] args) {
        Car car = new Car("Toyota", "Corolla", 2022);
        car.displayDetails();
    }
}
