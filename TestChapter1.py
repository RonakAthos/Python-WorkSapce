#Print only  the word start with s in the string
text1="Print only  the word start with s in the string"
list1 = text1.split()
# print(len(list1))
for words in list1:
    temp = words
    for char in temp:
        temp2= char
        if temp2 in "s":
            print(temp)
        else:
             break
#Print even number in range 0,10
list2 = []
for x in range(0,11):
     list2.append(x)
for y in list2:
    if y%2==0:
        print(y)
#
