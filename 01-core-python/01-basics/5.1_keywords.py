# pass keyword is a placeholder that does nothing when executed


# in functions : 
# when we define a function but dont want to implement
#its logic

def fun():
    pass

fun()


# In conditional statements
# just for syntax its a placeholder simply

x = 10

if x > 5:
    pass #placeholder for future logic
else:
    print("x is less")


# In loops :
# no just for syntax
for i in range(5):
    if i == 3:
        pass # do nothing when i is 3 only saves sysntax
    else:
        print(i)



# In Classes :
# the pass statment allows defining empty classes or methods
# that acts as placeholders simply

class EmptyClaas:
    pass # no moethods or attributes yet

class Person:
    def __init__ (self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        pass # placeholder for greet method

p = person("trish",22)




    
