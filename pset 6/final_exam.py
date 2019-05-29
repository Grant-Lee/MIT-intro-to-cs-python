d = {1:10, 2:20, 3:30, 4:30}
c = {4:True, 2:True, 0:True}
def dict_invert(d):
    temp = []
    invert_dict = {}
    for i in d:
        temp.append(i)
    temp = sorted(temp)
    for i in temp:
        if d[i] in invert_dict:
            invert_dict[d[i]].append(i)
        else:
            invert_dict[d[i]] = [i] 
    return invert_dict
#print dict_invert(c)
#print dict_invert(d)

#final exam P4 part 1

L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
n = 4
L2 = [1, 1, 1, 1, 4]
n2 = 2

def getSublists(L, n):
    master = []
    L_dupe = L
    while len(L_dupe) >= n:
        temp_sub = []
        for i in range(n):
            temp_sub.append(L_dupe[i])
        master.append(temp_sub)
        L_dupe = L_dupe[1:]
    return master

#print getSublists(L,6)


def longestRun(L):
    i = 1
    best = 0
    while i <= len(L):
         for list in getSublists(L, i):
            if list == sorted(list):
                if i > best:
                    best = i
         i += 1
    return best
print longestRun(L)


    
        