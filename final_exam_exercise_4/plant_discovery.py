number = int(input())
plant_dict = {}

for plants in range(number):
    current_plant = input().split("<->")
    plant = current_plant[0]
    rarity = current_plant[1]
    plant_dict[plant] = {"rarity": int(rarity)}

command = input().split(" - ")
while command[0] != "Exhibition":
    current_command = command[0].split(": ")
    action = current_command[0]
    plant_command = current_command[1]
    if action == "Rate":
        rating = int(command[1])
        if "rating" not in plant_dict[plant_command]:
            plant_dict[plant_command].update({'rating': rating})
        else:
            plant_dict[plant_command]["rating"] += rating
    elif action == "Update":
        new_rarity = int(command[1])
        plant_dict[plant_command].update({'rarity': new_rarity})
    elif action == "Reset":
        plant_dict.pop(plant_command)
    command = input().split(" - ")
