class BMW:
    def fuel_type(self):
        print("BMW fuel type: Petrol and Diesel")

    def max_speed(self):
        print("BMW max speed: 250 km/h")

class Ferrari:
    def fuel_type(self):
        print("Ferrari fuel type: Petrol")

    def max_speed(self):
        print("Ferrari max speed: 340 km/h")


def car_details(car):
    car.fuel_type()
    car.max_speed()


bmw = BMW()
ferrari = Ferrari()

car_details(bmw)
car_details(ferrari)