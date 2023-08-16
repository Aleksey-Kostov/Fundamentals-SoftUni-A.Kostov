string = input().split(", ")
list_of_sheep = []
index_wolf = 0
number_of_sheep = 0

for animal in string:
    if animal == "sheep":
        list_of_sheep.append(animal)
        number_of_sheep = len(list_of_sheep)
    elif animal == "wolf":
        index_wolf = string.index(animal)

if index_wolf == 0:
    print(f"Oi! Sheep number {number_of_sheep}! You are about to be eaten by a wolf!")
else:
    print("Please go away and stop eating my sheep")
