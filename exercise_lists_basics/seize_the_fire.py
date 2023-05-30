fire = input().split("#")
water = int(input())
list_fire = []
total_water = 0
total_fire = 0
effort = 0

for level in range(len(fire)):
    current_fire = fire[level].split("=")
    list_fire += fire[level].split("=")
    while water >= 0:
        if current_fire[0] == "High" and 81 <= int(current_fire[1]) <= 125:
            total_fire += int(current_fire[1])
            water -= int(current_fire[1])
            effort += 0.25 * int(current_fire[1])
        elif current_fire[0] == "Medium" and 51 <= int(current_fire[1]) <= 80:
            total_fire += int(current_fire[1])
            water -= int(current_fire[1])
            effort += 0.25 * int(current_fire[1])
        elif current_fire[0] == "Low" and 1 <= int(current_fire[1]) <= 50:
            total_fire += int(current_fire[1])
            water -= int(current_fire[1])
            effort += 0.25 * int(current_fire[1])
        else:
            break

print("Cells:")
for index in range(len(list_fire)):
    if index % 2 != 0:
        print(f" - {list_fire[index]}")
print(f"Effort: {effort}")
print(f"Total Fire: {total_fire}")
