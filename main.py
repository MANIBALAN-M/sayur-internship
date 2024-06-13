import sys
print('hello')
name=input('enter name :')
print(name)
age=input('enter age :')
if age.isdigit()==False :
    print('invalid input')
    sys.exit()
age = int(age)
if age<0 or age>100 :
    print('invalid input')
    sys.exit()
else:
    print('your age is',age)
email=input('enter email :')
if '.' not in email or '@' not in email:
    print("your email muust be contain '.' and '&'")
    sys.exit()
print (email.count('&'))