'''
IPV6 ADDRESS VALIDATION , BY READ DATA FROM ANOTHER FILE

algorithm:
1.check if there is have 7 colon
2.split each colon
3.check it is less then 5 in each splitted elements
4.check the elements are only contain hexadecimal values

'''

import sys

def validator(ipv6):
    #ipv6 = input('enter the IPV6 address: ')#'1234:5678:90AB:CDEF:0000:9876:ABCD:102'
    
    count = 0
    for colon in ipv6:
        if colon==':':
            count = count+1
    if count != 7:
        print('your IP address is invalid , please enter with 7 colon')
        return
    splitted_ipv6 = ipv6.split(':')
    for split in splitted_ipv6:
        if len(split)>4:
            print('invalid IP address')
            return
        for check in split:
            if check.isalpha():
                check = check.upper()
            if check.isnumeric()!= 1 and check!='A' and check!='B' and check!='C' and check!='D' and check!='E' and check!='F':
                print('invalid IP address')
                return
    print('your IP address is valid')

action1 = input('do you want to validate your IP address (1) yes / (2) no , enter (1/2): ')
if action1.isnumeric()==1:
    if action1=='1':
        action2 = input('do you want to validate (1) IPV4 address / (2) IPV6 address / (3) IPV6 address in file , enter (1/2/3): ')
        if action2=='2':
            ipv6 = input('enter the IPV6 address: ')
            validator(ipv6)
        elif action2=='3':
            fipv6 = open('IPV6datafile.txt','r')
            listipv6 = (fipv6.read())
            splitipv6 = listipv6.split(',')
            for ipv6 in splitipv6:
                    ipv6 = ipv6.strip()
                    print(ipv6)
                    validator(ipv6)
        else:
            print('sorry this is a IPV6 address validater,thank you for coming')
    else:
        print('thank you for coming')
else:
    print('invalid input')  

