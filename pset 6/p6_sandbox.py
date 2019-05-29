import string
shifted = {}
key = 0
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
for i in range(26):
    if i + key < 26:
        shifted[lowercase[i]] = lowercase[i+key]
    else:
        shifted[lowercase[i]] = lowercase[i+key-26]

for j in range(len(uppercase)):
    if j + key < len(uppercase):
        shifted[uppercase[j]] = uppercase[j+key]
    else:
        shifted[uppercase[j]] = uppercase[j+key-26]
        
#print shifted
#print lowercase

message = "Hello World!"
encrypted = ''
for letter in message:
    if str.isalpha(letter):
        encrypted += shifted[letter]
    else:
        encrypted += letter
print encrypted
    