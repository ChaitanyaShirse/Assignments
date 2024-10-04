'''5. The length & breadth of a rectangle and radius of a circle are input through the 
    keyboard. Write a program to calculate the area & perimeter of the rectangle, and the 
    area & circumference of the circle.'''

lenght = int(input('Enter the lenght of the rectangle:\t'))
breadth = int(input('Enter the breadth of the rectangle:\t'))
radius = int(input('Enter the radius of the circle:\t'))

area_of_rectangle = lenght * breadth
parameter =  2 * breadth + 2 * lenght
area_of_circle = 3.14 * (radius * radius)
circumfarence = 2 * 3.14 * radius

print(f'The area of the rectangle is {area_of_rectangle}sqrm.')
print(f'The parameter of the rectangle is {parameter}.')
print(f'The area of the circle is {area_of_circle}.')
print(f'The circumfarence of the circle is {circumfarence}.')
