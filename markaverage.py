'''
you have a list of student names. you have one list each for their marks in CS, Math and English. 
hard code the values. no need to get it as input
Pass mark is 50.
Grade A is, mark 90 or above
Grade B , 80 or above
Fail is < 50
Print the name of the students who got A in all subjects or atleast one A and the rest B.
Try to use only one if statement.

'''
import sys
name = ['akshat','dinesh','mani','srisanth','senthil']
cs_mark= [65,78,90,80,85,98]
math_mark= [87,90,95,97,89,97]
eng_mark= [87,90,95,94,96]

for i in range(len(name)):
    if((cs_mark[i]>=90 and math_mark[i]>=90 and eng_mark[i]>=90)or(cs_mark[i]>=90 and math_mark[i]>=80 and eng_mark[i]>=80)or(math_mark[i]>=90 and cs_mark[i]>=80 and eng_mark[i]>=80)or(eng_mark[i]>=90 and math_mark[i]>=80 and cs_mark[i]>=80)):
        print('the students got A in all subject or atleast 1 subject and got others in B are',name[i])
