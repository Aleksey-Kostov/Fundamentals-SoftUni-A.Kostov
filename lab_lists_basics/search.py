number_n = int(input())
word = input()
string = []

for j in range(number_n):
    current_string = input()
    string.append(current_string)
print(string)

for j in range(len(string) - 1, -1, -1):
    elements = string[j]
    if word not in elements:
        string.remove(elements)
print(string)
