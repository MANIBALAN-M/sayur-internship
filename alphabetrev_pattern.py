'''

Generate the following output using for loop. Go until g.
a
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba

1
121
1213121
121312141213121

'''

import sys

limit = input('enter th limit: ' )
if limit.isdigit() != 1:
    print('please enter numerical characters')
    sys.exit()
limit = int(limit)
num1 = 97
num2 = 97
print(chr(num1))
for i in range (limit-1) :
    num2 = num2+1
    if isinstance(num1,int)==1:
        num3= str(chr(num1))
    if isinstance(num1,str)==1:
        num3= str(num1)
    sum= num3+str(chr(num2))+num3
    print(sum)
    num1 = sum
    num2= int(num2)



