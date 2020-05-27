import sys
my_list = [1,2,3]
for iteam in my_list:
    print(iteam)
print('---------------')
myList = [1,2,3,4,5,6]
for number in myList:
    if number % 2 == 0:
        print(number)
    else:
        print(f"odd number:",{number})
print('---------------')
myList1 = [(1,2,21),(3,4,22),(5,6,23),(7,8,24),(9,10,25),(11,12,26)]
for a,b,c in myList1:
    print(a)
    print(b)
    print(c)
    print(a,b,c)
print(sys.maxsize)

myDic = {'k1':1, 'k2':2, 'k3':3}
for key,val in myDic.items():
    print(key,':',val)


