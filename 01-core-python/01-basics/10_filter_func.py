# filter function used to extract element from iterable like list, tuple or set
# that satisfy a given condition
#  It works by applying a function to each element


def start_a(w):
    return w.startswith("a")

li = ["apple","bnsns","mango","akash"]

store = filter(start_a, li)
print(list(store))

# apple aakash


#2
def even(n):
    return n % 2 == 0

a = [1, 2, 3, 4, 5, 6]
b = filter(even, a)
print(list(b)) # Convert filter object to a list

# 2,4,6


