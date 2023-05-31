items_prices = input().split("|")
budget = int(input())
current_list = []
total_list = []
total_profit = 0
total_price = 0

for items in items_prices:
    list_items = items.split("->")
    string = list_items[0]
    price = float(list_items[1])
    total_list.append(price)
    if string == "Clothes" and 0 <= price <= 50:
        budget -= price
        current_list.append(budget)
    elif string == "Shoes" and 0 <= price <= 35:
        budget -= price
        current_list.append(budget)
    elif string == "Accessories" and 0 <= price <= 20.50:
        budget -= price
        current_list.append(budget)
    else:
        continue
    if 0 > budget:
        current_list.remove(budget)
        budget += price
        break
    profit_price = 0.4 * price
    total_profit += profit_price
    price += profit_price
    total_price += price
    print(f"{price:.2f}", end=" ")

print(f"\nProfit: {total_profit:.2f}")
new_budget = min(current_list) + total_price
if new_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
