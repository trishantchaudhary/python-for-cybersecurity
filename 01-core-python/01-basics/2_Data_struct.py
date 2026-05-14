# Strings are sequence of characters written inside quotes. 
# It can include letters, numbers, symbols and spaces
# are immutable




# multiline strings

s = """I am Learning
Python String on mac"""
print(s)

s = '''I'm a 
hacker'''
print(s)

# string operations


# ==========================================
# CYBERSECURITY USER PROFILE SYSTEM
# Python String Concepts - Complete Example
# ==========================================

# 1. Creating Strings
username = "Trishant"
role = "Security Analyst"
skill = "Python Programming"
status = "active"

print("=" * 45)
print("CYBERSECURITY USER PROFILE")
print("=" * 45)

# 2. String Indexing
print("\n--- STRING INDEXING ---")
print("First character:", username[0])
print("Third character:", username[2])
print("Last character:", username[-1])

# 3. String Slicing
print("\n--- STRING SLICING ---")
print("First four characters:", username[0:4])
print("First word of skill:", skill[:6]) # from start onyl 6 leters
print("Last four characters:", username[-5:-3]) # means only give 2 letters from last and choose 1
print("Reversed username:", username[::-3]) # means :: al letters and choose 3rd letter from last

# 4. String Looping
print("\n--- STRING LOOPING ---")
for character in username:
    print(character)

# Looping with condition
print("\nVowels in username:")
for character in username:
    if character in "aeiou":
        print(character)

# 5. String Immutability
print("\n--- STRING IMMUTABILITY ---")
original = "hacker"

# original[0] = "H"  # TypeError: strings are immutable
# Yahan hum index 0 par 'P' assign karne ki koshish kar rahe hain
#username[0] = "P"

print(username)

updated_word = "H" + original[1:]
print("Original string:", original)
print("New string:", updated_word)

# 6. String Updating
print("\n--- STRING UPDATING ---")
message = "I am learning Java"
message = message.replace("Java", "Python")
print("Updated message:", message)

# Update username capitalization
username = username.upper()
print("Uppercase username:", username)

# 7. String Deleting
print("\n--- STRING DELETING ---")
text = "Cyber Security Course"
text = text.replace("Cyber ", "")
print("After removing Cyber:", text)

# Delete a variable binding
temporary_data = "Temporary information"
del temporary_data
print("Temporary variable deleted successfully")

# 8. Common String Methods
print("\n--- COMMON STRING METHODS ---")
raw_text = "   python security   "

print("Uppercase:", raw_text.upper())
print("Lowercase:", raw_text.lower())
print("Title case:", raw_text.title())
print("Stripped:", raw_text.strip())
print("Replace:", raw_text.replace("python", "cyber"))
print("Find security:", raw_text.find("security"))
print("Count of 't':", raw_text.count("t"))
print("Starts with spaces:", raw_text.startswith("   "))
print("Ends with spaces:", raw_text.endswith("   "))
print("Split into words:", raw_text.split())

# 9. Concatenating Strings
print("\n--- STRING CONCATENATION ---")
first_name = "Trishant"
last_name = "Sharma"

full_name = first_name + " " + last_name
print("Full name:", full_name)

profile = username + " works as a " + role
print("Profile:", profile)

# 10. Repeating Strings
print("\n--- STRING REPETITION ---")
print("-" * 30)
print("SECURITY REPORT")
print("-" * 30)

warning = "WARNING! "
print(warning * 3)

# 11. String Membership Testing
print("\n--- MEMBERSHIP TESTING ---")
description = "Trishant is learning Python security"

print("'Python' present:", "Python" in description)
print("'Java' present:", "Java" in description)
print("'Java' absent:", "Java" not in description)
print("'security' present:", "security" in description)

# Case-sensitive membership
print("'python' present:", "python" in description)

# 12. String Formatting with f-strings
print("\n--- STRING FORMATTING ---")
username = "Trishant"
role = "Security Analyst"
experience = 2
score = 95.567

