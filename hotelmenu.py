import sys
from datetime import datetime 

bill = 0

drinksmenu = {
    '(1).coffee':20,
    '(2).tea':20,
    '(3).lemon juice':20,
    '(4).apple juice':45,
    '(5).oraange juice':40
}
snacksmenu = {
    '(1).samosa':10,
    '(2).paff':20,
    '(3).plain cake':20
}
snackserial = {
    1:'(1).samosa',
    2:'(2).paff',
    3:'(3).plain cake'
}
drinkserial = {
    1:'(1).coffee',
    2:'(2).tea',
    3:'(3).lemon juice',
    4:'(4).apple juice',
    5:'(5).oraange juice'
}
breakfastmenu = {
    '(1).idly':10,
    '(2).dosa':30,
    '(3).poori':30,
    '(4).pongal':30,
    '(5).special dosa':40
}
breakfastserial = {
    1:'(1).idly',
    2:'(2).dosa',
    3:'(3).poori',
    4:'(4).pongal',
    5:'(5).special dosa'
}
lunchmenu = {
    '(1).meals':80,
    '(2).biryani':100,
    '(3).veriety rice':30,
    '(4).chickenfried rice':100,
    '(5).eggfried rice':80
}
lunchserial = {
    1:'(1).meals',
    2:'(2).biryani',
    3:'(3).veriety rice',
    4:'(4).chickenfried rice',
    5:'(5).eggfried rice'
}


def order(menu,serials,bill):
    print(serials)
    for item in menu:
        print(item,'=',menu.get(item))
    #try:
    orderinput = input('enter your order serial number:')
    if orderinput in serials:
        for serial in serials:
            if orderinput==(serial):
                item = serial.get(serials)
                print(item)
                    #bill += menu.get(item)  
    else:
        print('your order not in the list')    
    #except:
     #   print('invalid input') 
    #return bill


action = int(input('enter action:'))
#try:
if action==1:
    bill = order(drinksmenu,drinkserial,bill)
    print('drink bill = ',bill)
elif action==2:
    bill = order(breakfastmenu,breakfastserial,bill)
    print('breakfast bill = ',bill)
elif action==3:
    bill = order(lunchmenu,lunchserial,bill)
    print('lunch bill = ',bill)    
elif action==4:
    bill = order(snacksmenu,snackserial,bill)
    print('lunch bill = ',bill)
else:
    print('invalid order action')    
#except:
 #   print('invalid order input')
