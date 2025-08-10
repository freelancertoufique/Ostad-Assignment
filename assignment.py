
#===================Making a class with name person===================

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")

#====================creating an class with the name sutudent====================
#=====================it will inherit the person class=====================

class Student(Person):
    def __init__(self, name, age, address,student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []
    
    def add_grade(self, subject, grade):
        if subject not in self.grades:
            self.grades[subject] = grade
    
    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

ob1 = Student(name="Toufique Ahamed", age=20, address = 'Khulna', student_id='S12345')
ob1.add_grade('Math', 90)
ob1.add_course('Computer Science')
print(ob1.grades)
print(ob1.courses)