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
        key_2 = new_students[i + 2]
        student_dict[key] = value
        new[key_2] = value
        student_dict += new
        break

print(student_dict)
