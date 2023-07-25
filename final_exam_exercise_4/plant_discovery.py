number = int(input())
plant_dict = {}

for plants in range(number):
    current_plant = input().split("<->")
    plant = current_plant[0]
    rarity = current_plant[1]
    if plant not in plant_dict:
        plant_dict[plant] = {"rarity": int(rarity), "rating": []}
    else:
        plant_dict[plant]["rarity"] += int(rarity)

command = input().split(" - ")
while command[0] != "Exhibition":
    current_command = command[0].split(": ")
    action = current_command[0]
    plant_command = current_command[1]
    if plant_command not in plant_dict:
        print("error")
    elif action == "Rate":
        rating = int(command[1])
        plant_dict[plant_command]["rating"].append(rating)
    elif action == "Update":
        new_rarity = int(command[1])
        plant_dict[plant_command]["rarity"] = new_rarity
    elif action == "Reset":
        plant_dict[plant_command]["rating"] = []
    else:
        print("error")
    command = input().split(" - ")

print("Plants for the exhibition:")
for plant_name, items in plant_dict.items():
    if not plant_dict[plant_name]["rating"]:
        average_rating = 0
    else:
        average_rating = sum(plant_dict[plant_name]["rating"]) / len(plant_dict[plant_name]["rating"])
    current_plant_name = plant_dict[plant_name]
    rarity = int(plant_dict[plant_name]["rarity"])
    print(f"- {plant_name}; Rarity: {rarity}; Rating: {average_rating:.2f}")
