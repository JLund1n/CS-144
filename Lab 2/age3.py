pippin_age = 29
frodo_age = 51
gollum_age = 589
arwen_age = 2901


class LOTR_3 ():
    def __init__(self,name,age):
        self.age = age
        self.name = name
    def logic(self):
        if int(self.age) > arwen_age:
            print(self.name,"is",self.age,"years old, and they are older than Pippin, Frodo, Gollum and Arwen")
        elif int(self.age) > gollum_age:
            if int(self.age) == arwen_age:
                print(self.name,"is",self.age,"years old, and they are older than Pippin, Frodo and Gollum but the same age as Arwen")
            else:
                print(self.name,"is",self.age,"years old, and they are older than Pippin, Frodo, and Gollum")
                print(self.name,"is",self.age,"years old, and they are younger than Arwen")
        elif int(self.age) > frodo_age:
            if int(self.age) == gollum_age:
                print(self.name,"is",self.age,"years old, and they are older than Pippin, Frodo, but the same age as Gollum")
                print(self.name,"is",self.age,"years old, and they are younger than Arwen")
            else:
                print(self.name,"is",self.age,"years old, and they are older than Pippin and Frodo")
                print(self.name,"is",self.age,"years old, and they are younger than Gollum and Arwen")
        elif int(self.age) > pippin_age:
            if int(self.age) == frodo_age:
                print(self.name,"is",self.age,"years old, and they are older than Pippin but the same age as Frodo")
                print(self.name,"is",self.age,"years old, and they are younger than Gollum and Arwen")
            else:
                print(self.name,"is",self.age,"years old, and they are older than Pippin")
                print(self.name,"is",self.age,"years old, and they are younger than Frodo, Gollum and Arwen")
        elif int(self.age) <= pippin_age:
            if int(self.age) == pippin_age:
                print(self.name,"is",self.age,"years old, and they are the same age as Pippin")
                print(self.name,"is",self.age,"years old, and they are younger than Frodo, Gollum and Arwen")
            else:
                print(self.name,"is",self.age,"years old, and they are ypunger than Pippin, Frodo, Gollum and Arwen")


name = input("What is the name of your character?\n")
age = input("What is the age of your character?\n")
if int(age) < 0:
    print("invalid input")
    exit()
    
logic = LOTR_3(name,age)
logic.logic()