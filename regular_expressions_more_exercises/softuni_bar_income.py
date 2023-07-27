import re

valid_order_dict = {}
total_price = 0
all_order = ""

order = input()
while order != "end of shift":
    all_order += order
    order = input()

pattern = r"\%([A-Z][a-z]+)\%[^\|\$\%\.]*?\<(\w+)\>[^\|\$\%\.]*?\|([0-9]+)\|[\w\-]*?([0-9.]+[0-9])(?=\$)"
matches = re.finditer(pattern, all_order)

for match in matches:
    product = match.group(2)
    count = int(match.group(3))
    price_product = float(match.group(4))
    t_price = count * price_product
    if match.group(1) not in valid_order_dict:
        valid_order_dict[match.group(1)] = [product]
        valid_order_dict[match.group(1)].append(t_price)
    else:
        valid_order_dict[match.group(1)].append(product)
        valid_order_dict[match.group(1)].append(t_price)

for k, v in valid_order_dict.items():
    customer_name = k
    if len(v) > 2:
        for index in range(len(v)):
            if index % 2 == 0:
                product = v[index]
                price = v[index + 1]
                total_price += float(price)
            else:
                continue
            print(f"{customer_name}: {product} - {float(price):.2f}")
    else:
        product = v[1]
        price = v[1]
        total_price += float(price)
        print(f"{customer_name}: {product} - {float(price):.2f}")
print(f"Total income: {total_price:.2f}")
