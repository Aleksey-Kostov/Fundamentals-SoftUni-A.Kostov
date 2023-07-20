target = input().split("||")
target_dict = {}

while target[0] != "Sail":
    cities, population, gold = target[0], int(target[1]), int(target[2])
    if cities not in target_dict:
        target_dict[cities] = [population, gold]
    else:
        target_dict[cities][0] += population
        target_dict[cities][1] += gold
    target = input().split("||")

command = input().split("=>")

while command[0] != "End":
    if command[0] == "Plunder":
        town, people, gold_command = command[1], int(command[2]), int(command[3])
        if people <= target_dict[town][0] and gold_command <= target_dict[town][1]:
            target_dict[town][0] -= people
            target_dict[town][1] -= gold_command
            print(f"{town} plundered! {gold_command} gold stolen, {people} citizens killed.")
        if target_dict[town][0] == 0 or target_dict[town][1] == 0:
            del target_dict[town]
            print(f"{town} has been wiped off the map!")
    elif command[0] == "Prosper":
        town, gold_command = command[1], int(command[2])
        if gold_command >= 0:
            target_dict[town][1] += gold_command
            print(f"{gold_command} gold added to the city treasury. {town} now has {target_dict[town][1]} gold.")
        else:
            print("Gold added cannot be a negative number!")
    command = input().split("=>")

if len(target_dict) > 0:
    print(f"Ahoy, Captain! There are {len(target_dict)} wealthy settlements to go to:")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
for cities, resource in target_dict.items():
    if cities:
        print(f"{cities} -> Population: {resource[0]} citizens, Gold: {resource[1]} kg")

