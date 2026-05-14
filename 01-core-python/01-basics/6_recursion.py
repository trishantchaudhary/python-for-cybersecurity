
# basically its a technique where a function to call itself directly or indirectly
# to solve a problem
# 1. breaking problems into smaller prbolems
# 2. maths calculations like fabonacci


# base case : stopping condition that prevents infinite recursion
# recursive case : part of function where it calls its self


def factorial(n):
    if n == 0: # base case
        return 1 
    else:
        return n * factorial(n-1) # recursive case

print(factorial(5))

# when we will got n ==0 it will return 1



# fabonacci series in recursion
# fabonacci means
# this is sequence. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# rule is simple
# 1. Pehla number 0
# 2. Doosra number 1
# 3. Uske baad har number = pichhle do numbers ka sum

# calculating nth number 

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(10))
    



