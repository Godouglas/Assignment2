Sum = 0
while Sum >= 0:
	num = int(input("Enter number: "))
	if num < 0:
		break
	Sum += num
print(Sum)