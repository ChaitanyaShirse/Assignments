''' 7. If a five-digit number is input through the keyboard, write a program to calculate the 
       sum of its digits. (Hint: Use the modulus operator ‘%’)'''

num = int(input('Enter a five digit number:\t'))
sum = 0

while num!=0:
	digit = int(num%10)
	sum += digit
	num = num/10

print(f'sum of five digits = {sum}')

