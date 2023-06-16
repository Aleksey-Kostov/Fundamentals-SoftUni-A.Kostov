collecting_items = input().split(", ")

command = input()

while command != "Craft!":
    list_command = command.split(" - ")
    if list_command[0] == "Collect":
        if list_command[1] not in collecting_items:
            collecting_items.append(list_command[1])
        else:
            continue
    elif list_command[0] == "Drop":
        if list_command[1] in collecting_items:
            collecting_items.remove(list_command[1])
    elif list_command[0] == "Combine Items":
        new_items = list_command[1].split(":")
        if new_items[0] in collecting_items:
            index_items = collecting_items.index(new_items[0])
            collecting_items.insert(index_items + 1, new_items[1])
    elif list_command[0] == "Renew":
        if list_command[1] in collecting_items:
            collecting_items.remove(list_command[1])
            collecting_items.append(list_command[1])
    command = input()


print(", ".join(collecting_items))
