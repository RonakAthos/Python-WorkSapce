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
    list1=word.split()
    temp=list1[0]
    temp1=list1[1]
    return temp[0]==temp1[0]

value = animal_cracker("world car")
print(value)

#OLD_MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(word):
        listword = [x for x in word]
        listword[0]= listword[0].upper()
        listword[3]=listword[3].upper()
        str = ""
        for ele in listword:
            str = str+ele
        return str

value=old_macdonald('oldmacdonald')
print(value)

#MASTER YODA: Give a sentence, return a sentence with the word reverce
def master_yoda(word):
    list1=word.split( )
    list2 = list1[::-1]
    str =" "
    return (str.join(list2))
value = master_yoda("I am home")
print(value)

#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200¶
def almost_there(number):
    if (number-100)<=10:
        return True
    else:
        return False

value=almost_there(11)
print(value)

#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(listData):
    for index,value1 in enumerate(listData):
        if value1 == 3:
            next_index = index+1
            if listData[next_index] == 3:
                return True
            else:
                return False
value = has_33([1,3,1,3])
print("array contains 3 next to a 3 : ",value)

#PAPER DOLL: Given a string, return a string where for every character in the original there are three ch
def paper_doll(word):
    string1=''
    for iteam in word:
        for iter1 in range(3):
            string1 +=iteam
    print(string1)
paper_doll('Mississippi')

#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21,
# return their sum. If their sum exceeds 21 and there's an eleven,
# reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def black_jack(a,b,c):
    sum1 = a+b+c
    if sum1 <= 21:
        return sum1
    elif 11 in (a,b,c):
        sum2 = sum1 - 10
        return sum2
    else:
        return 'BUST'
value = black_jack(9,9,11)
print("black_jack",value)

# SUMMER OF '69: Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and extending to the next 9
# (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_of_69(array1):
    for r in array1:
        summ =0
    return summ

array1 = [1,2,3,4,5,6]
value=summer_of_69(array1)
print(value)