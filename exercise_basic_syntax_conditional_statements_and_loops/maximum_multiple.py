divisor = int(input())
boundary = int(input())

current_i = 0

for i in range(boundary + 1):
    if i % divisor == 0 and i > 0:
        current_i = i

print(current_i)
