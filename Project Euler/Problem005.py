## ----- Smallest multiple ----- ##
#Written by: Aarni Junkkala

#Problem:
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#My Thoughs:
#This problem is just least common multiple of the chosen list.
#For looking all possible solutions we know that aswer must be in multiple of the largest in the list,
#so we can only test numbers that increase by the amount of highest number.
#we can also reduce all numbers that are divisibles of themselfs in the list,
#so all numbers from 10 and below.

numbers = [20,19,18,17,16,15,14,13,12,11]
num = 0
while True:
    num += max(numbers)
    CorrectNumber = True
    for i in numbers: 
        if (num / i).is_integer() == False: #Must be divisible by all numbers in the list
            CorrectNumber = False
            break
    if CorrectNumber == True:
        print(num)
        break