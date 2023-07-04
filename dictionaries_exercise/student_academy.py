pair_of_rows = int(input())
student_dict = {}

for student in range(pair_of_rows):
    name_student = input()
    grade_student = float(input())
    if name_student not in student_dict.keys():
        student_dict[name_student] = []
    student_dict[name_student].append(grade_student)
for name, grade in student_dict.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")
