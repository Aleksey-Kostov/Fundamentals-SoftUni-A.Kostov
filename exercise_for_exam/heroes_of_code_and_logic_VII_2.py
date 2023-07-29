def cast_spell(current_command, current_heroes_dict):
    hero_name = current_command[1]
    mp_needed = int(current_command[2])
    spell_name = current_command[3]
    if current_heroes_dict[hero_name]["MP"] < mp_needed:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    else:
        current_heroes_dict[hero_name]["MP"] -= mp_needed
        print(f"{hero_name} has successfully cast {spell_name} and now has"
              f" {current_heroes_dict[hero_name]['MP']} MP!")
    return current_heroes_dict[hero_name]["MP"]


def take_damage(current_command, current_heroes_dict):
    hero_name = current_command[1]
    damage = int(current_command[2])
    attacker = current_command[3]
    if damage < current_heroes_dict[hero_name]["HP"]:
        current_heroes_dict[hero_name]["HP"] -= damage
        print(f"{hero_name} was hit for {damage} HP by"
              f" {attacker} and now has {current_heroes_dict[hero_name]['HP']} HP left!")
    else:
        del current_heroes_dict[hero_name]
        print(f"{hero_name} has been killed by {attacker}!")
    return current_heroes_dict


def recharge(current_command, current_heroes_dict):
    hero_name = current_command[1]
    amount = int(current_command[2])
    total_amount = amount + current_heroes_dict[hero_name]["MP"]
    if total_amount > 200:
        diff = 200 - current_heroes_dict[hero_name]["MP"]
        current_heroes_dict[hero_name]["MP"] = 200
    else:
        diff = amount
        current_heroes_dict[hero_name]["MP"] = current_heroes_dict[hero_name]["MP"] + amount
    print(f"{hero_name} recharged for {diff} MP!")
    return current_heroes_dict


def heal(current_command, current_heroes_dict):
    hero_name = current_command[1]
    amount = int(current_command[2])
    total_amount = amount + current_heroes_dict[hero_name]["HP"]
    if total_amount > 100:
        diff = 100 - current_heroes_dict[hero_name]["HP"]
        current_heroes_dict[hero_name]["HP"] = 100
    else:
        diff = amount
        current_heroes_dict[hero_name]["HP"] = current_heroes_dict[hero_name]["HP"] + amount
    print(f"{hero_name} healed for {diff} HP!")
    return current_heroes_dict


number_of_heroes = int(input())
heroes_dict = {}

for heroes in range(number_of_heroes):
    current_heroes = input().split()
    name_of_hero = current_heroes[0]
    health_points = current_heroes[1]
    mana_points = current_heroes[2]
    heroes_dict[name_of_hero] = {"HP": int(health_points), "MP": int(mana_points)}

command = input().split(" - ")

while command[0] != "End":
    action = command[0]
    if action == "CastSpell":
        cast_spell(command, heroes_dict)
    elif action == "TakeDamage":
        take_damage(command, heroes_dict)
    elif action == "Recharge":
        recharge(command, heroes_dict)
    elif action == "Heal":
        heal(command, heroes_dict)
    command = input().split(" - ")


for key, value in heroes_dict.items():
    hero_name_dict = key
    print(f"{hero_name_dict}")
    hp_dict = heroes_dict[hero_name_dict]["HP"]
    mp_dict = heroes_dict[hero_name_dict]["MP"]
    print(f"HP: {hp_dict}\nMP: {mp_dict}")
