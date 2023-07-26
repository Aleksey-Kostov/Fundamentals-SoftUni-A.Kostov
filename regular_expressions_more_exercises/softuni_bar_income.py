import re

valid_order_dict = {}
total_price = 0
all_order = ""

order = input()
while order != "end of shift":
    all_order += order
    order = input()

pattern = r"%([A-Z][a-z]+)\%[^\|\$\%\.]*?\<(\w+)\>[^\|\$\%\.]*?\|([0-9]+)\|[\w\-]*?([0-9.]+[0-9])(?=\$)"
matches = re.finditer(pattern, all_order)

for match in matches:
    product = match.group(2)
    count = int(match.group(3))
    price_product = float(match.group(4))
    if count > 0:
        valid_order_dict[match.group(1)] = {product: count * price_product}

for k, v in valid_order_dict.items():
    customer_name = k
    for key, value in v.items():
        product = key
        price = value
        total_price += price
        print(f"{customer_name}: {product} - {price:.2f}")
print(f"Total income: {total_price:.2f}")
