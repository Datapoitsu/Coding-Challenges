## ----- Special Pythagorean triplet ----- ##
#Written By: Aarni Junkkala

#Problem:
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a**2 + b**2 = c**2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

#My Thoughs:
#I can just brute force the answer out.
#There is only 3 numbers that can vary from 1 to 1000
#This isn't fastest way to solve the problem, but good enought for now.

# a < b < c
def Problem():
    for i in range(1,1000):
        for k in range(1,1000):
            for j in range(1,1000):
                if i < k and k < j and i ** 2 + k ** 2 == j ** 2 and i + k + j == 1000:
                    return i * k * j
print(Problem())