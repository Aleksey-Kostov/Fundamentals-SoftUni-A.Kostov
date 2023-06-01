def calculates(operator, number_1, number_2):
    result = 0
    if operator == "multiply":
        result = number_1 * number_2
    elif operator == "divide":
        result = int(number_1 / number_2)
    elif operator == "add":
        result = number_1 + number_2
    elif operator == "subtract":
        result = number_1 - number_2
    return result


input_operator = input()
num_1 = int(input())
num_2 = int(input())

print(calculates(input_operator, num_1, num_2))
