num = input()

m = sorted(num, reverse=True)

for index, digits in enumerate(m):
    print(digits, end="")
