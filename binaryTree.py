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
    



'''Depth first search function'''
def find6(value):
    return value.getValue() == 9
    
def DFSBinary(root, fcn):
    stack = [root]
    while len(stack) > 0:
        print 'at node ' + str(stack[0].getValue())
        if fcn(stack[0]):
            return True
        else:
            temp = stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0, temp.getLeftBranch())
    return False
    
def BFSBinary(root, fcn):
    queue = [root]
    while len(queue) > 0:
        print 'at node ' + str(queue[0].getValue())
        if fcn(queue[0]):
            return True
        else:
            temp = queue.pop(0)
            if temp.getLeftBranch():
                queue.append(temp.getLeftBranch())
            if temp.getRightBranch():
                queue.append(temp.getRightBranch())
    return False

def DFSBinaryOrdered(root, fcn, target):
    queue = [root]
    
    while len(queue) > 0:
        print 'at node ' + str(queue[0].getValue())
        if fcn(queue[0]):
            return True
        else:
            temp = queue.pop(0)
            if temp.getValue() < target and temp.getRightBranch():
                queue.append(temp.getRightBranch())
            if temp.getValue() > target and temp.getLeftBranch():
                queue.append(temp.getLeftBranch())

    return False
                
n5 = binaryTree(5)
n2 = binaryTree(2)
n1 = binaryTree(1)
n4 = binaryTree(4)
n3 = binaryTree(3)
n8 = binaryTree(8)
n6 = binaryTree(6)
n7 = binaryTree(7)

n5.setLeftBranch(n2)
n2.setParent(n5)
n5.setRightBranch(n8)
n8.setParent(n5)
n2.setLeftBranch(n1)
n1.setParent(n2)
n2.setRightBranch(n4)
n4.setParent(n2)
n4.setLeftBranch(n3)
n3.setParent(n4)
n8.setLeftBranch(n6)
n6.setParent(n8)
n6.setRightBranch(n7)
n7.setParent(n6)

#print DFSBinary(n5, find6)
#print BFSBinary(n5, find6)
#print DFSBinaryOrdered(n5, find6, 9)

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
foobar = DFSDTree(treeTest, sumValue, weightBelow10)
print foobar.getValue()