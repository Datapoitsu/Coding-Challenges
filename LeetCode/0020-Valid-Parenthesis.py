## ----- Valid parentheses ----- ##
#Written By: Aarni Junkkala
#Date: 24.1.2023

#Runtime: 32 ms. Beats 86.01% of user with python3
#Memory: 16.61 MB. Beats 57.35% of users with Python3

#Based on an idea to list up parentheses that have appeared.
#When closing parentheses appears program checks if last one was one that opened it.

class Solution:
    def isValid(s):
        # -- Listing opening parenthesis -- #
        L = []
        for i in range(len(s)):
            if s[i] in ["(","[","{"]:
                L.append(s[i])
            
            # -- Checking the closing parentheses -- #
            #This could have been done with list and it would look lot nicer as a code,
            #but the speed of the program slows down.
            if s[i] == ")":
                if len(L) > 0 and L[-1] == "(":
                    L.pop()
                else:
                    return False
            
            if s[i] == "]":
                if len(L) > 0 and L[-1] == "[":
                    L.pop()
                else:
                    return False
                    
            if s[i] == "}":
                if len(L) > 0 and L[-1] == "{":
                    L.pop()
                else:
                    return False
        
        #If there was any left over brackes, will be false.
        if len(L) > 0:
            return False
        return True