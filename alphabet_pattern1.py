'''
print alphabet using * pattern
'''

'''
AaaaaaaaaA
AaaaaaaaaA
AaaaaaaaaA
AaaaaaaaaA
AaaaaaaaaA


row = 5
column =10
for i in range(row):
    for j in range(column):
        if (i==0 and j==0 or i==0 and j==9 or i==1 and j==0 or i==1 and j==9 or i==2 and j==0 or i==2 and j==9 or i==3 and j==0 or i==3 and j==9 or i==4 and j==0 or i==4 and j==9):
            print('A',end='')
        else:    
            print('a',end='')
    print('') 

print(' ')
row = 5
column =10
for i in range(row):
    print('A',end='')
    for j in range(column):
            print('a',end='')    
    print('A') 

print(' ')
row = 5
column =10
for i in range(row):
    for j in range(column):
        if ( j==0 or  j==column-1 ):
            print('A',end='')
        else:    
            print('a',end='')
    print('') 

print(' ') 
row = 5
column =10
for i in range(row):
    for j in range(column):
        if (i==0 and j==0 or i==0 and j==9 or i==4 and j==0 or i==4 and j==9):
            print('A',end='')
        else:
            print(' ',end='')
    print('') 

'''    
def print_a():
    print(' ')
    row = 7
    column = 7
    for i in range(row):
        for j in range(column):
            if (i==0 and j==3) or (i==1 and j==2) or (i==1 and j==4) or (i==2 and j==1) or (i==2 and j==5) or (i==3 and j==3) or (i==3 and j==2) or (i==3 and j==4) or (i==3 and j==0) or (i==3 and j==6) or (i==4 and j==0) or (i==4 and j==6) or (i==5 and j==0) or (i==5 and j==6):
            #if i==j:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('')    

def print_b():
    print(' ')
    row = 7
    column = 7
    for i in range(row):
        for j in range(column):
            if (j==0) or (i==0 and j==1) or(i==0 and j==2) or (i==1 and j==3) or (i==2 and j==3) or (i==3 and j==1) or(i==3 and j==2) or (i==6 and j==1) or(i==6 and j==2) or (i==4 and j==3) or (i==5 and j==3):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('')            


def print_c():        
    print(' ')
    row = 7
    column = 7
    for i in range(row):
        for j in range(column):
            if (i==0 and j==1) or (i==0 and j==2) or (i==1 and j==0) or (i==1 and j==3) or (i==2 and j==0) or (i==4 and j==0) or (i==3 and j==0) or (i==5 and j==0) or (i==5 and j==3) or (i==6 and j==1) or (i==6 and j==2):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('')
    

def print_d():        
    print(' ')
    row = 7
    column = 7
    for i in range(row):
        for j in range(column):
            if (j==0) or (i==0 and j==1) or (i==0 and j==2) or (i==1 and j==3) or (i==5 and j==3) or (i==6 and j==1) or (i==6 and j==2) or (i==2 and j==3) or (i==3 and j==3) or (i==4 and j==3):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('')


def print_e():        
    print(' ')
    row = 7
    column = 7
    for i in range(row):
        for j in range(column):
            if (j==0) or (i==0 and j==1) or (i==0 and j==2) or (i==0 and j==3) or (i==3 and j==3) or (i==3 and j==1) or (i==3 and j==2) or (i==6 and j==3) or (i==6 and j==2) or (i==6 and j==1):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('')


def print_f():        
    print(' ')
    row = 7
    column = 7
    for i in range(row):
        for j in range(column):
            if (j==0) or (i==0 and j==1) or (i==0 and j==2) or (i==0 and j==3) or (i==3 and j==3) or (i==3 and j==1) or (i==3 and j==2):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('')


def print_g():        
    print(' ')
    row = 7
    column = 7
    for i in range(row):
        for j in range(column):
            if (j==0) or (i==0 and j==1) or (i==0 and j==2) or (i==0 and j==3) or (i==3 and j==3) or (i==3 and j==2) or (i==3 and j==4) or (i==3 and j==5) or (i==6 and j==3) or (i==6 and j==2) or (i==6 and j==1) or (j==3 and (i==4 or i==5)) or (j==5 and (i==3 or i==4 or i==5 or i==6)):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('')


def print_h():        
    print(' ')
    row = 7
    column = 7
    for i in range(row):
        for j in range(column):
            if (j==0) or (j==4) or (i==3 and (j==1 or j==2 or j==3)):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('')


def print_i():        
    print(' ')
    row = 7
    column = 5
    for i in range(row):
        for j in range(column):
            if (i==0) or (i==6) or (j==2 and (i==1 or i==2 or i==3 or i==4  or i==5)):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('')


def print_j():        
    print(' ')
    row = 7
    column = 5
    for i in range(row):
        for j in range(column):
            if (i==0) or (i==6 and (j==1 )) or (j==2 and (i==1 or i==2 or i==3 or i==4)) or (i==5 and (j==0 or j==2)):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('')


def print_k():        
    print(' ')
    row = 7
    column = 5
    for i in range(row):
        for j in range(column):
            if (j==0) or (i==3 and j==1) or (j==2 and (i==2 or i==4)) or (j==3 and (i==1 or i==5)) or (j==4 and (i==0 or i==6)):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('')


def print_l():        
    print(' ')
    row = 7
    column = 5
    for i in range(row):
        for j in range(column):
            if (j==0) or (i==6):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('')


def print_m():        
    print(' ')
    row = 7
    column = 7
    for i in range(row):
        for j in range(column):
            if (j==0) or (j==6) or (i==3 and j==3) or (i==2 and (j==2 or j==4)) or (i==1 and (j==1 or j==5)):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('')

 

