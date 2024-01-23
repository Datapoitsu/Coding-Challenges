## ----- Largest prime factor ----- ##
#Written By: Aarni Junkkala

#Problem:
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#My Thoughts:
#I will be looking for primes, till I find one that can divide the number.
#When divided: the prime will be saved.
#If none of the primes work, then I will look for a new prime.
#Reason not to look for all primes, is that would take way too much
#computing and we have no idea how big largest prime in this problem is.

num = 600851475143
PrimeFactors = []
Primes = [2,3,5] #Starting from 2,3,5 as then rest of primes end with 1,3,7 or 9

#Looks for next prime and adds it to prime lsit
def FindNextPrime():
    global Primes
    num = Primes[-1] + 1 #Number to be tested
    while True: #Repeat till next is found
        if str(num)[-1] in ["1","3","7","9"]: #Excludes numbers that aren't ending properly
            isPrime = True
            for i in Primes:
                if (num / i).is_integer() == True: #if divisible by any prime, then not a prime
                    isPrime = False
                    break
            if isPrime == True:
                Primes.append(num)
                return
        num += 1

#Process will be repeeated till number is reduced to one.
while num > 1:
    for i in range(len(Primes)):#Tries to divide with every prime number
        if (num / Primes[i]).is_integer() == True: #If result is an integer.
            PrimeFactors.append(Primes[i])
            num = num / Primes[i] #actually dividing the number
            break
    FindNextPrime()
print("Largest primefactor: " + str(max(PrimeFactors)))