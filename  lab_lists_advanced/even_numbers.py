def even_number(list_number: list):
    even_number_list = []
    for index, number in enumerate(list_number):
        if int(number) % 2 == 0:
            even_number_list.append(index)
    return even_number_list


string_number = input().split(", ")
print(even_number(string_number))
