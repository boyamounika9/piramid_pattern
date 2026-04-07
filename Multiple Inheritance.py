class Teacher:
    def marks(self):
        print("full marks")
class Researcher:
    def papers(self):
        print("refer papers")
class Professor(Teacher,Researcher):
    pass
p=Professor()
p.marks()
p.papers()