
name_for_sorting = input().split(", ")
sorting_list = sorted(name_for_sorting, key=lambda x: (-len(x), x))

print(sorting_list)