print(f"Username: {username}")
print(f"Role: {role}")
print(f"Experience: {experience} years")
print(f"Assessment score: {score:.2f}%")

# Formatting with expressions
print(f"Next experience milestone: {experience + 1} years")

# 13. String Formatting with format()
report = "User {} has role {}.".format(username, role)
print(report)

# 14. Final Combined Report
print("\n" + "=" * 45)
print("FINAL SECURITY REPORT")
print("=" * 45)

final_report = (
    f"User: {username}\n"
    f"Role: {role}\n"
    f"Skill: {skill}\n"
    f"Status: {status.upper()}\n"
    f"Assessment: {score:.2f}%"
)

print(final_report)

print("=" * 45)



# ==========================================
# list in python , mutables
# ==========================================

print("\n--- List in python ---")
print("\n" + "=" * 45)

# list in python , mutables

list = [1, 'hello', 4, 5]
print(list)


list = [1, 2, 3, 4, 5]
print(list)



print(list[0])  # prints first element of list
list.append(6)  # adds 6 to the end of list
list.remove(3)  # removes 3 from the list


list[1] = 20  # changes the second element of list to 20



#list compression in python

# squaring every number in list
a = [2, 3, 4, 5]
res = [val ** 2 for val in a]
print(res)


# conditional statement in list compression
a = [1, 2, 3, 4, 5]
res = [val for val in a if val % 2 == 0]
print(res)


# creating a list from range
a =[i for i in range(10)]
print(a)

# neested looops

c = [(x, y) for x in range(3) for y in range(3)]
print(c)
#[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]





################################### tuples ###################################

print("\n" + "=" * 45)
print("\n--- Tuples in python ---")
print("\n" + "=" * 45)


# tuples in python are immutuable, ordered collection of elements.

#creating a tuples

tup = ()
print(tup)

# Using String
tup = ('Geeks', 'For')
print(tup)

# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple('Geeks')
print(tup)


# with mixed datatypes

tup = (5, 'Welcome', 7.5, True, [1, 2, 3], {'key': 'value'})
print(tup)



################################### dictionary ###################################

print("\n" + "=" * 45)
print("\n--- dictionary in python ---")
print("\n" + "=" * 45)





# dictionary in python, are immutables


hacker_info = {
    'name' : 'trishant',
    'age' : 20,
    'language' : 'python',
    'skills' : ['python', 'web sec', 'ai sec'],
    'hobby' : 'reading'
    
}


print(hacker_info['name'])  # prints the value of key 'name'



# nested dictionaries

d = {
    "student": {
        "name": "Me",
        "age": 20
    }
}

print(d["student"]["name"])




################################### sets ###################################

print("\n" + "=" * 45)
print("\n--- sets in python ---")
print("\n" + "=" * 45)


# Set is a built-in Python data type used to store a collection of unique items.
# immutable

s = {10, 50, 20}
print(s)
print(type(s))

# type casting
s = set(["a", "b", "c"])
print(s)

# a set cannot have duplicate values
s = {"x", "for", "x"}
print(s)

# values of a set cannot be changed
#s[1] = "Hello"
print(s)

# frozen set is an immutable version of set,its element cant be change
# after creation, but we can perform actions likes union intersections etc

s = set(["a", "b", "c"])
print("Normal Set:", s)

fs = frozenset(["e", "f", "g"])
print("Frozen Set:", fs)


# adding elements

s = {"a", "b", "c"}
s.add("d")
print(s)

# union 

a = {"x", "y"}
b = {"y", "z"}
u = a.union(b)
print(u)

# clear function removes all elements from set
s = {1, 2, 3}
s.clear()
print(s)






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

import numpy as np
a = np.array([1,2,4,5])

# element-wise operations
print(a * 2)

# multi-dimensional array
res = np.array([[1,2],[3,4]])
print(res * 2)



# array - pythons array module for simple

# creating an array
import array as arr
a = arr.array('i',[1,2,3])

for i in range(0,3):
    print(a[i], end="")








