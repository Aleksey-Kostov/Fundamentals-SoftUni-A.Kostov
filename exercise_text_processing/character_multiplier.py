string = input().split()
total_sum = 0
sum_char_list1 = []
sum_char_list2 = []
current_char = 0

for character in range(len(string[0])):
    sum_char_list1.append(ord(string[0][character]))

for character in range(len(string[1])):
    sum_char_list2.append(ord(string[1][character]))

for char1 in range(len(sum_char_list2)):
    for char2 in range(char1, char1 + 1):
        if char1 in range(len(sum_char_list1)):
            total_sum += sum_char_list1[char1] * sum_char_list2[char2]

if len(sum_char_list1) > len(sum_char_list2):
    current_char = len(sum_char_list1) - len(sum_char_list2)
    for characters in sum_char_list1[-current_char:]:
        total_sum += characters
elif len(sum_char_list1) < len(sum_char_list2):
    current_char = len(sum_char_list2) - len(sum_char_list1)
    for characters in sum_char_list2[-current_char:]:
        total_sum += characters


print(total_sum)
