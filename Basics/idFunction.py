x = 5
id(x) # id will return address of variable x


# now change the value of x 
x = 35
print(id(x)) # now this time it will return different address

# because of stack and heap memory first x has 5 and then x is break up with 5 and dereference if and patch up with 35 then new addres reference and it store different memory location.

