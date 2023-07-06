username = input().split(", ")
len_name = False
is_num = False
counter = 0

for name in username:
    if 3 <= len(name) <= 16:
        len_name = True
    for char in range(len(name)):
        if name[char] == "_" or name[char] == "-" or name[char].isalnum():
            counter += 1
            if counter == len(name):
                is_num = True
    if len_name and is_num:
        print(name)
    counter = 0
    len_name = False
    is_num = False

