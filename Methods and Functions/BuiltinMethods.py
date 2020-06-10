#Functions
def add_function(num1,num2):
    return num1+num2
result = add_function(2,3)
# print(result)

def squre_function(num):
    return num**2
result = squre_function(5)
# print(result)

def name_function(name = 'NAME'):
    '''
    DOCSTRING : Information about the function
    Input: name
    Output: hello name
    '''
    # print("hello ",name)
name_function('ronak')

#biggest of 2 numbers
def max_function(num1,num2):
    if num1>num2:
        return (num1,"is max")
    else:
        return (num2,"is max")
result = max_function(5.7,5.5)
# print(result)
result= sum(range(0,6))
# print(result)
# Find our if the word "dog" is in the string
def dog_check(dog_string):
    return 'dog' in dog_string.lower()
result = dog_check("my dogger is missing")
print(result)


##PIG LATIN "data encocding method"

def pig_latin(word):
    first_letter = word[0]
    if first_letter in 'aeiou':
        pig_word = word+'ay'
    else:
        pig_word = word[1:]+first_letter+'ay'
    return pig_word

def word_order(word):
    listData = [iteam for iteam in word]
    listData.sort()
    return listData

result = pig_latin('ronak')
x=word_order(result)
print(x)

#Prime Number
def prime_number(number):
    if number>1:
        for i in range(2,number):
            if number%2 ==0:
                return (" not prime number")
            elif i == (number%2+1) :
                return ("Prime number")
result=prime_number(2)
print(result)

#Sum of n numbers suing *args
def sum_of_numbers(*argu):
    return sum(argu)*0.05
re1=sum_of_numbers(5000)
# print(re1)

#finding fruit or vegi using **kwargs (keyword arguments)
def fruit_find(**kwargs):
    if 'fruit' in kwargs:
        print("my fruit choice is {}".format(kwargs['fruit']))
    elif 'vegi'in kwargs:
        print("my vegi choice is {}".format(kwargs['vegi']))
    else:
        print("I don't find any fruit or vegi's")
fruit_find(fruits = 'apple',vegis = 'cabage', other = 'choco')

# Using both *args and **kwargs
def my_function(*args,**kwargs):
    for data in args:
        if data == 1:
            print(kwargs['fruit'])
        else:
            print(kwargs['vegges'])
my_function(2, fruit='apple', vegges='carrot')