n = int(input())
plant_dict = {}

for items in range(n):
    plants = input().split("<->")
    plant = plants[0]
    rarity = int(plants[1])
    if plant not in plant_dict:
        plant_dict[plant] = [rarity]
    else:
        plant_dict[plant].append(rarity)

command = input().split(" - ")

while command[0] != "Exhibition":
    second_command = command[0].split(": ")
    if second_command[0] == "Rate":
        plant_command, rating = second_command[1], int(command[1])
        plant_dict[plant_command].append(rating)
    elif command[0] == "Update":
        plant_command, rating = second_command[1], int(command[1])
    elif command[0] == "Reset":
        pass

    command = input().split(" - ")

print(plant_dict)
