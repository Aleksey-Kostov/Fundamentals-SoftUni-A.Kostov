number_of_companions = int(input())
days = int(input())

total_coins = 0

for current_days in range(1, days + 1):
    if current_days % 10 == 0:
        number_of_companions -= 2
    if current_days % 15 == 0:
        number_of_companions += 5
    if current_days % 3 == 0:
        total_coins -= 3 * number_of_companions
    if current_days % 5 == 0:
        total_coins += 20 * number_of_companions
        if current_days % 3 == 0:
            total_coins -= 2 * number_of_companions
    total_coins += 50
    total_coins -= 2 * number_of_companions

coins_per_companions = total_coins // number_of_companions
print(f"{number_of_companions} companions received {coins_per_companions} coins each.")
