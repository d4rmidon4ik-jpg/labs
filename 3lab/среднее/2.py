class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = [] 
    
    def add_grade(self, grade):
        self.grades.append(grade)
            
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def show_info(self):
        return f"{self.name}, {self.age} лет, средний балл: {self.get_average():.2f}"

student = Student("Саша", 19)
student.add_grade(5)
student.add_grade(4)
student.add_grade(3)
print(student.show_info()) 
