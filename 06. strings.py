string = "This is a string, I assigned the string to a variable named string. Strings can be written in a straight line or multiline"

multilineString = '''
This is a multiline string 
'''
#concatenation: strings can be concatenated. i.e combined together, for example

firstString = 'Stephen'
secondString = 'Oyebamiji'
concatenatedString = "firstString + secondString"

print (concatenatedString)

#indexing: you start indexing from 0

word = "Ogstevyn"

print (word[0])
#to traverse the string using a for loop

for character in word:
 
   print(character)

#to look for the length of a string

print(len(word))

#to check for members in a string

print('o' in word)

#string slicing: to get a sub string of a string.... negative indexing for indexing from the back

line = 'queen'

substring = line[1:3]

print(substring)

# string functions: changing a string to upper case or lowercase
upperCase = 'god'
lowerCase = 'GOAT'

print(upperCase.upper())
print(lowerCase.lower())

'''
Other functions include strip,replace... i.e variable.function
'''
print(upperCase.replace('o','j'))

#to generate a list from your string using a delay meter

names = 'Bimbo Mike Abu'
print(names.split(" "))