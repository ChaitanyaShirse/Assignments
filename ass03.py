''' 3. If the marks obtained by a student in five different subjects are input through the 
    keyboard, find out the aggregate marks and percentage marks obtained by the student. 
    Assume that the maximum marks that can be obtained by a student in each subject is 
    100.'''

PP = int(input('Enter a marks of Python Programing:\t\t'))
NT = int(input('Enter a marks of Networ Theory:\t\t\t'))
SS = int(input('Enter a marks of Signal System:\t\t\t'))
PTRP = int(input('Enter a marks of Probability & Random Process:\t'))
BHR = int(input('Enter a marks of Basic Human Rights:\t\t'))

total_marks = 500
obtained_marks = PP + NT + SS + PTRP + BHR
persent = (obtained_marks / total_marks) * 100
print(f'Aggregate marks of the semister = {obtained_marks} / {total_marks}.')
print(f'The student obtained {persent}% marks in the semister.')

