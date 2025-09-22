first = input()
second = input()

print(first + second)

s = "a"
# we have two method in string concatenation
# first

print(s + s + s) # output is aaa

# second
print(s*3) # return aaa

# Note- but you can not concatinate string and number 
# Error :- TypeError: can only concatenate str (not "int") to str
# we can't add int with string
# print("2" + 2)


print("2" + "2") # return 22

# we can't multiply string to string
# like "Pragesh" * S
# Error :- TypeError: can't multiply sequence by non-int of type 'str'
print("pragesh" * s)




