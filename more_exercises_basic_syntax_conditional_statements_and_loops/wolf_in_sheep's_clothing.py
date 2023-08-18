string = input().split(", ")
list_of_sheep = []
index_wolf = 0
number_of_sheep = 0
flag = False

for i in range(len(string))[::-1]:
    if string[i] == "sheep":
        number_of_sheep += 1
        flag = True
    elif string[i] == "wolf":
        break

if flag:
    print(f"Oi! Sheep number {number_of_sheep}! You are about to be eaten by a wolf!")
else:
    print("Please go away and stop eating my sheep")

