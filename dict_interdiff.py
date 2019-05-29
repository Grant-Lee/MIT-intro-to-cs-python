def f(a,b):
    return a > b
def dict_interdiff(d1,d2):
    temp1 = {}
    temp2 = {}
    main = (temp1,temp2)
    for i in d1.keys():
        for j in d2.keys():
            if j not in d1.keys():
                temp2[j] = d2[j]
            if i == j:
                temp1[i] = f(d1[i] , d2[i])
        if i not in d2.keys():
            temp2[i] = d1[i]        
            
    return main
                
d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
print dict_interdiff(d1,d2)