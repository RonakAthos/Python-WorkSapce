string1 = "January is the first month of the every year"
myList = string1.split()
for iteam in myList:
    temp = iteam
    for chars in temp:
        if chars == 'f':
            print(temp)
        else:
            break
###############
# myList1 = []
# for mylistdata in range(0,50):
#     myList1.append(mylistdata)
# print(myList1)
###### List comprehension
myList2 = [data1 for data1 in range(1,50) if data1%3 == 0]
print(myList2)
########## word even or not
for data2 in myList:
    temp1 = data2
    if len(temp1)%2 ==0:
        print(temp1,": even")
    else:
        print(temp1,": odd")
#########
myList3 = [data3 for data3 in range(1,100)]
for number in myList3:
    if number%5 ==0 and number%3 ==0:
        print(number," : FizzBuzz")
    elif number%5 ==0:
        print(number," : bazz")
    elif number%3 ==0:
        print(number," : Fizz")
#####
string2 = "create a list of the first letters of evey word in this string"
myList4 = string2.split()
myList5 = [ia for data5 in myList4 for ia in enumerate(data5)]
print(myList5)