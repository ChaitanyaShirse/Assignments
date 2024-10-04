'''9. If a four-digit number is input through the keyboard, write a program to obtain the sum 
      of the first and last digit of this number.'''

num = int(input("Enter a four-digit number: "))
first_digit = num // 1000
last_digit = num % 10
sum = first_digit + last_digit
print("The sum of the first and last digits is:", sum)


