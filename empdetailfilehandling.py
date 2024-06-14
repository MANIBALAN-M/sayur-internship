class Empinformation():
    def __init__(self,Id,Name,Email,Phno):
        self.Id = Id
        self.Name = Name
        self.Email = Email
        self.Phno = Phno
        self.printer(Id,Name,Email,Phno)
        
    def printer(self,Id,Name,Email,Phno):
        with open('empdetailfile.txt','w') as detailfile:
            detailfile.write(f'Employee Id           :{Id}\n')
            detailfile.write(f'Employee Name         :{Name}\n')
            detailfile.write(f'Employee Email        :{Email}\n')
            detailfile.write(f'Employee Phone number :{Phno}\n')
    

def validator(Email):
    if '.' not in Email or '@' not in Email :
        print("your email must be contain '.' and '@'")
        return
    if ' ' in Email :
        print("your email must not be contain any space")
        return
    if Email.count('@') > 1 :
        print("your email must be contain only one '@'")
        return
    split_email = Email.split('@')
    if split_email == 0 :
        print("your email must contain domain name")
        return
    if split_email[0].isalnum==False :
        print('your username must be contain only numericalphabets ')
        return
    if '.' not in split_email[1] :
        print("your domain must be contain '.'")
        return
    split_domain = split_email[1].split('.')
    if len(split_domain[0]) < 3:
        print("invalid input, your domain name must contain a minimum of 3 characters")
        return
    if len(split_domain[1]) < 2:
        print("invalid input, your domain name after '.' must contain a minimum of 2 characters")
        return        

def phvalidator(phone):
    if phone.isdigit()==False :
        print("invalid input , your phone number must be contain only numerical character")
        return
    if len(phone)!= 10 :
        print("your phone number must be contain 10 numbers")
        return
    ph = phone.strip()
    if ph[0]== '0' :
        print("your must not be starts with '0'")
        return
    if phone.count('0') >= 5 or phone.count('1') >= 5 or phone.count('2') >= 5 or phone.count('3') >= 5 or phone.count('4') >= 5 or phone.count('5') >= 5 or phone.count('6') >= 5 or phone.count('7') >= 5 or phone.count('8') >= 5 or phone.count('9') >= 5 :
        print("enter valid mobile number")
        return


actions = int(input("Enter how many employee deteils you want to enter :"))
for action in range(actions):
    Id = int(input('Emter epmloyee Id           :'))
    Name = input('Emter epmloyee Name         :')
    Email = input('Emter epmloyee Email        :')
    validator(Email)
    Phno = input('Emter epmloyee Phone number :')
    phvalidator(Phno)
    Employee = Empinformation(Id,Name,Email,Phno)
    
