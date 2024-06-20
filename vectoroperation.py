class vectoroperator():
    def __init__(self,val1,val2,val3,val4,action):
        self.val1 = val1
        self.val2 = val2
        self.val3 = val3
        self.val4 = val4
        self.action = action
        
    def multiplyer(self):
        num = (self.val1*self.val3) - (self.val2*self.val4)
        comp = (self.val1*self.val4) + (self.val2*self.val3)
        num = str(num)
        comp = str(comp)
        print(f'answer = {num} + {comp}i')
    def divisor(self):
        num = ((self.val1*self.val3) + (self.val2*self.val4))/(self.val3*self.val3 + self.val4*self.val4)
        comp = ((self.val1*self.val4) + (self.val2*self.val3))/(self.val3*self.val3 + self.val4*self.val4)
        num = str(num)
        comp = str(comp)
        print(f'answer = {num} + {comp}i')

    def performer(self):
        if self.action == '1':
            self.multiplyer()
        if self.action == '2':
            self.divisor()
    

action = input('what vector you want to do (1) multiplier / (2) divisor / (3) exit:')

if action == '1':
    def vectmultiplier():    
        print('Enter two vectors')
        vect1 = input('Enter vector 1:')
        vect1 = vect1.strip()
        if vect1[-1] == 'i':
            vect1 = vect1.replace('i','')
            vect1 = vect1.split('+')
            val1 = vect1[0]
            val2 = vect1[1]
            val1 = int(val1)
            val2 = int(val2)
        else:
            print('invalid vector')
            return
        vect2 = input('Enter vector 2:')    
        if vect2[-1] == 'i':
            vect2 = vect2.replace('i','')
            vect2 = vect2.split('+')
            val3 = vect2[0]
            val4 = vect2[1]
            val3 = int(val3)
            val4 = int(val4)
        else:
            print('invalid vector')
            return
        operation = vectoroperator(val1,val2,val3,val4,action)
        operation.performer()
    vectmultiplier()

elif action == '2':
    def vectdiviser():    
        print('Enter two vectors')
        vect1 = input('Enter vector 1:')
        vect1 = vect1.strip()
        if vect1[-1] == 'i':
            vect1 = vect1.replace('i','')
            vect1 = vect1.split('+')
            val1 = vect1[0]
            val2 = vect1[1]
            val1 = int(val1)
            val2 = int(val2)
        else:
            print('invalid vector')
            return
        vect2 = input('Enter vector 2:')    
        if vect2[-1] == 'i':
            vect2 = vect2.replace('i','')
            vect2 = vect2.split('+')
            val3 = vect2[0]
            val4 = vect2[1]
            val3 = int(val3)
            val4 = int(val4)
        else:
            print('invalid vector')
            return
        operation = vectoroperator(val1,val2,val3,val4,action)
        operation.performer()
    vectdiviser()
elif action == '3':
    print('thank you for coming')
else:
    print('invalid input')
