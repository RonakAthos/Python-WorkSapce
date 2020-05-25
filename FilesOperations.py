myFiles = open("D:\\PYTHON\\PythonWorkSpace\\TestFilesPython\\Test.txt")
print(myFiles)
print(myFiles.read())
print('hello')
print('--------------------------------')
myFiles.seek(0)
print( myFiles.readlines())
myList = [myFiles]
print(myList)
print('--------------------------------')
myFiles.seek(0)
# with out using close method

#To read file with different name

with open('Test.txt') as myNew_File:
    contain = myNew_File.read()
print(contain)

#write file


myFiles.close()

d = {'k1':[{'nest_key' : ['this is deep', ['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])
d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

if 2>3:
    print('T')
else:
    print('F')

if 3<=2:
    print('T')
else:
    print('F')
if 3==3.0:
    print('T')
else:
    print('F')
if 4**2.0!=2:
    print(4**2.0 )
    print('T')
else:
    print('F')