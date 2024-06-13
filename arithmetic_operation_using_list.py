'''
Problem #4
Input is an array of strings of an arithmetic expression. Calculate the value.
eg - input ["1", "2", "+", "5", "*"]
output =  15
explanation (1 + 2) * 5 = 15

input ["10", "2", "3", "+","-", "5", "*"]
output =  25
explanation (10 - ( 2 + 3)) * 5 = 25
Hint : Use the concept of stack. Push and pop. 
Parse the input list one element at a time. Convert to integer, push it to a stack. Whenever you see an
operator, pop two elements from the stack, apply the operation and push the result back.

ALGORITHM:
1.check the place of the arithmetic and pop it 
2.convert two poped value into one and push it
3.repeat untill it finish
'''

def arithmeticexp(expression):
    newexpression = []
    val3 = 0
    for exp in expression:
        if exp.isdigit() == 1:
                newexpression.append(exp)
        else:
            val1 = newexpression.pop()
            val2 = newexpression.pop()
            if exp == '+':
                val3 = int(val2) + int(val1)
            elif exp == '-':
                val3 = int(val2) - int(val1)
            elif exp == '*':
                val3 = int(val2) * int(val1)
            elif exp == '/':
                val3 = int(val2) / int(val1)
            else:
                print('please enter valid data')
                return
            newexpression.append(val3)
    return val3

exploop = int(input('how many characters you want to enter in list: '))
expression = ['1','2','+','5','*']#[]
for loop in range (exploop):
    value = input(f'enter list 1 value of {loop + 1}:')
    expression.append(value)
try:
    val3 = arithmeticexp(expression)
    print(f'the value of the expression is {val3}')
except:
    print('please enter valid input')
    



