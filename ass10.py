'''10. In a town, the percentage of men is 52. The percentage of total literacy is 48. If total 
       percentage of literate men is 35 of the total population, write a program to find the total 
       number of illiterate men and women if the population of the town is 80,000'''

population = 80000
men = (population/100)*52
literacy = (population/100)*48
literate_men = (population/100)*35

women = population - men
illiterate = population - literacy
illiterate_men = men - literate_men
illiterate_women = women - (literacy - literate_men)


print("Total number of illiterate men:", illiterate_men)
print("Total number of illiterate women:", illiterate_women)

