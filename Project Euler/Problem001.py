## ----- Multiples of 3 or 5 ----- ##
#Written By: Aarni Junkkala

#Problem:
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#My thoughts:
#For this we need to use modulo of both 3 and 5.
#I want to build this in way where,
#I can just insert list of numbers that are ok to be multipiers

Multipliers = [3,5]
Multiples = []
for i in range(1000):
    MultipleOf = False
    for k in Multipliers:
        if i % k == 0:
            MultipleOf = True
            break
    if MultipleOf == True:
        Multiples.append(i)
print("Sum: " + str(sum(Multiples)))