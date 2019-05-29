s = 'yqyyov'
k = 'aeiou'
i = 0
count = 0
while i < len(s):
    j = 0
    while j < len(k):
        if s[i] == k[j]:
            count = count + 1
        j = j + 1
    i = i + 1
print "Numbers of Vowels: %i" % count



    