class homer:
    def __init__(self,sight): #creates object
        self.sight = sight
    def homer_func(self): #logic function
        if self.sight == "marshmallow": #if else statements
            print ("Mmm... marshmallow!")
        elif self.sight == "chocolate":
            print("Mmm... chocolate!")
        elif self.sight == "maca-ma-damia nuts":
            print("Mmm... maca-ma-damia nuts!")
inpt = str(input("What is the tasty thing?\n"))
fin = homer(inpt)
fin.homer_func()
