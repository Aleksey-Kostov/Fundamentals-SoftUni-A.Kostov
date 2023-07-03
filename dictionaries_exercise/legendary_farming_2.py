item_dict = {"shards": 0, "fragments": 0, "motes": 0}
is_legendary = False
TARGET = 250

while True:
    item_input = input().split()
    for index in range(0, len(item_input), 2):
        quantity = int(item_input[index])
        material = item_input[index + 1].lower()
        if material not in item_dict:
            item_dict[material] = 0
        item_dict[material] += quantity
        if item_dict["shards"] >= TARGET:
            item_dict[material] -= TARGET
            print("Shadowmourne obtained!")
            is_legendary = True
            break
        elif item_dict["fragments"] >= TARGET:
            item_dict[material] -= TARGET
            print("Valanyr obtained!")
            is_legendary = True
            break
        elif item_dict["motes"] >= TARGET:
            item_dict[material] -= TARGET
            print("Dragonwrath obtained!")
            is_legendary = True
            break
    if is_legendary:
        break

for material, quantity in item_dict.items():
    print(f"{material}: {quantity}")
