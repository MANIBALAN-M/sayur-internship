import sys
pwd = input('enter your password : ')
if len(pwd) < 5 :
    print('your password must be contain atleast 5 character')
    sys.exit()
if pwd.isalpha() :
    print('your password is weak , your password only contain alphabet characters')
    sys.exit()
if pwd.isdigit() :
    print('your password is weak , your password only contain numerical characters')
    sys.exit()
if pwd.isalnum == False :
    print('your password is weak , your password only contain special characters')
    sys.exit()
if not any(pwd.isalpha() for pwd in pwd) :
    print('your password is weak , your password not contain alphabet characters')
    sys.exit()
if not any(pwd.isdigit() for pwd in pwd) :
    print('your password is weak , your password not contain numerical characters')
    sys.exit()
if not any(pwd.isalnum() == False for pwd in pwd) :
    print('your password is weak , your password not contain special characters')
    sys.exit()

for i in pwd :
    if i.isalpha() :
        print(pwd.count(i))
for j in pwd :
    if j.isnumeric() :
        pwd.count(j)
for k in pwd :
    if k.isalnum() == False :
        pwd.count(k)
