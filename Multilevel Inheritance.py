class Grandfather:
    def land(self):
        print("grapha land")
class father(Grandfather):
    def home(self):
        print("dads home")
class child(father):
    def car(self):
        print("car")
c=child()
c.car()
c.land()
c.home()