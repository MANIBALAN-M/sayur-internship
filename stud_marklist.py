'''
1.you have a list of student names. you have one list each for their marks in CS, Math and English. 
hard code the values. no need to get it as input
Pass mark is 50.
Grade A is, mark 90 or above
Grade B , 80 or above
Fail is < 50
Print the name of the students who got A in all subjects or atleast one A and the rest B.
Try to use only one if statement.
'''
import sys
stud_names = ['akshat','ashik','dinesh','mani']
cs_mark = [78,87,76,45]
math_mark = [89,87,90,90]
eng_mark = [89,85,97,95]
for i in stud_names:
    if int(cs_mark[i])<50 or int(math_mark[i])<50 or int(eng_mark[i])<50:
        print(f'your fail {stud_names}')

