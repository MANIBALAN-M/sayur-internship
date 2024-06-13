'''
check the given number is amstrong
'''
import sys

num = input('enter the number to check amstrong: ')
if num.isdigit()!=1:
    print('enter only numerical values')
    sys.exit()
sum = 0
for i in range (len(num)):
    a = num[i]
    a = int(a)
    sum+=a**len(num)
print(sum)
sum = str(sum)
if num == sum:
    print('amstrong')
else:
    print('not amstrong')
    
