import math
#Write a function that computes the volume of a sphere given its radius.
def vol(radious):
    return (4/3) * math.pi * radious ** 3
v1 = vol(2)
print(v1)

#Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(number,low,high):
    if number >= low and number <=high:
        return "The given number in the range"
    else:
        return "the given number is not in range"
v2 = ran_check(3,1,10)
print(v2)

def ran_check1(number,low,high):
    return number >= low and number<= high+1
v2 = ran_check1(11,1,10)
print(v2)

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
#
# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33
def up_low(string):
    up_count,low_count = 0,0
    my_list1 = [item for item in string if item != ' ']
    for item1 in my_list1:
        if item1.isupper():
            up_count = up_count+1
        elif item1.islower():
            low_count +=1
        else:
            pass
    return (f"No. of Upper case characters : {up_count} \nNo. of Lower case Characters : {low_count} ")
v3 = up_low('World War $$Ends')
print(v3)

# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
def unique_list(number_list):
    unique_list = []
    for item in number_list:
        if item not in unique_list:
            unique_list.append(item)
    print("unique",unique_list)
unique_list([1,1,1,2,3,4,4,4])


# Write a Python function to multiply all the numbers in a list.
# Sample List : [1, 2, 3, -4]
# Expected Output : -24
def muliply(num_list):
    multi = 1
    for i in num_list:
        multi = multi * i
    print("multiply list of numbers : ",multi)
muliply([1,2,3,-4])


# Write a Python function that checks whether a word or phrase is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward,
# e.g., madam,kayak,racecar, or a phrase "nurses run".
# Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces.
# Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.
def palindrome(word):
    word = word.replace(' ','')
    if word == word[::-1]:
        print("The given word is palindrome")
    else:
        print("The given word is not a palindrome")
palindrome("nurses run")


# Hard:
# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
import string
def ispangram(str1, alphabet = string.ascii_lowercase):
    alphabet = set(alphabet)
    str1 = str1.replace(' ','')
    str1 = str1.lower()
    str1 = set(str1)
    print(sorted(alphabet),'\n',sorted(str1))
    return str1 == alphabet
v4 = ispangram("The quick brown fox jumps over the lazy dog")
print(v4)