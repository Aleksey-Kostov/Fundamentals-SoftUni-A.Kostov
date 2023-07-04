user_input = input()
users_dict = {}

while user_input != "Lumpawaroo":
    if "->" in user_input:
        change_user = user_input.split(" -> ")
        name_user, side_user = change_user[0], change_user[1]
        if side_user not in users_dict.keys():
            users_dict[side_user] = {name_user: 0}
        if name_user in users_dict[side_user].keys():
            users_dict[side_user][name_user] += 1
        if name_user not in users_dict[side_user].keys():
            del users_dict[name_user]
    elif "|" in user_input:
        current_user = user_input.split(" | ")
        side, name = current_user[0], current_user[1]
        if side not in users_dict.keys():
            users_dict[side] = {name: 0}
        users_dict[side][name] += 1
    user_input = input()

print(change_user)
print(current_user)
