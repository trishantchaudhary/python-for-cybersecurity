# first class functions in python 
# functions are treated as first-class objects. This means they can be used just like numbers, 
#strings, or any other variable. You can:


# assigning functions to variables

def msg(name):
    return f"hello, {name}"

x = msg

print(x("trish"))

# passing functions as arguements

def msg(name):
    return f"hello,{name}"

def fun1(fun2,name):
    return fun2(name)
#PASSING msg functions as an arguemnt

print(fun1(msg,"trishant"))



# return functions from other functions




def fun1(msg):
    def fun2():
        return f"Message: {msg}"
    return fun2

# Getting the inner function
func = fun1("Hello, World!")
print(func())


# storing functions in datastructures

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# Storing functions in a dictionary
d = {
    "add": add,
    "subtract": subtract
}

# Calling functions from the dictionary
print(d["add"](5, 3))       
print(d["subtract"](5, 3))