class titlemaker():
    def __init__(self,title): #creates title object
        self.title = title
    def titleconversion(self): #title logic)
        title = self.title #sets object to a variable
        title = str(title)
        split = title.split('_') #splits the input up at every '_'
        season = [] #season number to append
        for n in split[0]:
            season.append(n)
        season.remove("S")       
        seasonfin = ''.join(season) #season number
        episode = [] #episode number to append
        for n in split[1]:
            episode.append(n)
        episode.remove("E")
        episodefin = ''.join(episode) #episode number
        print("Season",seasonfin+",","Episode",episodefin+":",split[2],"(The Simpsons)") #final title


constant = (input("Input raw title\n"))
fin = titlemaker(constant)
fin.titleconversion()