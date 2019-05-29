def mergeL(L1,L2):
    new = []
    i, j = 0, 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            new.append(L1[i])
            i += 1
            if len(L1) == 0:
                new = new + L2
                break
        else:
            new.append(L2[j])
            j += 1
            if len(L2) == 0:
                new += L1
                break
    return new
L1 = [1,5,12,18,19,20]
L2 = [2,3,4,17]
print mergeL(L1,L2)
