class Bird:
    def fly(self):
        print("Bird can fly")

class Airplane:
    def fly(self):
        print("Airplane can fly")

def flying_test(entity):
    entity.fly()

bird = Bird()
airplane = Airplane()

flying_test(bird)    
flying_test(airplane)