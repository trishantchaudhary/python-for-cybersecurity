def greet(name):  # parameter name
    print(f"Hello, {name}")


greet("trishant") # argument "trishant" is passed to the function greet



#function arguements

# 1. default argument - use predefined value when no value is
# passed during function call


def myFun(x,y=55):
    print("x :" ,x)
    print("y:",y )

myFun(10) # y is not provided its uses default 50


# keyword arguemnts :
# pass values using parameter names, orderdoesnt matter at all

def student(name, classs):
    print(name,classs)

student(name="trishant",classs='8th')
student(name="tris",classs='9th')



# positional arguements
# values are assigned to parameters based on their order in the function call

def nameAge(name, age):
    print("Hii, I am", name)
    print("my age", age)

print("case1")
nameAge("trish", 45)

print("case2")
nameAge(56,"trish")

# tried but positional arguemnts and parameter arguemtns giving same results lol



# arbitrary arguments : aall  functions to accepts multiple values



## *args and **kwargs

## *args multiple positional arguments

def port_scan(*ports):
    for port in ports:
        print(f"scanning port {port}")


x = port_scan(22, 80, 443, 8080) # multiple arguments passed to the function port_scan

print(x) # None is printed because the function port_scan does not return any value



# **kwargs multiple keyword arguments

def user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


user_info(name="trishant", age=20, country="india") # multiple keyword arguments passed to the function user_info




# inner function
# a function defined inside another function is called inner function

def f1():
    s = 'I love coding'
    def f2():
        print(s)
        
    f2()
f1()






## if need to use functions output in other functions, we can return the output of the function and use it in other functions

def add(a, b):
    return a + b

result = add(5, 10) # the output of the function add is stored in the variable result
print(result) # 15 is printed because the function add returns the sum of a and b


x = add(5, 10) # the output of the function add is stored in the variable x
print(x) # 15 is printed because the function add returns the sum of a and b




# Pass by reference  and pass by value
# Variables refer to objects. Function behavior depends on 
# whether the object is mutable or immutable.

# mutable = lists
# immutable = integers

def myF(x):
    x[0] = 30

b = [10,11,13,4]

myF(b) # modifies the first element becuase lists are mutuable
print(b)

def myF2(x):
    x = 20

a = 10
myF2(a) #strings are immutable so cant modify
print(a)




