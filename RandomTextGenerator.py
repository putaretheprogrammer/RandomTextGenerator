import random as r

alphaChars = ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'k', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
randChars = []

print("character count: ")
charCount = int(input())
for a in range(charCount):
    randChars.append(r.choice(alphaChars))

print("".join(randChars))
