#write a function that returns the lesser of two given numbers if both numbers are even,
# but return greater if one or bith number is odd.
from http.cookiejar import uppercase_escaped_char
def even_odd(*args):
    if args[0]%2==0 and args[1]%2==0:
        return min(args)
    else:
        return max(args)

value=even_odd(10,6)
print(value)

#Write a function takes a two word string and return True if both words begine with same letter
def animal_cracker(word):
    list1=word.lower().split()
    return list1[0][0]==list1[1][0]

value = animal_cracker("world war")
print(value)

#OLD_MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(word):
       first_half = word[:3]
       second_half = word[3:]
       return first_half.capitalize()+second_half.capitalize()

value=old_macdonald('oldmacdonald')
print(value)

#MASTER YODA: Give a sentence, return a sentence with the word reverce
def master_yoda(word):
    list1=word.split( )
    list2 = list1[::-1]
    return ' '.join(list2)

value = master_yoda("I am home")
print(value)

#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200¶
def almost_there(number):
   return (abs(100-number)<=10) or (abs(200-number)<=10)

value=almost_there(150)
print(value)

#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    for i in range(0, len(nums) - 1):

        # nicer looking alternative in commented code
        # if nums[i] == 3 and nums[i+1] == 3:

        if nums[i:i + 2] == [3, 3]:
            return True

    return False

value = has_33([1,3,3,0])
print("array contains 3 next to a 3 : ",value)

#PAPER DOLL: Given a string, return a string where for every character in the original there are three ch
def paper_doll(word):
    string1=''
    for iteam in word:
        string1+=iteam*3
    print(string1)
paper_doll('Mississippi')

#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21,
# return their sum. If their sum exceeds 21 and there's an eleven,
# reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def black_jack(a,b,c):
    sum1 = sum([a,b,c])
    if sum1 <= 21:
        return sum1
    elif 11 in [a,b,c] and sum1-10 <=21:
        return sum1-10
    else:
        return 'BUST'
value = black_jack(9,9,11)
print("black_jack",value)

# SUMMER OF '69: Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and extending to the next 9
# (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_of_69(array1):
    total = 0
    add = True
    for num in array1:
        while add:
            if num!=6:
                total += num
                break
            else:
                add = False
        while not add:
            if num !=9:
                break
            else:
                add = True
                break
    return total


array1 = [1,2,3,4,5,6,7,9,5]
value = summer_of_69(array1)
print("sum of 69 ", value)
# print(value)

# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False
def spy_game(numbers):
   code = [0,0,1,'x']

   for num in numbers:
       if num == code[0]:
           code.pop(0)
   return len(code)==1

value=spy_game([1,2,3,4,0,0,9,8])
print("007",value)
# #
# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

def makes_twenty(a,b):
   return (a+b)==20 or a==20 or b==20
value1=makes_twenty(15,10)
print(value1)

#
# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25
# By convention, 0 and 1 are not prime.
def count_prime(num):
    #check for 0 or 1 input
    if num<2:
        return 0
    ##################
    #2 or grater
    ###############
    #to store prime nummbes
    primises = [2]
    #Counter going upto given numbers
    x = 3
    while x<=num:
        for y in range(3,x,2):
            if x%y == 0:
                x+=2
                break
        else:
            primises.append(x)
            x +=2
    print(primises)
    return len(primises)
value = count_prime(6)
print(value)


# Just for fun, not a real problem :)
# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
# print_big('a')
#
# out:   *
#       * *
#      *****
#      *   *
#      *   *
# HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
# For purposes of this exercise, it's ok if your dictionary stops at "E".
def print_big(letter):
    dest = {'1':"*",'2':"**",'3':"***"}
    print(dict['1']['3'])

print_big("a")