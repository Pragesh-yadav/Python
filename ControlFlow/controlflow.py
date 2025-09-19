# age = int(input())
# if age > 18:
#   print("You Can Drive");
# else:
#   print("Can't Drive, Just Wait to turn 18")




# Nested if else Control flow 
# if(age > 18):
#   if(age >= 65):
#     print("Take Care")
    
#   else:
#     print("You are eligible")
#     print("Drive slow")
    
# else:
#   print("Can't Drive, Just Wait to turn 18")


# Check the number is positive or zero or negative

# num = int(input())

# if(num > 0):
#   print("Positive")
# elif(num == 0):
#   print("Zero")
# else:
#   print("Negative")

# Find Maximum in the List => Consider that list is not empty;
# List = [90, 50, 40, 100, 95]
# highest = List[0]
# for i in List:
#   if i > highest:
#     highest = i
# print(highest)


marks = int(input())

if marks >= 90 and marks <= 100:
    print("A")
elif marks >= 80 and marks < 90:
    print("B")
elif marks >= 70 and marks < 80:
    print("C")
elif marks >= 60 and marks < 70:
    print("D")
elif marks < 60:
    print("E")
else:
    print("Invalid")