# Print multiplication table of given numbers
n = int(input())
print("Table of ", n)
for i in range(1, 11): # using range method start with 1 and end with 10 because 11 is excluded and if step or jump will not provide then by default jump by 1
    print(n, "*", i, "=", i * n)
    

''' Pattern - 1 print # like square
# # # #
# # # #
# # # #
# # # #
'''

for i in range(4):
    for j in range(4):
        print("#", end = " ")
    print()


"""
pattern -2 print like this
#
# #
# # #
# # # #

"""

for i in range(n+1):
    for j in range(i):
        print("#" , end = " ")
    print()

