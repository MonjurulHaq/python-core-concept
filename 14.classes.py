class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_id(self):
        print(f"My student ID is {self.student_id}")

if __name__ == "__main__":
    person = Person("Alice", 30)
    person.greet()

    student = Student("Bob", 20, "S12345")
    student.greet()
    student.display_id()