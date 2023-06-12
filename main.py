# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def start_engine(self):
#         return "The engine is running!"
#
#
# class Car(Vehicle):
#     def start_engine(self):
#         return super().start_engine() + " It's a car engine"
#
# my_car = Car("Toyota", "corolla", 2020)

class Engine:
    def start(self):
        return "Engine started"

    def stop(self):
        return "Engine stopped"

class Wheels:
    def rotate(self):
        return "Wheels are rotating"

class Car(Engine, Wheels):
    pass

my_car = Car()

print(my_car.start())
print(my_car.rotate())


