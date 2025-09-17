print(True and True)
print(2 > 3 and 3 > 2)
# logical and operators
#  Only return when both the condition is true;


#  Logical or & not operators
print("Logical or & not operators")
print(True or True)
# In Logical or operator return True if any one of the condition is True;

print(2 > 3 or 3 > 4)

#  Not operator not true => flase and not False => true;


print(not 3 > 2)
print(not 2 > 3)

#  Special operators
#  1. in operator (membership operator)
#  2. is operator;
name = "Pragesh Singh"

print("a" in name) # return true because a is present name
print("D" in name) # return False because D is not present in name;

print(" " in name) # return true because white space is present in name;

# is operator tells you if both object are at same memory location

a = 5
b = 8
print(id(a), id(b))
print(a is b) # return false because both object are store at different location;
# if both object location is same then it will return true;

