user_input = input()
users_dict = {}
is_here = False

while user_input != "Lumpawaroo":
    if "->" in user_input:
        change_user = user_input.split(" -> ")
        name_user, side_user = change_user[0], change_user[1]
        for side, user in users_dict.items():
            for name_users in user:
                if name_users == name_user:
                    users_dict[side].remove(name_users)
                    break
        if side_user in users_dict.keys():
            if name_user not in users_dict[side_user]:
                users_dict[side_user].append(name_user)
        elif side_user not in users_dict.keys():
            users_dict[side_user] = [name_user]
        print(f"{name_user} joins the {side_user} side!")
    elif "|" in user_input:
        current_user = user_input.split(" | ")
        side, name = current_user[0], current_user[1]
        if side not in users_dict.keys():
            users_dict[side] = []
        for k, v in users_dict.items():
            for old_name in v:
                if name in v:
                    is_here = True
                    break
        if not is_here:
            users_dict[side].append(name)
    user_input = input()

for key, value in users_dict.items():
    if len(value) != 0:
        print(f"Side: {key}, Members: {len(value)}")
    for force_user in value:
        print(f"! {force_user}")
