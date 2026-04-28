class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("Woof")

a = Animal()
a.speak()

d = Dog()
d.speak()