names = [
    "Frodo",
    "Samwise",
    "Gandalf",
    "Legolas",
    "Gimli",
    "Aragorn",
    "Boromir",
    "Merry",
    "Pippin",
]
ages = [51, 39, 2000, 2931, 140, 88, 41, 37, 29]

class LOTR_4():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def logic(self):
        younger = []
        older = []
        for n in range(len(ages)):
            if ages[n] < int(self.age):
                older.append(names[n])
            elif ages[n] > int(self.age):
                younger.append(names[n])
        if len(older) > 0:
            print(self.name,"is",self.age,"years old and they are older than",", ".join(older))
        if len(younger) > 0:
            print(self.name,"is",self.age,"years old and they are younger than",", ".join(younger))

name = input("What is the name of your character?\n")
age = input("What is the age of your character?\n")
if int(age) < 0:
    print("invalid input")
    exit()
    
logic = LOTR_4(name,age)
logic.logic()