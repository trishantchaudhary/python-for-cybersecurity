# arthmetic operators in python

a = 10
b = 5

print(a + b)  # addition
print(a - b)  # subtraction
print(a * b)  # multiplication
print(a / b)  # division
print(a % b)  # modulus
print(a ** b)  # exponentiation
print(a // b)  # floor division

## bitwise operators in python

x = 10  # binary: 1010
y = 4   # binary: 0100      

print(x & y)  # bitwise AND
print(x | y)  # bitwise OR
print(x ^ y)  # bitwise XOR
print(~x)     # bitwise NOT
print(x << 1)  # left shift
print(x >> 1)  # right shift
print(x >> 2)  # right shift by 2
print(x << 2)  # left shift by 2



## comparison operators in python


a = 10
b = 20  

print(a == b)  # equal to
print(a != b)  # not equal to
print(a > b)   # greater than
print(a < b)   # less than
print(a >= b)  # greater than or equal to
print(a <= b)  # less than or equal to

##  ID operators in python

a = 20
b = 10

print(a is b)  # returns True if both variables are the same object
print(a is not b)  # returns True if both variables are not the same object



## logical operators in python

a = True
b = False

print(a and b)  # returns True if both statements are true
print(a or b)   # returns True if one of the statements is true
print(not a)    # returns True if statement is fals


## membership operators in python

hacker_tools = ['nmap', 'metasploit', 'burpsuite', 'wireshark']
print('nmap' in hacker_tools)  # returns True if 'nmap' is present in hacker_tools
print('sqlmap' not in hacker_tools)  # returns True if 'sqlmap'


x = 8
y = 3

result = (x % y == 2) and (x // y > 2)
print(f"lets test : {result}")
print(x//y)