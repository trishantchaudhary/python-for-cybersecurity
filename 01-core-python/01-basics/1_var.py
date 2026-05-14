# variables in python

variable_name = 20

print(variable_name)



## assigning values to variables

# 1.basic assignment

x = 5
y = 3.14

# dynamic typing

x = 10
x = "its string now"

# assigning same value to multiple variables

a = b = c = 10
print(a,b,c)   # 10,10,10

""" object of reference

 when x = 5 is executed, python creates an object to represent
 the value 5 and makes x reference of this object\

 x ------> [5]

 lets assign another variable y to the variabel x
 y = x

 now this creates  y and refrences the same object as x , 
 not itself x, this is called shared refrences 
 where multiple variables reference the same object

 x ----------> [5] <----------y

now if i write x = 'trish'
python creates a new object for the value trish and makes x 
 reference this new obj


y ------> [5]
          [trish] <------- x
 and y remains unchanged, still refrencing the original ojb 
 5 but if i assign new value to y

y = yo

          [5]<---------garbage
 ------>[trish]
        [yo]. <--------- y


python var stores refrences to ojb not the actual values themselves, 
when we reassigned variable its starts referncing to new object 

"""

# scope of variables

x = 10 # global

def my_function():
    y = 30 # local
    print(x)
    print(y)

my_function()

print(x)
print(y)


# for modifying global variable inside a function first
# we need to delcare it global

# deleting a variable

x = 4
del x
print(x)









