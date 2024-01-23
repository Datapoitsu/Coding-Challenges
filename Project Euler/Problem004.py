## -- Largest palindrome product -- #
#Written By: Aarni Junkkala

#Problem:
#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

#My Thoughs:
#For this we need to test two numbers agains each other and reduce them till we reach 99.
#We will have to list all possible answers as 999 X 993 could be first working solution,
#but 998 x 998 is greater number, so we can't know witch is highest, before we know all of them.

#Note: This could have been done lot more dynamic.

def LargestPalindromeProduct():
    PalindromeProducts = []
    num1 = 999
    num2 = 999
    
    while num1 > 99: #repeat till num isn't 3 digits
        num2 = 999
        while num2 > 99:
            holder = str(num1 * num2)
            if len(holder) == 6:
                if holder[0] == holder[-1] and holder[1] == holder[-2] and holder[2] == holder[-3]:
                    PalindromeProducts.append(int(holder))
            num2 -= 1
        num1 -= 1
    return max(PalindromeProducts)

print("Largest Palindromeproduct: " + str(LargestPalindromeProduct()))