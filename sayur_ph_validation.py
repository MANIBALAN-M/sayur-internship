import sys
print('hello user')
phone_no = input('enter your phone number : ')
phone_no = phone_no.replace('+','')
if phone_no.isdigit() == False :
    print("your phone number must be numerical characters")
    sys.exit()
if phone_no.startswith('91')  and (len(phone_no) != 12 or len(phone_no) != 10) :
    print("enter valid input if it contain country code your phone number must be 12 charactes or not have country code it must be 10 characters")
    sys.exit()
if len(phone_no) != 10 :
    print("enter valid input your phone number must be 10 characters")
    sys.exit()
if phone_no.startswith('0') :
    print("your phone must not be start's with '0' ")
    sys.exit()

