def data_type(data_input_first, data_input_second):
    if data_input_first == "int":
        result = int(data_input_second) * 2
        return result
    elif data_input_first == "real":
        result = float(data_input_second) * 1.5
        return f"{result:.2f}"
    elif data_input_first == "string":
        result = f"${data_input_second}$"
        return result


first_input = input()
second_input = input()
print(data_type(first_input, second_input))
