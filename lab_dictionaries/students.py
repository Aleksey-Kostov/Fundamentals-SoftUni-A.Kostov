student_dict = {}
students_list = []
new = {}

while True:
    student = input()
    if student in student_dict.values():
        print("A")
    if ":" not in student:
        break
    new_students = student.split(":")
    students_list += new_students
    for i in range(len(new_students)):
        key = new_students[i]
        value = new_students[i + 1]
        student_dict[key] = value
    for j in range(len(new_students)):
        key_3 = new_students[j + 2]
        value = student_dict

print(student_dict)
