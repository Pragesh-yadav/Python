# Find if a string is pallindrome

string = input()
check = ""
for i in string[-1::-1]: # also write like this [::-1]
    check += i

if string == check:
    print(True)
else:
    print(False)
    
print(check)

