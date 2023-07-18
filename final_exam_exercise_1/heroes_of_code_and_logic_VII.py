number_of_heroes = int(input())
heroes_dict = {}
current_mp = 0
current_hp = 0

for heroes in range(number_of_heroes):
    hero = input().split()
    name = hero[0]
    hp = hero[1]
    mp = hero[2]
    if name not in heroes_dict:
        heroes_dict[name] = []
    heroes_dict[name] += hp, mp

command = input().split(" - ")

while command[0] != "End":
    if command[0] == "CastSpell":
        if int(command[2]) <= int(heroes_dict[command[1]][1]):
            heroes_dict[command[1]][1] = int(heroes_dict[command[1]][1]) - int(command[2])
            print(f"{command[1]} has successfully cast {command[3]} and now has {heroes_dict[command[1]][1]} MP!")
        else:
            print(f"{command[1]} does not have enough MP to cast {command[3]}!")
    elif command[0] == "TakeDamage":
        if int(command[2]) < int(heroes_dict[command[1]][0]):
            heroes_dict[command[1]][0] = int(heroes_dict[command[1]][0]) - int(command[2])
            print(f"{command[1]} was hit for {command[2]} HP by {command[3]} and now "
                  f"has {heroes_dict[command[1]][0]} HP left!")
        else:
            del heroes_dict[command[1]]
            print(f"{command[1]} has been killed by {command[3]}!")
    elif command[0] == "Recharge":
        current_mp = int(heroes_dict[command[1]][1])
        heroes_dict[command[1]][1] = int(heroes_dict[command[1]][1]) + int(command[2])
        if heroes_dict[command[1]][1] > 200:
            current_mp = 200 - current_mp
            heroes_dict[command[1]][1] = 200
        else:
            current_mp = command[2]
        print(f"{command[1]} recharged for {current_mp} MP!")
    elif command[0] == "Heal":
        current_hp = int(heroes_dict[command[1]][0])
        heroes_dict[command[1]][0] = int(heroes_dict[command[1]][0]) + int(command[2])
        if heroes_dict[command[1]][0] > 100:
            current_hp = 100 - current_hp
            heroes_dict[command[1]][0] = 100
        else:
            current_hp = command[2]
        print(f"{command[1]} healed for {current_hp} HP!")
    command = input().split(" - ")

for key, value in heroes_dict.items():
    print(key)
    print(f"HP: {value[0]}")
    print(f"MP: {value[1]}")

