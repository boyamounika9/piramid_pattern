class Shape:
    def circlearea(self):
        print("area of circle")
    def rectangle(self):
        print("area of rectangle")
class Circle(Shape):
    def area1(self):
        pass
class Rectangle(Shape):
    def area2(self):
        pass
a1=Circle()
a2=Rectangle()
a1.circlearea()
a2.rectangle()

