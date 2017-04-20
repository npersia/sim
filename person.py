import copy,random


class Person:
    idPerson = 1

    def __init__(self,sexo,family={}):
        self.idP = Person.idPerson
        self.age = -1
        self.sex = sexo
        self.married = False
        self.alive = True
        self.children = 0
        self.family = family
        Person.idPerson += 1

    
    def addYear(self):
        self.age += 1

    def marry(self,couple):
        self.married = True
        self.couple = couple
        
    def haveSon(self):
        self.children += 1
        sonFamily = copy.copy(self.family)
        sonFamily[len(sonFamily)+1]#seguir aca
        return Person(random.choice('mf'))
	

    def die(self):
        self.alive = False
    
    
    def __str__(self):
        return "id: "+str(self.idP)+"\tsex: "+str(self.sex)+"\tmarried: "+str(self.married)+"\tchildren: "+str(self.children)+"\tage: "+str(self.age)+"\talive: "+str(self.alive)




a=Person("f")
print(a)
a.idPerson=2
b=Person("m")
print(b)

print(b.haveSon())
