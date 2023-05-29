money_for_beggars = input().split(", ")
money_for_each_beggars = []
count_of_beggars = int(input())
index = 0

while index < count_of_beggars:
    all_money_for_beggars = 0
    for current_index in range(index, len(money_for_beggars), count_of_beggars):
        all_money_for_beggars += int(money_for_beggars[current_index])
    money_for_each_beggars.append(all_money_for_beggars)
    index += 1


print(money_for_each_beggars)
