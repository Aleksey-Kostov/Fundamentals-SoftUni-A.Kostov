user_input = input()
users_dict = {}

while user_input != "Lumpawaroo":
    if "->" in user_input:
        change_user = user_input.split(" -> ")
        name_user, side_user = change_user[0], change_user[1]
        if name_user in users_dict.values():
            users_dict[side_user] = [user for user in name_user if user != name_user]
        if side_user in users_dict.keys():
            if name_user not in users_dict[side_user]:
                users_dict[side_user].append(name_user)
    elif "|" in user_input:
        current_user = user_input.split(" | ")
        side, name = current_user[0], current_user[1]
        if side not in users_dict.keys():
            users_dict[side] = []
        users_dict[side].append(name)
    user_input = input()

print(users_dict)
