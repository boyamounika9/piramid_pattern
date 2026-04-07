#single inheritance
class Parent:
    def __init__(self,name,age):
        # self.name = input()
        # self.age = int(input())
        self.name = name
        self.age = age
    def calling(self):
        print(self.name, ' is calling')
        print(self.age)

p1 = Parent('Sudha',21)
p2 = Parent('mounika',20)

p1.calling()
p2.calling()

#===================single with user input==================
class Parent:
    def land(self):
        print('Parents land')
    
class Child(Parent):
    def car(self):
        print('I have a Car')

c1 = Child()

c1.car()
c1.land()

#=============Multiple inheritance===============
class Father:
    def land(self):
        print('Parents land')

class Mother:
    def house(self):
        print('Mothers house')
    
class Child(Father, Mother):
    def car(self):
        print('I have a Car')

c1 = Child()

c1.car()
c1.land()
c1.house()

#=========multi level ==============
class Grandfather:
    def land(self):
        print('GrandParents land')

class Father(Grandfather):
    def house(self):
        print('Fathers house')
    
class Child(Father):
    def car(self):
        print('I have a Car')

c1 = Child()
c2 = Father()


c2.house()
c2.land()
c2.car()

c1.car()
c1.land()
c1.house()

#=========== Hirartical inheritance=============
class Parent:
    def land(self):
        print('Parent land')

class Child1(Parent):
    def house(self):
        print('Child1 house')
    
class Child2(Parent):
    def car(self):
        print('I have a Car')

c1 = Child2()

c1.car()
c1.land()

#============Hybrid inheritance============
class GrandParent:
    def gold(self):
        print('GrandParents gold')

class Father(GrandParent):
    def house(self):
        print('Fathers home')

class Mother:
    def love(self):
        print('Mothers love...')

class Me(Father, Mother):
    def job(self):
        print('Karuvupani...')

m1 = Me()

m1.love()
m1.job()

class parent :
    def __init__(self,name,age):
        self.name=input()
        self.age=int(input())
    def calling(self):
        print(self.name, ' is calling')
        print(self.age)

pa=parent()
pa.calling()