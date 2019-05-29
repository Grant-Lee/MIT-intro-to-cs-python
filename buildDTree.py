class binaryTree(object):
    def __init__(self, value):
        self.value = value
        self.leftBranch = None
        self.rightBranch = None
        self.parent = None
        
    def setLeftBranch(self, node):
        self.leftBranch = node   
    def setRightBranch(self, node):
        self.rightBranch = node
        
    def setParent(self, parent):
        self.parent = parent
        
        
    def getValue(self):
        return self.value       
    def getLeftBranch(self):
        return self.leftBranch
    def getRightBranch(self):
        return self.rightBranch
    def getParent(self):
        return self.Parent
    def __str__(self):
        return self.value
        
        
        
def buildDTree(sofar, todo):
    #build decision tree map out every possible out come 
    #sofar (what element is in the tree so far) and todo (elements that need to add to the tree) list of elements
    if len(todo) == 0:
        return binaryTree(sofar)
    else:
        #build a tree by adding decisions of adding or not adding elements
        #build a tree with the element
        withelt = buildDTree(sofar + [todo[0]], todo[1:])
        #build a tree without the element in it
        withoutelt = buildDTree(sofar, todo[1:])
        here = binaryTree(sofar)
        here.setLeftBranch(withelt)
        here.setRightBranch(withoutelt)
        return here
#constraint function limiting the weight in Knapsack
def weightBelow10(list):
    wts = [e[1] for e in list]
    return sum(wts) <= 10
    '''
    sum = 0
    for i in list:
        sum += i
    return sum < 10
    '''
#valueFcn to add the values in the list
def sumValue(list):
    vals = [e[0] for e in list]
    return sum(vals)
    '''
    sum = 0
    for i in list:
        sum += i
    return sum
    '''
def DFSDTree(root, valueFcn, constraintFcn):
    #element in stack tracks what part of the tree it is exploring
    stack = [root]
    best = None
    visited = 0
    while len(stack)> 0:
        visited += 1
        #if value is within constrainFcn limit, search for the best solution
        if constraintFcn(stack[0].getValue()):
            if best == None:
                best = stack[0]
            #compare the best value to current value to find the best
            elif valueFcn(stack[0].getValue()) > valueFcn(best.getValue()):
                best = stack[0]
            temp = stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0, temp.getLeftBranch())
        else:
            #if value is higher than constraintFcn(limit) remove it from stack
            stack.pop(0)
    print 'visited', visited
    return best
    
'''example'''
#example assignment a = [6,3] == a = [value,weight]

a = [6,3]
b = [7,2]
c = [8,4]
d = [9,5]
#sumValue Sum all element's value 
#weightBelow10 sum all the element's weight and return boolean of weight below 10

treeTest = buildDTree([], [a,b,c,d])
DFSDTree(treeTest, sumValue, weightBelow10)