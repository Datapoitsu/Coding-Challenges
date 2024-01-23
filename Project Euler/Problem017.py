## ----- Number letter counts ----- ##
#Written By: Aarni Junkkala

#Problem:
#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

#My Thoughs:
#This one was easy but fun.
#With the names of english numbers it is quite easy to build up all numbers,
#as they doesn't have any weirdness in them. No partitive, no nothing.
#This mostly about listing the amount of numbers, and not really about building the words

Ones = ["one","two","three","four","five","six","seven","eight","nine"]
Teens = ["eleven", "twelve","thirteen", "fourteen","fifteen", "sixteen","seventeen","eighteen","nineteen"]
Tens = ["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

def Calculate():
    total = 0
    for i in range(1000,0,-1):
        
        sana = ""
        StringI = str(i)
        
        #Thousand
        if len(StringI) == 4:
            sana += "oneThousand"
        #Hundreds
        if len(StringI) == 3:
            sana += Ones[int(StringI[-3]) - 1] + "hundred"
            if StringI[-2] != "0" or StringI[-1] != "0":
                sana += "and"
        #Tens
        if len(StringI) > 1:
            #Tens that aren't 10-19
            if StringI[-2] != "1" and StringI[-2] != "0":
                sana += Tens[int(StringI[-2]) - 1]
            #Ten
            if StringI[-2] == "1" and StringI[-1] == "0":
                sana += "Ten"
            #teens
            if StringI[-2] == "1" and StringI[-1] != "0":
                sana += Teens[int(StringI[-1]) - 1]
                total += len(sana)
                continue
            
        if StringI[-1] != "0":
            sana += Ones[int(StringI[-1]) - 1]
        total += len(sana)
    return total

print(Calculate())