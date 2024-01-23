def find_highest(lst):
    highest = lst[0]
    for i in range(1,len(lst)):
        if lst[i] > highest:
            highest = lst[i]
    return highest
print(find_highest([-1, 3, 5, 6, 99, 12, 2]))