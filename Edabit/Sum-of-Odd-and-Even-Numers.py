def sum_odd_and_even(lst):
    sumOdd = 0
    sumEven = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            sumEven += lst[i]
        if lst[i] % 2 == 1:
            sumOdd += lst[i]
    return [sumEven,sumOdd]