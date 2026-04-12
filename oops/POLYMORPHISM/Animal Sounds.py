# Polymorphism - Animal Sounds

class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


class Cow:
    def sound(self):
        print("Cow moos")


# Creating objects
d = Dog()
c = Cat()
w = Cow()

# Using loop (same method, different behavior)
animals = [d, c, w]

for animal in animals:
    animal.sound()