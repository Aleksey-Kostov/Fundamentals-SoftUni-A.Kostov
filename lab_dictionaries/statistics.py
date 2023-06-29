list_products = []
item_dict = {}

while True:
    product = input()
    if ":" not in product:
        break
    new_product = product.split(": ")
    list_products += new_product

for item in range(0, len(list_products), 2):
    key = list_products[item]
    value = list_products[item + 1]
    if key in item_dict:
        item_dict[key] += int(value)
    else:
        item_dict[key] = int(value)

print("Products in stock:")
for key, value in item_dict.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(item_dict)}")
print(f"Total Quantity: {sum(item_dict.values())}")
