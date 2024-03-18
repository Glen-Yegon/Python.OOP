class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    
    def introPerson(self):
        print(f"My name is {self.name}, I am a {self.gender} citizen of {self.age} years of age.")

P1 = Person("John", "Male", 20)
P1.introPerson()