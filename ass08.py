'''  8. If a five-digit number is input through the keyboard, write a program to reverse the number'''

num = int(input('Enter a 5 digit number :'))
rev_num = 0

while num != 0:
    digit = num % 10
    rev_num = rev_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(rev_num))


