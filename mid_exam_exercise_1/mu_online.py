string_input = input().split("|")
INITIAL_HEALTH = 100
chest_list = []
max_string = 0
string_index = 0

for string in string_input:
    current_string = string.split()
    if current_string[0] == 'potion':
        if INITIAL_HEALTH >= int(current_string[1]):
            new_string = int(current_string[1])
            print(f'You healed for {new_string} hp.')
            print(f"Current health: {INITIAL_HEALTH + new_string} hp.")
    elif current_string[0] == "chest":
        if max_string < int(current_string[1]):
            max_string = int(current_string[1])
            string_index = string_input.index(string)
        print(f"You found {int(current_string[1])} bitcoins.")
    else:
        INITIAL_HEALTH -= int(current_string[1])
        if INITIAL_HEALTH > 0:
            print(f"You slayed {current_string[0]}.")
        else:
            print(f"You died! Killed by {current_string[0]}.")
            print(f"Best room: {string_index}")
            break


