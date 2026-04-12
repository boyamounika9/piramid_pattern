from abc import ABC,abstractmethod
class Vehicle(ABC) :
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("car starts ")
    def stop(self):
        print("car stops")
class Bike(Vehicle):
    def start(self):
        print("bike strats")
    def stop(self):
        print("bike stops")

c=Car()
b=Bike()

c.start()
c.stop()
b.start()
b.stop()