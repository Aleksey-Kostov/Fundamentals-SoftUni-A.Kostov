list_of_cards = input().split(", ")
number_of_command = int(input())

for command in range(number_of_command):
    string_command = input().split(", ")
    if string_command[0] == "Add":
        if string_command[1] not in list_of_cards:
            list_of_cards.append(string_command[1])
            print("Card successfully added")
        else:
            print("Card is already in the deck")
    elif string_command[0] == "Remove":
        if string_command[1] in list_of_cards:
            list_of_cards.remove(string_command[1])
            print("Card successfully removed")
        else:
            print("Card not found")
    elif string_command[0] == "Remove At":
        if int(string_command[1]) in range(len(list_of_cards)):
            list_of_cards.pop(int(string_command[1]))
            print("Card successfully removed")
        else:
            print("Index out of range")
    elif string_command[0] == "Insert":
        if int(string_command[1]) in range(len(list_of_cards)):
            if string_command[2] not in list_of_cards:
                list_of_cards.insert(int(string_command[1]), string_command[2])
                print("Card successfully added")
            else:
                print("Card is already added")
        else:
            print("Index out of range")

print(", ".join(list_of_cards))

