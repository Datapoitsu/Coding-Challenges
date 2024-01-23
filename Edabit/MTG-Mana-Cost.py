## -------------------- MTG Mana Cost -------------------- ##
#Written By: Aarni Junkkala

# In the trading card game Magic: the Gathering,
# players must use a resource called mana to cast spells.
# There are six types of mana in Magic:
# white (W), blue (U), black (B), red (R), green (G), and colorless (C).
# The mana cost of a spell indicates the amount and type(s)
# of mana that must be paid to cast the spell.

# If the mana cost contains a number (such as "3"),
# that number must be paid with that total amount of mana in any combination of types.
# If the mana cost contains a mana type ("W", "U", "B", "R", "G", or "C"),
# that symbol must be paid with one mana of the corresponding type.
# Each individual mana in the player's mana pool can only pay one part of the cost.
# For example, the mana cost "3WW" requires
# two white (W) mana and 3 additional mana in any combination of types.
# The two white mana used to pay the "WW" do not also contribute to the "3".

# In this challenge, the player's mana pool will be represented as
# a string, with each character (W, U, B, R, G, or C) representing a single mana.
# The mana cost to be paid will also be represented as a string, which may contain
# a single one or two digit number and/or any number of W, U, B, R, G, and C characters.

# Write a function that takes in the two strings,
# the player's mana and a mana cost,
# and determines whether or not the player's mana can pay the cost.

def can_pay_cost(mana_pool,cost):
    if cost == "0":
        return True

    ## ----- Find the amount of neutral mana ----- ##
    #Checks for the amount of numeral digits at start of the cost
    NumeralDigits = 0
    for i in range(len(cost)):
        try:
            int(cost[i])
            NumeralDigits += 1
        except:
            break
    
    Neutralmana = 0 #How many neutral mana_pool are in the cost
    if NumeralDigits > 0:
        Neutralmana = int(cost[0:NumeralDigits])

    ## ----- Check for colored mana_pool ----- ##
    mana_pool = list(mana_pool)
    ColoredCost = cost[NumeralDigits:]
    for i in range(len(ColoredCost)):
        if ColoredCost[i] in mana_pool:
            mana_pool.remove(ColoredCost[i])
        else:
            return False
    
    if len(mana_pool) >= Neutralmana:
        return True
    return False

if __name__ == "__main__":
    print(can_pay_cost("WWGGR","2WWG")) #True
    print(can_pay_cost("WWGG", "2WWG")) #False
    print(can_pay_cost("WGGGR","2WWG")) #False
    print(can_pay_cost("WUUBC", "UUB")) #True