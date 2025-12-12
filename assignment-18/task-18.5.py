class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Car: {self.brand} {self.model} ({self.year})")


if __name__ == "__main__":
    car = Car("Toyota", "Corolla", 2022)
    car.display_details()