class Empinformation:
    def __init__(self,EmpId,Empname,Empemail,Phno):
        self.EmpId = EmpId
        self.Empname = Empname
        self.Empemail = Empemail
        self.Phno = Phno
        
        def printer(self):
            print(f'Employee Id       :{EmpId}')
            print(f'Employee Name     :{Empname}')
            print(f'Employee Email    :{Empemail}')
            print(f'Employee Phone no :{Phno}')

        printer(self)

def Empdeteil(Id,Name,Email,Phno):
    employ = Empinformation(Id,Name,Email,Phno)

actions = int(input('how many data you want to enter:'))

for action in range(actions):
    Id = int(input('Enter the ID           :'))
    Name = input('Enter the Name         :')
    Email = input('Enter the Email        :')
    Phno = input('Enter the Phone number :')
    Empdeteil(Id,Name,Email,Phno)
