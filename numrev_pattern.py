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
num1 = 1
num2 = 1
print(num1)
for i in range (limit-1) :
   num2 = num2+1
   num1 = str(num1)
   num2 = str(num2)
   sum = num1+num2+num1
   print(sum)
   num1 = sum
   num2 = int(num2)
