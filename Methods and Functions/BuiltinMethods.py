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

result = pig_latin('ronak')
print(result)