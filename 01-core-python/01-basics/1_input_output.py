
#using map
numbers = list(
    map(
        int,
        input("values:").split()
    )
)
print(numbers)


#list compression

numb = [
    int(x)
    for x in input("val:").split()
]
print(numb)


## using a loop


a = []
b = int(input("how many items do u want to entr?"))

for i in range(b):
    val = input(f"enter item {i + 1}:")
    a.append(val)

for i in a:
    print(i)

print(a)



