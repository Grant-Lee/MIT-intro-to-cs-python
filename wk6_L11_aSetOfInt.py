class intSet(object):
    """create an empty list for base"""
    def __init__(self):
        self.Vals = []
    
    def __str__(self):
        '''print a string for all elements in self'''
        self.Vals.sort()
        #print a string for all the elements in self.vals(list) seperate by coma
        return '{'+','.join([str(e) for e in self.Vals])+'}'
        
    def insert(self, e):
        """Assume e is an int and inset e in self"""
        #add e to the list within self(self.vals) if its not in the list(self.vals)
        if not e in self.Vals:
            self.Vals.append(e)
            
    def member(self,e):
        '''return True if e is in Self else False'''
        return e in self.Vals
    def remove(self,e):
        '''Assume e is an integer and remove e from self
        raise ValueError if e not in self'''
        try:
            self.Vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
        