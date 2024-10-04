'''12. If the total selling price of 15 items and the total profit earned on them is input through 
       the keyboard, write a program to find the cost price of one item.'''

price = int(input("Enter the total selling price of 15 items: "))
profit = int(input("Enter the total profit earned on 15 items: "))

cost_price = (price - profit) // 15

print("The cost price of one item is:", cost_price)



