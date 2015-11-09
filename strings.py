#Flips a string and returns it
def flip(string):
    newString = ''
    for i in range(0, len(string)):
        newString = newString + string[len(string) - i - 1]
    return newString
#get the count of vocals the given string contains
def getVocals(string):
    vocals = 0
    for char in string:
        if char.lower() in 'aeiou':
            vocals = vocals + 1
    return vocals

hw = "Hello World!"

print(hw + " = " + flip(hw))
print(hw + " has ", getVocals(hw), " vocals")
