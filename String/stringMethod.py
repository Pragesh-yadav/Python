"""
# capitalize
# title
# upper
# lower
# find
# count
# index
# replace
# split
# islower
# isupper
# isnumeric
# isalpha

"""

name = "pragesh Singh"

print(len(name))
# capitalize() method is change the string first letter with capital.
# Note. not change in original string name.
print(name.capitalize()) 

# title is convert string to capital latter where is white space is given like in name pragesh is converted like => Pragesh and singh is converted like => Singh
# Note not changes in original string.
print(name.title()) 


# upper 
# upper method is convert every letter to a capital letter

print(name.upper())

# lower
#  lower method is used for convert all letter in small letter
print(name.lower())

# find
# find method is return the lowest index position of the word or character
#  if we not provide any argumnet in find method then i will return 0.
print(name.find(""))

# count
# In count method if we not provide any argument then it will return len + 1
#  count method return the count of the character or word in your string
print(name.count("s")) # it will return 2 because s is occur two times

# index
# In index method if you not provide any argument in side the quotes then it will return 0 
# it will return the lowest index pisition of the word.
# if word is not found then it will through error like ValueError: substring not found
print(name.index("")) # it will return 5 beacuse index start with 0


# replace
# In replace method minimum 2 argument is required first argument is what word you want to replace and second argument is replace with 
print(name.replace("s", "S"), "") # here i want to replace small s to with capital S
# Note if, in your string small s is not present then it will change nothing and return original string


# split
# By default if we not provide any argument then it will cut with space and return as a list in string formate

print(name.split("S")) # cut with S and return in list of string ['prage', 'h ', 'ingh']

# islower
# islower is return boolean value
# if your string is pure lower case then i will return True otherwise it will return False
print(name.islower()) # it will return False because my string is not a pure lower case string

print("pragesh".islower()) # it will return True because string is in pure lower case

# isupper
# it always return boolean value
# if your string is pure upper case then i will return True otherwise it will return False
print(name.isupper()) # return false because string is not in pure uppercase

print("PRAGESH".isupper()) # return true because all the letter of the string is in upper case


# isnumeric
# it will return true only if string is in numeric form

print(name.isnumeric()) # return false
print("133".isnumeric()) # reutrn true because string is in numeric form

# isalpha

print(name.isalpha()) # return false because string contain space 

print("Pragesh".isalpha()) # return true because string contains only string value


print(name)