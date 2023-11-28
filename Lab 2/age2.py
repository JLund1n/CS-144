frodo_age = 51
gollum_age = 589


class LOTR_char():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def logic(self):
        if int(self.age) < frodo_age:
            if int(self.age) < gollum_age:
                print(self.name,"is",self.age,"years old, and they are younger than Frodo and Gollum")
        elif int(self.age) == frodo_age:
            print(self.name,"is",self.age,"years old, and they are the same age as Frodo but younger than Gollum")
        elif int(self.age) > frodo_age:
            if int(self.age) < gollum_age:
                print(self.name,"is",self.age,"years old, and they are older than Frodo but younger than Gollum")
            if int(self.age) == gollum_age:
                print(self.name,"is",self.age,"years old, and they are older than Frodo and the same age as Gollum")
            if int(self.age) > gollum_age:
                print(self.name,"is",self.age,"years old, and they are older than Frodo and Gollum")

name = input("What is the name of your character?\n")
age = input("what is the age of your character?\n")

logic = LOTR_char(name,age)
logic.logic()