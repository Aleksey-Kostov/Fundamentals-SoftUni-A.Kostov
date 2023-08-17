sequence_of_numbers = [numbers for numbers in input().split()]
string = input()
list_sum = []
index_list = []
new_string = []
total_string = []

for number in sequence_of_numbers:
    for num in number:
        list_sum.append(int(num))
    index_list.append(sum(list_sum))
    list_sum.clear()
for i in range(len(string)):
    new_string.append(string[i])
for j in index_list:
    if j < len(new_string):
        real_string = new_string.pop(j)
        total_string.append(real_string)
    else:
        real_string = (new_string + new_string).pop(j)
        new_string.remove(real_string)
        total_string.append(real_string)

print("".join(total_string))

