class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello ,my name is {self.name}. I am {self.age} years old"
              f"and i am {self.gender}")


person1 = Person("Mary",25,"Female")
person2 = Person("Sebastian", 36,"Male")


person1.introduce()
person2.introduce()
