## ----- Number spiral diagonals ----- ##
#Written By: Aarni Junkkala

numbers = [1]
for i in range(1,501):
    for k in range(4):
        numbers.append(numbers[-1] + i * 2)
print(sum(numbers))