n = int(input())

for _ in range(n):
    current_n = int(input())
    if current_n % 2 != 0:
        print(f"{current_n} is odd!")
        break
else:
    print("All numbers are even.")
