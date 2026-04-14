class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, student_id, marks):
        super().__init__(name, age)   # Inheritance
        self.__marks = marks          # Encapsulation (private)
        self.student_id = student_id

    # Getter
    def get_marks(self):
        return self.__marks

    # Setter
    def set_marks(self, new_marks):
        self.__marks = new_marks

    def display(self):
        print("Student Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("ID:", self.student_id)
        print("Marks:", self.__marks)
        print("-------------------------")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)   # Inheritance
        self.subject = subject

    def display(self):
        print("Teacher Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Subject:", self.subject)
        print("-------------------------")


# Lists to store data
students = []
teachers = []


# Menu-driven system
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student Marks")
    print("4. Add Teacher")
    print("5. View Teachers")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        sid = int(input("Enter student ID: "))
        marks = int(input("Enter marks: "))

        s = Student(name, age, sid, marks)
        students.append(s)

    elif choice == 2:
        for s in students:
            s.display()

    elif choice == 3:
        sid = int(input("Enter student ID to update marks: "))
        for s in students:
            if s.student_id == sid:
                new_marks = int(input("Enter new marks: "))
                s.set_marks(new_marks)
                print("Marks updated successfully!")

    elif choice == 4:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        subject = input("Enter subject: ")

        t = Teacher(name, age, subject)
        teachers.append(t)

    elif choice == 5:
        for t in teachers:
            t.display()

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")