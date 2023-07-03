products = input().split()
products_dict = {}

while products[0] != "buy":
    product, price, quantity = products[0], float(products[1]), int(products[2])
    if product not in products_dict.keys():
        products_dict[product] = [price, quantity]
    else:
        products_dict[product][0] = price
        products_dict[product][1] += quantity
    products = input().split()

for product, item in products_dict.items():
    total_price = item[0] * item[1]
    print(f"{product} -> {total_price:.2f}")
