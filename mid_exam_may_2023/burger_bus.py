number_of_cities = int(input())
total_profit = 0

for city in range(1, number_of_cities + 1):
    name_of_the_city = input()
    money_earned = float(input())
    owner_expenses = float(input())
    current_profit = money_earned - owner_expenses
    if city % 5 == 0:
        current_profit -= 0.1 * money_earned
    elif city % 3 == 0:
        current_profit -= 0.5 * owner_expenses
    total_profit += current_profit
    print(f"In {name_of_the_city} Burger Bus earned {current_profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")
