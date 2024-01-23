## ----- Amicable numbers ----- ##
#Written By: Aarni Junkkala

#Problem:
#Let d(n) be defined as the sum of
#proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b,
#then a and b are an amicable pair and
#each of a and b are called amicable numbers.

#For example, the proper divisors of 220 are
#1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
#therefore d(220) = 284. The proper divisors of 284 are
#1, 2, 4, 71 and 142; so d(284) = 220.

#Evaluate the sum of all the amicable numbers under 10000.

#My Thoughs:
#I need to look for all possibilities for all numbers under 10000.
#I will test every single number I find against the number that it
#gives as the result. That will reduce amount of Divisor counting to 20000


def SumOfProperDivisors(n): #Tests if n is divisable with all numbers lower.
    Divisors = []
    for i in range(n - 1, 0, -1):
        if (n / i).is_integer() == True:
            Divisors.append(i)
    return sum(Divisors)

Amicable = []
for i in range(1,10000):
    if i in Amicable: #If already in the list, then no need to test.
        continue
    a = SumOfProperDivisors(i)
    if SumOfProperDivisors(a) == i and a != i:
        Amicable.append(i)
print(sum(Amicable))
