def flatten(aList):


    #empty flatten list call flat
    flat = []
    #check for list
    for i in aList:
        if isinstance(i, list):
            flat = flat + flatten(i)
        else:
            flat.append(i)
    return flat
a = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print flatten(a)