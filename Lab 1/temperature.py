class temp_conversion ():
    def __init__(self,Celsius): #creates objects
        self.Celsius = Celsius
    def conversion_func(self): #logic using created objectt
        c = self.Celsius #sets object to a variable
        self.Celsius = int((self.Celsius *(9/5)) + 32) #conversion calculation plus interger rounding if float
        print(c,"degrees in Canada would be", self.Celsius, "degrees in Springfield. D'oh!") #final phrase
inp = input("Temperature in celsius to covert\n")
try: 
    inp = int(inp)
except:
    inp = float(inp) #checks to see if the input is either a float or interger

fin = temp_conversion(inp)
fin.conversion_func()