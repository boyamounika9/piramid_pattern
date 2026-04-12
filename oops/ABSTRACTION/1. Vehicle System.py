from abc import ABC,abstractmethod
class Vehicle :
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