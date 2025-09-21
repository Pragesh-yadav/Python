s = "System"

s1 = 'Machine' # Single line string

# Multiline string 
s2 = """ Hi, how are you
i am good what about you
"""

print(s2)


# chr and ord

print(ord('a')) # ord method is used to know about the ascii value of a character

print(chr(97)) # chr method will return character 

print(chr(2325))

print(chr(35880))

string = "Pragesh Singh"

size = len(string) # len is method to find the length of the string
print(size, "length of the string")

# String have indexing method to iterate through the indexing

# String also have negative indexing method
'''
P r a g e s h   S i  n g  h
0 1 2 3 4 5 6 7 8 9 10 11 12 # In positive indexing index start with 0 and positive 
same as negative indexing
-13 -12 -11 - 10 -9 -8 -7 -6 -5 -4 -3 -2 -1 # In negative indexing index start with negative

'''

print(string[-13])
# Traversing with negative indexing using for loop

# for i in range(-size, -1): # here start with -13 left to right
#     print("Negative Index traversing ","Character " , string[i], "Index position", i)


for i in range(-1, -14, -1): # here i defined the start, stop, step and traversing through right to left
    print("Negative Index traversing ","Character " , string[i], "Index position", i)
    
