class Animal:
    count = 0

    def __init__(self, name):
        self.name = name
        self.count += 1 
    
    def move(self):
        print("총총총")

    def speak(self):
        pass

    @classmethod
    def showCount(Animal):
        print(Animal.count)

class Dog (Animal):
    def speak(self):
        print("멍멍")

class Cat (Animal) :
    def speak(self):
        print("냐옹")

dog = Dog("T-Poo")
d_name = dog.name
dog.move()
dog.speak()


animals = [Dog('멍멍'),Cat('냥냥')]

for a in animals:
    a.speak()

Animal.showCount()
