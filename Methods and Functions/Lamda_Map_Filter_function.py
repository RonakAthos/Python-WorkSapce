import math
def squre(num):
    return num**2
numbers = [1,2,3,4,5,6]

for item in map(squre,numbers):
    print(item)
my_list = list(map(squre,numbers))
print(my_list)


def even_char(word):
    if len(word)%2 == 0:
        return "The word having even character"
    else:
        return word[0]
value = even_char("king")
print(value)

#lambda function
squre1 = lambda num : num ** 3
print(squre1(5))

#map function with lambda function
list1 = list(map(lambda num:num**3,numbers))
print(list1)

#filter function with lambda function
list1 = list(filter(lambda num: num%2 != 0,numbers))
print(list1)

