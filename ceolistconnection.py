'''
ceo to employee connection using list
'''

empdetails = [
['1','mani','software developer','mani@gmail.com','2'],
['2','ganesh','team leader','ganesh@gmail.com','7'],
['3','prakash','software developer','prakash@gmail.com','2'],
['4','nandhini','team leader','nandhini@gmail.com','7'],
['5','nivin','software developer','nivin@gmail.com','4'],
['6','pradeep','software developer','pradeep@gmail.com','4'],
['7','daran','manager','daran@gmail.com','8'],
['8','manibalan','CEO','mani@gmail.com']
]

class detaillist():
    def __init__(self,ID,name,position,email,senior):
        self.ID = ID
        self.name = name
        self.position = position
        self.email = email
        self.senior = senior

    def uploader(self,file):
        upload.write(f'[{self.ID},')
        upload.write(f'{self.name},')
        upload.write(f'{self.position},')
        upload.write(f'{self.email},')
        upload.write(f'{self.senior}],\n')
        print(f'Id       :{self.ID}')
        print(f'name     :{self.name}')
        print(f'position :{self.position}')
        print(f'email    :{self.email}')
        print(f'senior   :{self.senior}')       

    def fetcher(file):
        file.seek(0)
        lines = file.readlines()
        for line in lines[1:-1]:
            line =  lines[1:-2]
            e =line
            ID = e[0]
            name = e[1]
            position = e[2]
            email = e[3]
            if e[2] != 'CEO':
                senior = e[4]
            else:
                senior = 'CEO'
    
with open('empdetaillist.txt','a') as upload:
    upload.write('emp =[\n')
    for emp in empdetails:
        ID = emp[0]
        name = emp[1]
        position = emp[2]
        email = emp[3]
        if emp[2] != 'CEO':
            senior = emp[4]
        else:
            senior = 'CEO'
        empdetail = detaillist(ID,name,position,email,senior)
        empdetail.uploader(upload)
with open('empdetaillist.txt','r') as upload:
    detaillist.fetcher(upload)
    upload.write(']')

