'''
Problem #5
Same as above, but the operator come first.
eg - input ["+","1", "2", "*", "5"]
output =  15
explanation (1 + 2) * 5 = 15
input ["-","10", "+", "2", "3", "*", "5"]
output =  25
explanation (10 - ( 2 + 3)) * 5 = 25
'''

list1 = ['+','1','2','*','5']
count = 0
empty = []
val4 = 0
for li in list1:
    empty.append(li)
    print(li)
    if li.isdigit():
        count += 1
        print('count',count)
        if count == 2:
            val1 = empty.pop()
            val2 = empty.pop()
            
            if li == '+':
                val4 = int(val2) + int(val1)
            elif li == '-':
                val4 = int(val2) + int(val1)
            elif li == '*':
                val4 = int(val2) + int(val1)
            elif li == '/':
                val4 = int(val2) + int(val1)
            else:
                print('invalid input')
        empty.append(val4)
        
print(f'answer = {val4}')

