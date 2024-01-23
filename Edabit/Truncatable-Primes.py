## -------------------- Truncatable Primes -------------------- ##
#Written By: Aarni Junkkala

#A left-truncatable prime is a prime number that contains no 0 digits and,
#when the first digit is successively removed, the result is always prime.

#A right-truncatable prime is a prime number that contains no 0 digits and,
#when the last digit is successively removed, the result is always prime.

#Create a function that takes an integer as an argument and:
#    If the integer is only a left-truncatable prime, return "left".
#    If the integer is only a right-truncatable prime, return "right".
#    If the integer is both, return "both".
#    Otherwise, return False.

primes = [2,3,5] #Primes are saved into a list, so if function is called multiple times, there is no need to recalculate them

#This function could have been way more optimal.
def isPrime(n): #Checks if number is a prime.
    num = primes[-1]
    while num < n: #If there isn't prime high enough in the list to confirm primeness of n
        num += 1
        
        if int(str(num)[-1]) not in [1,3,7,9]: #New number must end with any of these. 
            continue
        
        #Looking for primes
        wasDivideable = False
        for i in primes: #Checks if num is divideable with any of the primes already known
            if num % i == 0:
                wasDivideable = True
                break
        if wasDivideable == False:
            primes.append(num)
    
    #Checks if n was in the list
    if n in primes:
        return True
    return False

def truncatable(n):
    n = str(n) #More easy to handle when n is string
    
    if "0" in n: #Numbers including zeros must be returned.
        return False
    
    left = True
    right = True
    
    #Check left
    for i in range(len(n)):
        if isPrime(int(n[i:])) == False:
            left = False
            break
        
    #Check right
    for i in range(len(n)):
        if isPrime(int(n[:len(n)-i])) == False:
            right = False
            break
    
    #Returning values
    if left and right:
        return "both"
    if left:
        return "left"
    if right:
        return "right"
    return False

#Examples:
print(truncatable(9137)) # ➞ "left"
# Because 9137, 137, 37 and 7 are all prime.

print(truncatable(5939)) # ➞ "right"
# Because 5939, 593, 59 and 5 are all prime.

print(truncatable(317)) # ➞ "both"
# Because 317, 17 and 7 are all prime and 317, 31 and 3 are all prime.

print(truncatable(5)) # ➞ "both"
# The trivial case of single-digit primes is treated as truncatable from both directions.

print(truncatable(139)) # ➞ False
# 1 and 9 are non-prime, so 139 cannot be truncatable from either direction.

print(truncatable(103)) # ➞ False
# Because it contains a 0 digit (even though 103 and 3 are primes).