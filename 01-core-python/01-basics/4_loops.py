# if-else

age = 20

if age >= 18:
    print("you are hacker")
else:
    print("you are not hacker")



## if-elif-else

if age >=19:
    print("you are hacker")
elif age == 18:
    print("you are not hacker but you can learn hacking")

else:
    print("you are not hacker")



## nested if-else


x = 28
has_hacking_knowledge = True


if x <= 25 and x >=18:
    if has_hacking_knowledge:
        print("you are hacker")
    else:
        print("you are not hacker but you can learn hacking")

elif x >= 28:
    print("you are not hacker you are too old to learn hacking")

else:
    print("lol")



## Loops



# for loops
# when you know the number of iterations in advance, you can use for loops. The syntax is as follows:


#for variable in sequence:
    # do something with variable
    ##pass


fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


# string

for char in "banana":
    print(char)


for i in range(5): # range(1,5) will give 1,2,3,4
    print(i)








for i in range(5):
    if i == 3:
        break
    print(i)


for i in range(5):
    if i == 3:
        continue
    print(i)    


for i in range(5):
    if i == 3:
        pass
    print(i)



## while loops
# when you don't know the number of iterations in advance, you can use while loops. The syntax is as follows:


#while condition:
    # do something
    #zpass



x = 1

while x <=5:
    print(x)
    x += 1


# password checkers
password = "hacker5"

user_input = ""

while user_input != password:
    user_input = input("Enter password: ")
    if user_input != password:
        print("Access denied!")
    

print("Access granted!")


## nested loop 

for i in range(1,5):
    print(i)
    for y in range(i):
        print(i, end='')
    print()


