#  Python applies a function to every element of one or more iterables and 
# returns a map object (iterator) containing the transformed results

# yeah basically kisi function ko iterable ke elements par apply krna

# 1. lets find out squre of every number in list
# normal approach is


numbers = [1, 2, 3, 4, 5]

result = []

for n in numbers:   #using for loop
    result.append(n * n)

print(result)

# but with map we can do this

numbers = [1, 2, 3, 4, 5]

def square(n):
    return n * n

result = map(square,numbers)

print(result) # -----------------> <map object at 0x105e2e5c0> by default it returns object

#lets convert it in list
print(list(result))




# map with lambda(chhota anonymous function doesnt need def)
numbers = [1, 2, 3, 4, 5]
r = list(map(lambda x : x * 2, numbers))
print(r)




# map with multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]

result = list(map(lambda x, y: x + y, a, b))
print(result)



# string manupilation using map


words = ["hello", "python", "security"]
result = list(map(str.upper, words))
print(result)




# extracting first character

words = ["Python", "Security", "Hacking"]
result = list(map(lambda s: s[0], words))
print(result)











