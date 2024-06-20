'''
connection between employeee ,manager ,general manager and CEO of a company
'''

empdetail = [{
    'Id' : 6,
    'name' : 'ganesh',
    'position' : 'employee',
    'salary' : 10000,
    'email' : 'ganesh@gmail.com',
    'phno' : '9025808139'
    },{
    'Id' : 5,
    'name' : 'siva',
    'position' : 'employee',
    'salary' : 10000,
    'email' : 'siva@gmail.com',
    'phno' : '9025807639'
    },{
    'Id' : 4,
    'name' : 'siva',
    'position' : 'manager',
    'salary' : 20000,
    'email' : 'siva@gmail.com',
    'phno' : '9025807639'
    },{
    'Id' : 3,
    'name' : 'sri',
    'position' : 'manager',
    'salary' : 40000,
    'email' : 'sri@gmail.com',
    'phno' : '9025817639'
    },{
    'Id' : 2,
    'name' : 'prakash',
    'position' : 'gmanager',
    'salary' : 50000,
    'email' : 'prakash@gmail.com',
    'phno' : '9125807639'
    },{
    'Id' : 1,
    'name' : 'mani',
    'position' : 'CEO',
    'salary' : 200000,
    'email' : 'mani@gmail.com',
    'phno' : '9025808139'
    }]

class empconnection():
    def __init__(self,Id,name,position,email,phno,salary,action):
        self.Id = Id
        self.name = name
        self.position = position
        self.salary = salary
        self.email = email
        self.phno = phno
        self.action = action

    def employee(self):
        print(f'Id : {self.Id}')
        print(f'name : {self.name}')
        print(f'position : {self.position}')
        print(f'salary : {self.salary}')
        print(f'email : {self.email}')
        print(f'phone number : {self.phno}')
        
    def manager(self):
        print(f'Id : {self.Id}')
        print(f'name : {self.name}')
        print(f'position : {self.position}')
        print(f'salary : {self.salary}')
        print(f'email : {self.email}')
        print(f'phno : {self.phno}')
        action_p = input('Do you want to employee details (1) yes / (2) no:')
        if action_p == '1':
            self.employee()
        else:
            print('thank you for coming')

    def gmanager(self):
        print(f'Id : {self.Id}')
        print(f'name : {self.name}')
        print(f'position : {self.position}')
        print(f'salary : {self.salary}')
        print(f'email : {self.email}')
        print(f'phno : {self.phno}')
        action_p = input('Do you want to employee details (1) manager details / (2) employee / (3) exit:')
        if action_p == '1':
            self.manager()
        elif action_p == '2':
            self.employee()
        else:
            print('thank you for coming')

    def CEO(self):
        print(f'Id : {self.Id}')
        print(f'name : {self.name}')
        print(f'position : {self.position}')
        print(f'salary : {self.salary}')
        print(f'email : {self.email}')
        print(f'phno : {self.phno}')
        action_p = input('Do you want to employee details (1) general manager / (2) manager details / (3) employee / (4) exit:')
        if action_p == '1':
            self.gmanager()
        elif action_p == '2':
            self.manager()
        elif action_p == '2':
            self.employee()
        else:
            print('thank you for coming')

    def action_d(self,posi):
        if posi == 'employee':
            self.employee()
        if posi == 'manager':
            self.manager()
        if posi == 'gmanager':
            self.gmanager()
        if posi == 'CEO':
            self.CEO()

for emp in empdetail:
    Id = emp['Id']            
    name = emp['name']        
    position = emp['position']        
    salary = emp['salary']       
    email = emp['email']        
    phno = emp['phno'] 
    action = emp['position']
    operation = empconnection(Id,name,position,email,phno,salary,action)
    operation.action_d(position)

        
