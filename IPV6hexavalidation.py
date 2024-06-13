'''
IPV6 ADDRESS VALIDATION , BY READ DATA FROM ANOTHER FILE AND CONVERT HEXA DECIMAL TO DECIMAL

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
    for ch in ipv6:
        if ch==':':
            count = count+1
    if count != 7:
        print('your IP address is invalid , please enter with 7 colon')
        return
    splitted_ipv6 = ipv6.split(':')
    for eachsplit in splitted_ipv6:
        try:
            eachsplit = int(eachsplit,16)
            if eachsplit > 65535:
                print('invalid IP address')
                return
        except:
            print('invalid IP address')
            return

    print('your IP address is valid')

def action3(gipv6):
    try:
        fipv6 = open(gipv6+'.txt','r')
        print(fipv6)
        listipv6 = (fipv6.read())
        splitipv6 = listipv6.split(',')
        for ipv6 in splitipv6:
            ipv6 = ipv6.strip()
            print(ipv6)
            validator(ipv6)
    except:
        print('your file does not exist')

action1 = input('do you want to validate your IP address (1) yes / (2) no , enter (1/2): ')
if action1.isnumeric()==1:
    if action1=='1':
        action2 = input('do you want to validate (1) IPV4 address / (2) IPV6 address / (3) IPV6 address in file , enter (1/2/3): ')
        if action2=='2':
            ipv6 = input('enter the IPV6 address: ')
            validator(ipv6)
        elif action2=='3':
            gipv6 = input('enter the IPV6 address data file,Your file must text format ,No need to write extension:')#IPV6datafile
            action3(gipv6)         
        else:
            print('sorry this is a IPV6 address validater,thank you for coming')
    else:
        print('thank you for coming')
else:
    print('invalid input')  