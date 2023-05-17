quantity = int(input())
days = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights = 15

total_coast = 0
total_spirit = 0

for current_days in range(1, days + 1):
    if current_days % 11 == 0:
        quantity += 2
    if current_days % 2 == 0:
        total_coast += ornament_set_price * quantity
        total_spirit += 5
    if current_days % 3 == 0:
        total_coast += (tree_skirt_price + tree_garland_price) * quantity
        total_spirit += 13
    if current_days % 5 == 0:
        total_coast += tree_lights * quantity
        total_spirit += 17
        if current_days % 3 == 0:
            total_spirit += 30
    if current_days % 10 == 0:
        total_spirit -= 20
        total_coast += tree_skirt_price + tree_garland_price + tree_lights

if days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_coast}")
print(f"Total spirit: {total_spirit}")
