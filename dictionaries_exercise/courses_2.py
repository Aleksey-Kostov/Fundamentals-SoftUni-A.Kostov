courses = input().split(" : ")
courses_dict = {}

while courses[0] != "end":
    name, course = courses[1], courses[0]
    if course not in courses_dict.keys():
        courses_dict[course] = [name]
    else:
        courses_dict[course].append(name)
    courses = input().split(" : ")

for course, names in courses_dict.items():
    print(f"{course}: {len(names)}")
    for name in names:
        print(f"-- {name}")
