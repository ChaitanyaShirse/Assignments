'''13. If a five-digit number is input through the keyboard, write a program to print a new 
       number by adding one to each of its digits. For example if the number that is input is 
       12391 then the output should be displayed as 23402.'''

num = input("Enter a five-digit number: ")

new_num = ''
for each in num:
    digit = str((int(each) + 1) % 10)
    new_num += digit

print("The new number is:", new_num)


