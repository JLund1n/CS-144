frodo_age = 51

class LOTR_age():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def logic(self):
        if int(self.age) < frodo_age:
            print(self.name,"is",self.age,"years old, and they are younger than frodo")
        elif int(self.age) == frodo_age:
            print(self.name,"is",self.age,"years old, and they are the same age as frodo")
        else:
            print(self.name,"is",self.age,"years old, and they are older than frodo")

name = input("What is the name of your character?\n")
age = input("what is the age of your character?\n")

func = LOTR_age(name,age)
func.logic()

