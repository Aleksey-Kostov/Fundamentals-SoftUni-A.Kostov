single_string = input()
main_index = []

for i in range(len(single_string)):
    if single_string[i].isupper():
        main_index.append(i)

print(main_index)
