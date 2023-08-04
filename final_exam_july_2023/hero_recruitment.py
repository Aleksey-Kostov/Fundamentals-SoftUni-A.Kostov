command = input().split()
hero_dict = {}

while command[0] != "End":
    action = command[0]
    if action == "Enroll":
        hero_name = command[1]
        if hero_name not in hero_dict:
            hero_dict[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")
    elif action == "Learn":
        hero_name = command[1]
        spell_name = command[2]
        if hero_name not in hero_dict:
            print(f"{hero_name} doesn't exist.")
        else:
            if spell_name in hero_dict[hero_name]:
                print(f"{hero_name} has already learnt {spell_name}.")
            else:
                hero_dict[hero_name].append(spell_name)
    elif action == "Unlearn":
        hero_name = command[1]
        spell_name = command[2]
        if hero_name not in hero_dict:
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in hero_dict[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}.")
        else:
            hero_dict[hero_name].remove(spell_name)
    command = input().split()

print("Heroes:")
for key, value in hero_dict.items():
    hero_name = key
    print(f"== {hero_name}: {', '.join(value)}")
