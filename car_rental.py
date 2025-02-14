class Car:
    def __init__(self, model, rental_price, available=True):
        self.model = model
        self.rental_price = rental_price
        self.available = available

    def rent_car(self):
        if self.available:
            self.available = False
            print(f"{self.model} has been rented.")
        else:
            print(f"{self.model} is not available.")

    def return_car(self):
        self.available = True
        print(f"{self.model} has been returned.")

# Example Usage
if __name__ == "__main__":
    car1 = Car("Toyota Corolla", 40)
    car2 = Car("Honda Civic", 45)

    car1.rent_car()
    car1.return_car()
