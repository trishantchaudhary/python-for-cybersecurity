# reduce function combine any iterable like list one by one and gives single result
# at the end

from functools import reduce

numbers = [10, 20, 30, 40]

result = reduce(lambda a, b: a + b, numbers)

print(result) # --------> 100


# accumulate 
# its also combine iterable  elments but also give intermidiate result with final



from itertools import accumulate

numbers = [10, 20, 30, 40]

result = list(accumulate(numbers))

print(result)

# [10, 30, 60, 100]
