class Student:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

student1 = Student("Alice")

print("Name:", student1.get_name())

student1.set_name("Bob")

print("Changed Name:", student1.get_name())