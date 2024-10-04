'''11. A cashier has currency notes of denominations 10, 50 and 100. If the amount to be 
       withdrawn is input through the keyboard in hundreds, find the total number of currency 
       notes of each denomination the cashier will have to give to the withdrawer.'''


amount = int(input("Enter the amount to be withdrawn in hundreds: "))

notes_100 = amount//100
amount = amount%100
notes_50 = amount//50
amount = amount%50
notes_10 = amount//10

print("Number of 100 rupee notes:", notes_100)
print("Number of 50 rupee notes:", notes_50)
print("Number of 10 rupee notes:", notes_10)
