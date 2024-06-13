import sys
print('hello user')
email = input('enter your email id :')
if '.' not in email or '@' not in email :
    print("your email must be contain '.' and '@'")
    sys.exit()
if ' ' in email :
    print("your email must not be contain any space")
    sys.exit()
if email.count('@') > 1 :
    print("your email must be contain only one '@'")
    sys.exit()
split_email = email.split('@')
if split_email[1] == 0 :
    print("your email must contain domain name")
    sys.exit()
split_email[0] = split_email[0].replace('.','')
split_email[0] = split_email[0].replace('_','')
if split_email[0].isalnum()==False :
    print('your username must be contain only numericalphabets ')
    sys.exit()
if '.' not in split_email[1] :
    print("your domain must be contain '.'")
    sys.exit()
split_domain = split_email[1].split('.')
if len(split_domain[0]) < 3:
    print("invalid input, your domain name must contain a minimum of 3 characters")
    sys.exit()
if len(split_domain[1]) < 2:
    print("invalid input, your domain name after '.' must contain a minimum of 2 characters")
    sys.exit()
print("your email id is", email)
phone = input('enter your phone number :')
if phone.isdigit()==False :
    print("invalid input , your phone number must be contain only numerical character")
    sys.exit()
if len(phone)!= 10 :
    print("your phone number must be contain 10 numbers")
    sys.exit()
ph = phone.strip()
if ph[0]== '0' :
    print("your must not be starts with '0'")
    sys.exit()
if phone.count('0') >= 5 or phone.count('1') >= 5 or phone.count('2') >= 5 or phone.count('3') >= 5 or phone.count('4') >= 5 or phone.count('5') >= 5 or phone.count('6') >= 5 or phone.count('7') >= 5 or phone.count('8') >= 5 or phone.count('9') >= 5 :
    print("enter valid mobile number")
    sys.exit()
print('your phone number is',phone)