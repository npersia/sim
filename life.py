import person

class Life:

    def __init__(self,persons,marry_age,die_age):
        self.persons = persons
        self.marry_age = marry_age
        self.die_age = die_age

    def addYear(self):
        for p in self.persons:
            p.addYear()


