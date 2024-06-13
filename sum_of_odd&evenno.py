'''
get the input us a number from the user, check sum of odd numbers & sum of even numbers 
'''

import sys

num = int(input('enter the number: '))
odd_count = 0 
even_count = 0
sum_of_odd = 0
sum_of_even = 0
while num > 0:
    rem = num % 10
    num = num//10
    if rem % 2 == 1:
        odd_count = odd_count+1
        sum_of_odd = sum_of_odd + rem
    if rem % 2 == 0:
        even_count = even_count+1
        sum_of_even = sum_of_even + rem

print('odd count:',odd_count)
print('even count:',even_count)
print('sum of odd: ',sum_of_odd)
print('sum of even: ',sum_of_even)
    

