'''############## Problem  3  #################### 
#Calculate the monthly salary for the phone salesman
#Base monthly pay Rs10000. 
#For every 5 phones sold, Rs 5000 bonus.
#For every phone aftr the first 5 phones, Rs1100 per phone bonus.
#If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
# this month also, then he gets additional Rs5000.

monthlySalesList = [5,23,21,14,23,12,4,12,22,22,34,12]  # Sample number of phones sold in each month in a year
#FillinMissingCode - initialise all the variables needed

for month, phoneCount in enumerate(monthlySalesList):
    #calculate the Salary using If stmts
    #FillinMissingCode
    currentMonthSalary = #FillinMissingCode
    print (f"This month's salary before additional bonus {currentMonthSalary}") 

    #check for condition #If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
    # this month also, then he gets additional Rs5000.

    if(phoneCount < 20):
        previousMonthSalary = currentMonthSalary #we set this so that, we can use this info in the next iteration
        continue #no need to calculate anything because <20 phones sold
    
    #calculate the new salary
    currentMonthSalary =   #FillinMissingCode
    print({f}This month's salary after additional bonus {currentMonthSalary})
    previousMonthSalary = currentMonthSalary #Why are we doing this?
'''

import sys
monthlysalary = 10000
bonussalary1 = 0
premonthsalary = 0
monthlySales = [5,23,21,14,23,12,4,12,22,22,34,12]
for i in (monthlySales):
    if i != 0 and i % 5==0:
        bonussalary1 = (i//5)*5000
    if i >= 5:
        bonussalary2 = bonussalary1 + (i-5)* 1100
        currentmonthsalary = monthlysalary + bonussalary2
        print(f"This month's salary after additional bonus: {currentmonthsalary}")
    if i < 20:    
        premonthsalary = currentmonthsalary
    '''if premonthsalary - currentmonthsalary >= 20000:
        currentmonthsalary = currentmonthsalary + 5000 
        print(f"This month's salary after additional bonus: {currentmonthsalary}")
    '''
        
