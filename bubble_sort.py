
def bubble(L):
    if len(L) == 0 or len(L) == 1:
        return L
    else:
        count = 0
        i = 0
        biggest = L[0]
        while count < len(L):
            for j in range(len(L)):
                print L[i], L[j], L
                if biggest > L[j]:
                    biggest = L[j]
                    
            count += 1
                    
        return L

print bubble([3, 7, 2, 9, 5,4,1])