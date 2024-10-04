''' 6. Two numbers are input through the keyboard into two locations C and D. Write a 
    program to interchange the contents of C and D.'''

c = int(input('enter a number for c:\t'))
d = int(input('enter a number for d:\t'))

print(f'Before interchanging c:\t{c}')
print(f'Before interchanging d:\t{d}')

temp = c
temp2 = d
c=d
tempt2 = temp


print(f'After interchanging c:\t{c}')
print(f'After interchanging d:\t{tempt2}')
