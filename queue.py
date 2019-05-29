class Queue(object):
    def __init__(self):
        self.vals = []
    def insert(self,e):
        if not e in self.vals:
            self.vals.append(e)
    def __len__(self):
        return len(self.vals)
    def remove(self):
        try:
            return self.vals.pop(0)
        except:
            raise ValueError('List is empty')
    def __str__(self):
        return ','.join([str(i) for i in self.vals])
s = Queue()
s.insert(1)


