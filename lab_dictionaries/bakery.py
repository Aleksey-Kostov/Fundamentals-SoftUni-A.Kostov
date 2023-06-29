data_elements = input().split()
dictionary_products = {}

for elements in range(0, len(data_elements), 2):
    food_key = data_elements[elements]
    value = data_elements[elements + 1]
    dictionary_products[food_key] = int(value)

print(dictionary_products)
