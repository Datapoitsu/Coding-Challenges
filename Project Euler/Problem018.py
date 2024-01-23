## -------------------- Maximum path sum I -------------------- ##
#Written By: Aarni Junkkala

#Problem:
#By starting at the top of the triangle below and moving
#to adjacent numbers on the row below,
#the maximum total from top to bottom is 23.

#3
#7 4
#2 4 6
#8 5 9 3

#That is, 3 + 7 + 4 + 9 = 23.

#Find the maximum total from top to bottom of the triangle below:

numbers = [
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20,  4, 82, 47, 65],
[19,  1, 23, 75,  3, 34],
[88,  2, 77, 73,  7, 63, 67],
[99, 65,  4, 28,  6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]
]

# numbers = [
# [3],
# [7, 4],
# [2, 4, 6],
# [8, 5, 9, 3]
# ]

#NOTE: As there are only 16384 routes,
#it is possible to solve this problem by trying every route.
#However, Problem 67, is the same challenge
#with a triangle containing one-hundred rows;
#it cannot be solved by brute force, and requires a clever method! ;o)

#My Thoughts:
#This one opened my mind up for pathfinding methods.
#Mostly this problem is all about valuating all routes.
#For the value I just started from the end and gave,
#every slot value based on it's own value and greater one
#of the two that it can go. When starting from the bottom,
#values will increase towards up, but even better is that
#best route can have some very bad numbers and it will take
#that to notice.

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
for i in range(len(numbers)):
    print(str(numbers[i]) + " -> " + str(Path[i]))