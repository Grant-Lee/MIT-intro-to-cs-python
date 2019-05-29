s = 'azcbobobegghakl'
key = 'bob'
count = 0
while s.find(key) != -1:
    count = count + 1
    s = s[s.find(key) + 2:]
    
print "Number of times bob occurs is: %i" % count