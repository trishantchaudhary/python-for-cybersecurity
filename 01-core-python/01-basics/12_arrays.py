################################### arrays ###################################

print("\n" + "=" * 80)
print("\n------------------------Array in python --------------")
print("\n" + "=" * 80)



# array is such data structure in which we can store multiple values in single variable

# like think if you need to umm scan ports so

p1 = 90
p2 = 80
p3 = 443

# but with array we can do it in smart way

p = [90,80,443]

# in other programming languages like c or c++ arrays have strict rules
# but in python lists works behalf of arrays

# numpy arrays are part of numpy library

#import numpy as np
#a = np.array([1,2,4,5])

# element-wise operations
#print(a * 2)

# multi-dimensional array
#res = np.array([[1,2],[3,4]])
#print(res * 2)



# array - pythons array module for simple

# creating an array
import array as arr
a = arr.array('i',[1,2,3])

for i in range(0,3):
    print(a[i], end="")

# i means signed int its typecode tells python treat elements as signed int


# adding elements 
import array as arr

a = arr.array('i',[1,2,3])
print(*a) # 1,2,3 called upacking with asterk
print(a)

a.insert(1,4) # inserting 4 at index 1

print(*a)


# accessing items 

import array as arr
a = arr.array('i', [1, 2, 3, 4, 5, 6])

print(a[0])
print(a[3])

b = arr.array('d', [2.5, 3.2, 3.3])
print(b[1])
print(b[2])


# searching element

import array
a = array.array('i', [1, 2, 3, 1, 2, 5])

# index of 1st occurrence of 2
print(a.index(2))

# index of 1st occurrence of 1
print(a.index(1))

# operations on array

import array as arr
a = arr.array('i',[1,2,3,4,5,6,7,2,2,2,2])
count = a.count(2)
print(count)


#reversing array

import array as arr
a = arr.array('i',[1,2,3,4,5])
a.reverse()
print(*a)

#extend array

import array as arr 
a = arr.array('i', [1, 2, 3,4,5])
a.extend([6,7,8,9,10])
print(a)






##################### unpacking array as astrek ###########

#The unpacking techniques you use with lists also apply to python arrays, but with 
#slight differences due to the nature of the array module

import array
arr = array.array('i',[1,3,4])
a,b,c = arr
print(a)
print(b)
print(c)


# unpacking array with astrek operator

import array

arr = array.array('i', [1, 2, 3, 4, 5])
a, *rest, e = arr
print(a)     # 1
print(rest)  # [2, 3, 4]
print(e)     # 5








