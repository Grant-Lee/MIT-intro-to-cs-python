class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
    def __len__(self):
        '''Return len of self'''
        return len(self.vals)
    def insertL(self, L):
        for i in L:
            self.vals.append(i)
    def intersect(self,other):
        '''create a new list of intersect values from other assuming its an intSet()'''
        result = intSet()
        
        for i in self.vals:
            if other.member(i):
                result.insert(i)
        return result

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
s1 = intSet()
#s1.insertL([-16,-6,-4,0,3,6,8,9])
s2 = intSet()
#s2.insertL([-16,-13,-4,-1,2,8,9,12,17])
print s1.intersect(s2)

