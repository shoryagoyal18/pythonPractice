class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self, name, breed):
        # Call the constructor of the superclass (Animal)
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def __init__(self, name, color):
        # Call the constructor of the superclass (Animal)
        super().__init__(name)
        self.color = color

    def make_sound(self):
        return "Meow!"


dog_obj = Dog("Buddy", "Golden Retriever")
cat_obj = Cat("Whiskers", "Calico")

print(dog_obj.name+" is a "+dog_obj.breed+" that says "+dog_obj.make_sound())
print(cat_obj.name+" is a "+cat_obj.color+" cat that says "+cat_obj.make_sound())
