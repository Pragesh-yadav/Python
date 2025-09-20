# Loops
# 1. while
# 2. for


# 1. while 
# .Initializing value
# . Loop Condition
#  . Updating value



#  print name 6 times;
# Initialize
i = 1
#  loop condition 
while i <= 6:
  # inside body
  print("Python Is Fun")
  # update
  i += 1 # also write like i = i +1

# print all numbers from 1 to 10 using loop

i = 1;
while i <= 10:
    print(i, end = " ") # using end to print in same line 
    i += 1

# Print all even numbers between 1 to 10
print() # Using print statement because next print statement will print to the next line
i = 1
print("Even Numbers")
while i <= 10:
    if i % 2 == 0:
        print(i, end = " ")
    i += 1
    


# Print sum of all numbers from 1 to 10
print()
i = 1
sum = 0 
while i <= 10:
    sum += i
    i += 1

print("Sum = ", sum)

