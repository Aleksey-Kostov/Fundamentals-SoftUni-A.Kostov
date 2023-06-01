def calculates(products, quantity):
    coffee = 1.50
    water = 1.00
    coke = 1.40
    snacks = 2.00
    result = 0
    if products == "coffee":
        result = coffee * quantity
    elif products == "coke":
        result = coke * quantity
    elif products == "water":
        result = water * quantity
    elif products == "snacks":
        result = snacks * quantity
    return result


products_input = input()
quantity_input = int(input())
print(f"{calculates(products_input, quantity_input):.2f}")
