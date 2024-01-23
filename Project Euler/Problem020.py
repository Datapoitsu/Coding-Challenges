## ----- Factorial digit sum ----- ##
#Written By: Aarni Junkkala

#Problem:
#n! means n × (n − 1) × ... × 3 × 2 × 1
#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#Find the sum of the digits in the number 100!

#My Thoughs:
#This one introduces Factorial in quite nice way.

def FactorialDigitSum(n):
    #Factorial
    num = 1
    for i in range(n,0,-1):
        num *= i
    #Calculates the sum of digits
    num = str(num)
    result = 0
    for i in range(len(num)):
        result += int(num[i])
    return result

print(FactorialDigitSum(100))