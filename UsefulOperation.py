from random import shuffle
from random import random
# rangem

for iteam in range(1,20,2):
    print(iteam)
myList = list(range(50))
print(myList)
print(list(range(1,20,2)))

# enumerate
index_no = 0
for iteam in 'abcd':
    print("the index {} and it's value is {}".format(index_no,iteam))
    index_no += 1

# enumerate and unpackageing
word = "MacbookPro is one of the best laptop"
for index,value in enumerate(word):
    print(index,'\t',value)

# Zip
myList1 = [1,2,3,4]
myList2 = ['a', 'b','c']
myList2.append('d')
for i in zip(myList2,myList1):
    print(i)

if len(myList1) == len(myList2):
    zip(myList1,myList2)
    print("zip success")
else:
    print("the list size is not equal")

# shuffle
shuffle(myList1)
print(myList1)

x=random()
print(x)

#Comprehensions
string1= 'world'
list1=[]
for iteam in string1:
    list1.append(iteam)
print(list1)
list2=[iteam**2 for iteam in range(1,21)]
print(list2)

temprature = [0,23,30,25.3]
tempInFarni = [((9/5)*temp+32) for temp in temprature]
print(tempInFarni)


myList = []
for x in [1,2,3]:
    for y in [1,10,100]:
        myList.append(x*y)
print(myList)

myListComp = [x*y for x in [1,2,3] for y in [1,10,100]]
print(myListComp)