def print_n():        
    print(' ')
    row = 7
    column = 7
    for i in range(row):
        for j in range(column):
            if (j==0) or (j==6) or (i==j):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('')


def print_o():        
    print(' ')
    row = 7
    column = 7
    for i in range(row):
        for j in range(column):
            if (j==0 and (i==1 or i==2 or i==3 or i==4 or i==5)) or (j==4 and (i==1 or i==2 or i==3 or i==4 or i==5)) or (i==0 and (j==2 or j==3 or j==1)) or (i==6 and (j==2 or j==3 or j==1)):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('')


def print_p():
    print(' ')
    row = 7
    column = 7
    for i in range(row):
        for j in range(column):
            if (j==0) or (i==0 and j==1) or(i==0 and j==2) or (i==1 and j==3) or (i==2 and j==3) or (i==3 and j==1) or(i==3 and j==2):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('') 


def print_q():
    print(' ')
    row = 7
    column = 7
    for i in range(row):
        for j in range(column):
            if (j==0 and (i==1 or i==2 or i==3 or i==4 or i==5)) or (j==4 and (i==1 or i==2 or i==3 or i==4 or i==5)) or (i==0 and (j==1 or j==2 or j==3)) or (i==6 and (j==1 or j==2 or j==3)) or (i==3 and j==2) or (i==4 and j==3) or (i==5 and j==4) or (i==6 and j==5):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('')

def print_r():
    print(' ')
    row = 7
    column = 7
    for i in range(row):
        for j in range(column):
            if (j==0) or (i==0 and j==1) or(i==0 and j==2) or (i==1 and j==3) or (i==2 and j==3) or (i==3 and j==1) or(i==3 and j==2) or (i==4 and j==3) or (i==5 and j==3) or (i==6 and j==3):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('') 


def print_s():
    print(' ')
    row = 7
    column = 7
    for i in range(row):
        for j in range(column):
            if (j==0 and (i==1 or i==2)) or (j==3 and (i==4 or i==5)) or (i==0 and (j==1 or j==2)) or (i==6 and (j==1 or j==2)) or (i==3 and (j==1 or j==2)) or (i==1 and j==3) or (i==5 and j==0):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('')


def print_t():
    print(' ')
    row = 7
    column = 7
    for i in range(row):
        for j in range(column):
            if (i==0) or (j==3 and (i==1 or i==2 or i==3 or i==4 or i==5 or i==6)) :
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('')

def print_u():
    print(' ')
    row = 7
    column = 5
    for i in range(row):
        for j in range(column):
            if (j==0 and (i==1 or i==2 or i==3 or i==4 or i==5)) or (j==4 and (i==1 or i==2 or i==3 or i==4 or i==5)) or (i==6 and (j==1 or j==2 or j==3)):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('')


def print_v():
    print(' ')
    row = 5
    column = 10
    for i in range(row):
        for j in range(column):
            if (i==j) or (i==0 and j==8) or (i==1 and j==7) or (i==2 and j==6) or (i==3 and j==5):
                print('*',end='')
            else:
                print(' ',end=' ')
        print('')


def print_w():
    print(' ')
    row = 5
    column = 15
    for i in range(row):
        for j in range(column):
            if (i==j) or (i==4 and j==8) or (i==3 and j==7) or (i==2 and j==6) or (i==3 and j==5) or (i==3 and j==9) or (i==2 and j==10) or (i==1 and j==11) or (i==0 and j==12):
                print('*',end='')
            else:
                print(' ',end='')
        print('')

def print_x():
    print(' ')
    row = 7
    column = 7
    for i in range(row):
        for j in range(column):
            if (i==j) or (i==0 and j==6) or (i==1 and j==5) or (i==2 and j==4) or (i==4 and j==2) or (i==5 and j==1) or (i==6 and j==0):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('')

def print_y():
    print(' ')
    row = 7
    column = 7
    for i in range(row):
        for j in range(column):
            if (i==0 and (j==0 or j==6)) or (i==1 and (j==1 or j==5)) or (i==2 and (j==2 or j==4)) or (i==3 and j==3) or (i==4 and j==3) or (i==5 and j==3) or (i==6 and j==3):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('')

def print_z():
    print(' ')
    row = 7
    column = 7
    for i in range(row):
        for j in range(column):
            if (i==0) or (i==1 and j==5) or (i==2 and j==4) or (i==3 and j==3) or (i==4 and j==2) or (i==5 and j==1) or (i==6):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('')


alphabet = input('enter the alphabet:' )
if alphabet == 'a':
    print(print_a())
if alphabet == 'b':
    print(print_b())    
if alphabet == 'c':
    print(print_c())    
if alphabet == 'd':
    print(print_d())    
if alphabet == 'e':
    print(print_e())    
if alphabet == 'f':
    print(print_f())    
if alphabet == 'g':
    print(print_g())    
if alphabet == 'h':
    print(print_h())    
if alphabet == 'i':
    print(print_i())    
if alphabet == 'j':
    print(print_j())    
if alphabet == 'k':
    print(print_k())    
if alphabet == 'l':
    print(print_l())    
if alphabet == 'm':
    print(print_m())    
if alphabet == 'n':
    print(print_n())    
if alphabet == 'o':
    print(print_o())    
if alphabet == 'p':
    print(print_p())    
if alphabet == 'q':
    print(print_q())    
if alphabet == 'r':
    print(print_r())    
if alphabet == 's':
    print(print_s())    
if alphabet == 't':
    print(print_t())   
if alphabet == 'u':
    print(print_u())    
if alphabet == 'v':
    print(print_v())    
if alphabet == 'w':
    print(print_w())    
if alphabet == 'x':
    print(print_x())    
if alphabet == 'y':
    print(print_y())    
if alphabet == 'z':
    print(print_z())    

