name = input()

age = input()

print("My name is", name, ".My age is", age)
#  In above print statement we have a problem if i want to add full stop after the name then it very difficult
# for this problem we have format method in string

print("My name is {}. My age is {}".format(name, age)) # here i used format method to pring the string as i want but sequence is important

# if sequence is change then it will prrint like this
print("My name is {}. My age is {}".format(age, name)) # it will print like this My name is 26. My age is Pragesh