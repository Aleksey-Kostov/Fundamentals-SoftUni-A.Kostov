def length_is_valid(username_length):
    if 3 <= len(username_length) <= 16:
        return True
    return False


def characters_are_valid(username_char):
    for character in username_char:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True


def no_redundant_symbols(username_redundant):
    if " " in username_redundant:
        return False
    return True


def username_is_valid(username_valid):
    if length_is_valid(username_valid) and characters_are_valid(username_valid) and\
            no_redundant_symbols(username_valid):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if username_is_valid(username):
        print(username)
