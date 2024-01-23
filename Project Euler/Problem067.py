## -------------------- Maximum path sum I -------------------- ##
#Written By: Aarni Junkkala

#Problem:
#By starting at the top of the triangle below
#and moving to adjacent numbers on the row below,
#Find the maximum total from top to bottom in triangle.txt
#a 15K text file containing a triangle with one-hundred rows.

#My Thoughts:
#This one opened my mind up for pathfinding methods.
#Mostly this problem is all about valuating all routes.
#For the value I just started from the end and gave,
#every slot value based on it's own value and greater one
#of the two that it can go. When starting from the bottom,
#values will increase towards up, but even better is that
#best route can have some very bad numbers and it will take
#that to notice.
numbers = []
f = open("p067_triangle.txt", "r")
for x in f:
    row = x.split()
    for i in range(len(row)):
        row[i] = int(row[i])
    numbers.append(row)


import copy

PropabilityPath = copy.deepcopy(numbers) #Copy of the number list.
for i in range(len(PropabilityPath) - 2, -1, -1): #Starting from second bottom row, to highest row.
    for k in range(len(PropabilityPath[i])):
        #Set's value to be combination of self and greater number below.
        if PropabilityPath[i][k] + PropabilityPath[i + 1][k + 1] >= PropabilityPath[i][k] + PropabilityPath[i + 1][k]:
            PropabilityPath[i][k] += PropabilityPath[i + 1][k + 1]
        else:
            PropabilityPath[i][k] += PropabilityPath[i + 1][k]

Total = 0
Path = []
CurrentColumm = 0
for i in range(len(PropabilityPath)):
    if i != 0: #First one is always same
        if PropabilityPath[i][CurrentColumm] < PropabilityPath[i][CurrentColumm + 1]:
            CurrentColumm += 1
    Total += numbers[i][CurrentColumm]
    Path.append(CurrentColumm)

print(Total)
print(Path)    