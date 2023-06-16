string_input = input().split("|")
INITIAL_HEALTH = 100
health = INITIAL_HEALTH
total_bitcoins = 0
is_dead = False
best_room = 0

for string in string_input:
    best_room += 1
    current_string = string.split()
    if current_string[0] == 'potion':
        current_health = int(current_string[1])
        if INITIAL_HEALTH < current_health + health:
            diff = INITIAL_HEALTH - health
            health = 100
            print(f'You healed for {diff} hp.')
            print(f"Current health: {health} hp.")
        else:
            health += current_health
            print(f'You healed for {current_health} hp.')
            print(f"Current health: {health} hp.")
    elif current_string[0] == "chest":
        total_bitcoins += int(current_string[1])
        print(f"You found {int(current_string[1])} bitcoins.")
    else:
        health -= int(current_string[1])
        if health > 0:
            print(f"You slayed {current_string[0]}.")
        else:
            is_dead = True
            print(f"You died! Killed by {current_string[0]}.")
            print(f"Best room: {best_room}")
            break


if not is_dead:
    print("You've made it!")
    print(f"Bitcoins: {total_bitcoins}")
    print(f"Health: {health}")
