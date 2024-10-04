''' 1. Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of 
    basic salary, and house rent allowance is 20% of basic salary. Write a program to 
    calculate his gross salary.'''

salary = int(input('Enter the basic salary of Ramesh:\t'))
dearness_allowance = (salary/100)*40
house_rent_allowance = (salary/100)*20
gross_salary = salary + dearness_allowance + house_rent_allowance

print(f"The total gross salary of Ramesh is {gross_salary}.")