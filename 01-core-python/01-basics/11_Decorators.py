# decorator is a function that modify or extend the functionality of any functions without
# touch their original code 


def decorator(func):
    def wrapper():
        print("before starting")
        func()
        print("after ending")
    return wrapper

@decorator
def greet():
    print("hello world")

greet()




# Decorators with parameters

def decorator_name(func):
    def wrapper(*args, **kwargs):
        print("before start")
        x = func(*args, **kwargs)
        print("after start")
        return x
    return wrapper

@decorator_name
def add(a,b):
    return a + b

print(add(4,5))






    