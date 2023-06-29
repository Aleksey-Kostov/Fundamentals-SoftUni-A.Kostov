products = input().split()
given_products = input().split()

dictionary_product = {}

for i in range(0, len(products), 2):
    key = products[i]
    value = products[i + 1]
    dictionary_product[key] = value
for item in given_products:
    if item in dictionary_product:
        print(f"We have {dictionary_product[item]} of {item} left.")
    else:
        print(f"Sorry, we don't have {item}.")
