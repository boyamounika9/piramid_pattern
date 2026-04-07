class gp:
    def land(self):
        print("gps land")
class father(gp):
    def home(self):
        print("dadas home")
class mom:
    def love(self):
        print("moms love ")
class child(father,mom):
    pass
c=child()
c.land()
c.home()