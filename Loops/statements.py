# In Python we have three statement like pass, continue and break


# 1. Pass

# pass statement will use when you don't know what will i print or return this function or menthos then use pass statment

for i in range(5):
    pass # here i used pass statement because i don't know what should print


# 2. Continue

# continue statement is used when you want to skip like you are printing a number 1 to 10 but i want to skip 7 because 7 is a enmy.

for i in range(1, 11):
    if i == 7: # when i == 7 then continue statement will execute and skip the print statement 
        continue  # print statement is only skip that time when i == 7
    print(i) 
    

# 3. break

# break statemnt is used when you don't want to go further or don't want to execute that part of code 

for i in range(1, 11):
    if i == 7:  # here when i== 7 break statement will execute in that case i will print only 6 times.
        break
    print(i) 
