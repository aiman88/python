class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    pass

c1=Cat()
c1.walk()

d1=Dog()
d1.bark()

