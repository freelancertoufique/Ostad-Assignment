
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

    def display_student_info(self):
        self.display_person_info()
        print(f"Student ID: {self.student_id}")
        print("Courses: ", ", ".join(self.courses)if self.courses else "None")
        print(f'Grades: {self.grades}' if self.grades else "None")

#===========Creating a Class with the naem Course========================
class Course:
    def __init__(self,course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []
    def add_student(self, student_id):
        if student_id not in self.students:
            self.students.append(student_id)
    def display_course_info(self):
        print(f'Course Name: {self.course_name}')
        print(f'Course Code: {self.course_code}')
        print(f'Instructor: {self.instructor}')
        print(f'Students Enrolled: {', '.join(self.students) if self.students else "None"}')
