time_car = input().split()

index = int(int(len(time_car)) / 2)
left_car = 0
right_car = 0

for left_time in time_car[:index]:
    left_time = int(left_time)
    if left_time != 0:
        left_car += left_time
    else:
        left_car = 0.8 * left_car

for right_time in time_car[index:]:
    right_time = int(right_time)
    if right_time != 0:
        right_car += right_time
    else:
        right_car = 0.8 * right_car

print(f"{left_car:.1f}")
print(f"{right_car:.1f}")
