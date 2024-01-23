## ----- Power digit sum ----- ##
#Written By: Aarni Junkkala

#Problem:
#2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2 ** 1000?

#My Thoughts:
#Difficulty of these challenges are conserning me here.
#Some of the tasks are taking quite effort, like primenumbers
#and then there are these tasks where "taking x digits".

number = 2 ** 1000
Snumber = str(number)

total = 0
for i in range(len(Snumber)):
    total += int(Snumber[i])
    
print(total)