def divisible_by_b(a, b):
    num = a
    while True:
        num += 1
        if num % b == 0:
            return num
print(divisible_by_b(17,8))
