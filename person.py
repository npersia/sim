class Person:

    def __init__(self,name,sexo,family={}):
        self.name = name
        self.age = -1
        self.sex = sexo
        self.married = False
        self.alive = True
        self.children = 0
        self.family = family

    
    def addYear(self):
        self.age += 1

    def marry(self,couple):
        self.married = True
        self.couple = couple
        
    def haveSon(self):
        self.children += 1






    def die(self):
        self.alive = False




    def __str__(self):
        return "name: "+str(self.name)+"\tsex: "+str(self.sex)+"\tmarried: "+str(self.married)+"\tage: "+str(self.age)+"\talive: "+str(self.alive)

a=Person(1,"f")
a.addYear()
print(a)
