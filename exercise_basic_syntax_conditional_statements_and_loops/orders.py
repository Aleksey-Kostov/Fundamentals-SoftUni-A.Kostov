orders_number = int(input())

total_price = 0

for _ in range(orders_number):
    price_capsule = float(input())
    days = int(input())
    capsules_number = int(input())
    if 0.01 <= price_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_number <= 2000:
        price = price_capsule * days * capsules_number
        total_price += price
        print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total_price:.2f}")
