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

for right_time in time_car[:index:-1]:
    right_time = int(right_time)
    if right_time != 0:
        right_car += right_time
    else:
        right_car = 0.8 * right_car

if left_car < right_car:
    print(f"The winner is left with total time: {left_car:.1f}")
else:
    print(f"The winner is right with total time: {right_car:.1f}")
