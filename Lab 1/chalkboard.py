class chalkboard(): #creates necessary objects while maintaining organization
    def __init__(self,chalkboard,iterations):
        self.chalkboard = chalkboard
        self.iterations = iterations
    def writingfunc(self): #logic
        Text = self.chalkboard #sets objects to variables
        repetitions = self.iterations
        print((Text+" ")* repetitions) #multiplies string variable to emulate loop based repetition


phrase = input("What phrase would you like to iterate?\n")
repetitions = int(input("how many times would you like to print your phrase?\n"))
fin = chalkboard(phrase,repetitions) #places user input into function
fin.writingfunc()
