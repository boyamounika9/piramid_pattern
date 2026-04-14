class person:
    def __init__(self):
        self.name=input("enter the name :")
        self.age=int(input("enter the age :"))
class student(person):
    def __init__(self):
        super().__init__()
        self.marks=int(input("enter the marks:"))
        self.id=int(input("enter the id :"))
    def display_studentdetails(self):
        print(self.name,self.age,self.id,self.marks)
        
class teacher(person):
    def __init__(self):
        super().__init__()
        self.subject=input("enter the sub name:")
    def display_teacherdetails(self):
        print(self.name,self.age,self.subject)

s=student()
t=teacher()

s.display_studentdetails()
t.display_teacherdetails()