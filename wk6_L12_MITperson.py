import datetime
class Person(object):
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
    def getLastName(self):
        '''return self's last name'''
        return self.lastName
        
    def __str__(self):
        '''return name from self'''
        return self.name
    
    def getAge(self):
        '''gets age of a person'''
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days/365.0
        
    def __lt__(self,other):
        '''return True if self's name is lexicographically
        less than other's name and False otherwise'''
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
        
        
    def setBirthday(self, month, day, year):
        self.birthday = datetime.date(year, month, day)

class MITPerson(Person):
    #next ID Number to assign
    nextIdNum = 0
    def __init__(self, name):
        #initialize (Person) attribute
        Person.__init__(self, name)
        #new MITPerson attribute: a unique ID number
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
        
    def getIdNum(self):
        return self.idNum
        
    def __lt__(self, other):
        '''sorting MITPerson by ID'''    
        return self.idNum < other.idNum
s = MITPerson('Grant Liu')
s2 = MITPerson('David Chen')
print s.getIdNum(), s2.getIdNum()
