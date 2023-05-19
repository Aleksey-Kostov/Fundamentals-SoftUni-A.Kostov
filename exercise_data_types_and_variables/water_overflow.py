num = int(input())

TANK_CAPACITY = 255
total_liters = 0

for i in range(num):
    liters = int(input())
    total_liters += liters
    if total_liters > TANK_CAPACITY:
        total_liters -= liters
        print("Insufficient capacity!")
        continue

print(total_liters)
