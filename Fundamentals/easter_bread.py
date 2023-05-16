budget = float(input())
price_flour = float(input())

current_eggs_count = 0

price_pack_eggs = 0.75 * price_flour
price_one_liter_milk = 1.25 * price_flour

current_price = price_flour + price_pack_eggs + (0.25 * price_one_liter_milk)
total_bread_count = budget // current_price

for num in range(1, int(total_bread_count) + 1):
    current_eggs_count += 3
    if num % 3 == 0:
        current_eggs_count -= num - 2

total_price = current_price * total_bread_count
money_left = budget - total_price

print(f"You made {total_bread_count:.0f} loaves of Easter bread!"
      f" Now you have {current_eggs_count:.0f} eggs and {money_left:.2f}BGN left.")
