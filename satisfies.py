
def f(s):
    return 'a' in s
    
def satisfiesF(L):
    i = 0   
    while i < len(L):
        if f(L[i]) == False:
            L.pop(i)
            i -= 1
        i += 1
    return len(L)
    
L = ['a', 'b', 'a', 'c', 'd', 'a']
print satisfiesF(L)
print L
