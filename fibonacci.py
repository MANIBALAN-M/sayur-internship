'''
0 1 1 2 3 . . .
num1 num2 sum
0    1    1
1    1    2
1    2    3
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


   

