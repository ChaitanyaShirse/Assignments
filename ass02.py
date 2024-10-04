'''2. The distance between two cities (in km.) is input through the keyboard. Write a program 
   to convert and print this distance in meters, feet, inches and centimeters.'''


distance = int(input('Enter the distance between Two cities (in KM):\t'))
dis_in_meter = distance * 1000
dis_in_feet = dis_in_meter * 3.28
dis_in_inches = dis_in_feet * 12
dis_in_centimeter = dis_in_meter * 100 

print(f'The Distance In KM = {distance} KM\nIn Meter = {dis_in_meter} Meters\nIn Feet = {dis_in_feet} Feets\nIn Inches = {dis_in_inches} Inches\nIn Centimeters = {dis_in_centimeter} Centimeters')


