class Animals:
    pass

class pets(Animals):
    pass

class Dog(pets):
    @staticmethod
    def bark():
        print("The dog is barking")

d=Dog()
d.bark()