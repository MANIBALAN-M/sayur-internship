'''
organization management (or) relation beteen work & CEO
'''

class management():
    def __init__(self,name,desig,salary,phno):
        self.name =name
        self.desig = desig
        self.salary =salary
        self.phno = phno
        self.head = None

def printer(emp):
    print(f'name : {emp.name}')
    print(f'designation : {emp.desig}')
    print(f'salary : {emp.salary}')
    print(f'phone number : {emp.phno}')
    while emp.head != None:
        print(f'incharge : {emp.head.name}')
        emp = emp.head
        print(emp)

emp1 = management('Manibalan','CEO',100000,'9025808139')
emp2 = management('Akshat','managing director',80000,'8976543210')
emp2.head = emp1
emp3 = management('Dinesh kumar','marketing director',75000,'9087654321')
emp3.head = emp2
emp4 = management('Senthil','designing director',70000,'8765904321')
emp4.head = emp3
emp5 = management('Daniel','team leader',60000,'6578904321')
emp5.head = emp4
emp6 = management('Vasanth','senior developer',50000,'8769054321')
emp6.head = emp5
emp7 = management('Roshan','junior developer',30000,'7658904321')
emp7.head = emp6
printer(emp7)

employee = [emp7,emp6,emp5,emp4,emp3,emp2,emp1]

