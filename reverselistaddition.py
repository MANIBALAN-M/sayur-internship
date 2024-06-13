'''
Problem #3 
Add two number represented in a list as reversed. print the sum also as a list in reverse order
eg input list1 = [1,2,3] list2 = [5,6,7]
answer= [6,8,0,1]
explanation (321 + 765 = 1086)

ALGORITHM:
1.reverse the list by reverse() method
2.convert the list into digits
3.add the digits
4.convert added digits into list
'''

def reverseadd(newlist):    
    p = 0
    sum = 0
    for l in newlist:
        p += 1
        i = 10**(len(newlist) - p)
        sum += l * i
    return sum

def list3convert(list3): 
    reverselist3 = []       
    for i in range (len(list3)):
        list3 = int(list3)
        value = list3 % 10
        reverselist3.append(value)
        list3 = list3 / 10
    return reverselist3

'''list1loop = int(input('how many numbers you want to enter in list: '))
list1 = []
for listloop in range (list1loop):
    value = int(input(f'enter list 1 value of {listloop + 1}:'))
    list1.append(value)

list2loop = int(input('how many numbers you want to enter in list: '))
list2 = []
for listloop in range (list2loop):
    value = int(input(f'enter list 1 value of {listloop + 1}:'))
    list2.append(value)
'''
list1 = [1,2,3]
list2 = [5,6,7]
print(f'list 1 = {list1}')
print(f'list 2 = {list2}')

list1.reverse()#reverselist1 = converter(list1)
a = reverseadd(list1)

list2.reverse()
b = reverseadd(list2)

list3 = a + b
list3 = str(list3)

answer = list3convert(list3)
print(f'answer = {answer}')
    