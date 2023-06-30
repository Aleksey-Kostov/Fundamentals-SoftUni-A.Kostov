words = input().split()
words_dict = {}

for word in words:
    new_item = word.lower()
    if new_item not in words_dict:
        words_dict[new_item] = 0
    words_dict[new_item] += 1

for key, value in words_dict.items():
    if value % 2 != 0:
        print(key, end=" ")

