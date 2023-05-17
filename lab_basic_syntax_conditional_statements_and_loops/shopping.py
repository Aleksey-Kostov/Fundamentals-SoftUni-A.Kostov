budget = int(input())
products = input()

total_sum = 0

while products != "End":
    total_sum += int(products)
    if total_sum > budget:
        print("You went in overdraft!")
        break
    products = input()

else:
    print("You bought everything needed.")
