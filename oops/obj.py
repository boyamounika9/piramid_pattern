class circle :
    def rad(self,radius):
        self.radius=radius
    def area(self):
        self.circlearea=3.14*(self.radius*self.self.radius)
        print(self.circlearea)
    def circum(self):
        self.circlecircum=2*3.14*self.radius
        print(self.circlecircum)

c=circle(12)
c.area()
c.circum()
