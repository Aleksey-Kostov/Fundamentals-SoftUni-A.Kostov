numbers = int(input())

for _ in range(numbers):
    name_string = input()
    flag = True
    for characters in name_string:
        if characters == "." or characters == "," or characters == "_":
            print(f"{name_string} is not pure!")
            flag = False
            break
    if flag:
        print(f"{name_string} is pure.")