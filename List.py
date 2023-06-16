sum = 0
for number in [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10]:
    if number < 0:
        continue
    sum += number
print(sum)