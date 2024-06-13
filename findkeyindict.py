col_of_fruits = {
    'apple':10,
    'orange':12,
    'banana':15,
    'grapes':13
}

cos_list = {}

count = 0
while count == 0:
    wanted_fruit = input('what fruit you want: ')
    if wanted_fruit.isalpha() != 1:
        print('please enter only alphabetic inputs')
    else:    
        wanted_fruit = wanted_fruit.lower()
        if wanted_fruit in col_of_fruits:
            if wanted_fruit in cos_list:
                cos_list[wanted_fruit] += 1
            else:
                cos_list[wanted_fruit] = 1
        else:
            print('your fruit not available in the cart')              
    action = input('you want more fruits ,enter (yes/no): ')
    if action=='yes' :
        count = 0
    elif action== 'no':
        count = 1
    else:
        print('please enter input')
        continue


print(cos_list)

