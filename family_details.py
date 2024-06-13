import sys
from datetime import datetime

num_of_members = input("enter number of family members : ")
if num_of_members.isdigit() != 1 :
    print("please enter positive numerical values")
    sys.exit()
num_of_members = int(num_of_members)
if num_of_members < 2 or num_of_members > 25 :
    print("you enter invalid number of family members")
    sys.exit()

minor = 0
major = 0
senior_citizen = 0
for i in range (1,num_of_members+1) :
    name = input(f"enter the name of family member {i} :")
    if name.isalpha() != 1 :
        print("your name must be contain only alphabetic characters")
        sys.exit()
    age = input(f"enter the age of family member {i} :")
    if age.isdigit() != 1 :
        print("please enter positive numerical values")
        sys.exit()
    age = int(age)
    if age < 1 or age > 110 :
        print("you enter invalid number of age")
        sys.exit()
    if age < 18 :
        minor = minor+1
    if age >= 18 :
        major = major+1
    if age >= 61 :
        senior_citizen = senior_citizen+1

print(f"minor {minor}")
print(f"major {major}")
print(f"senior citizen {senior_citizen}")
    

