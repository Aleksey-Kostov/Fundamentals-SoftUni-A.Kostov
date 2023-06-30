student_dict = {}
students_list = []
course_student = ""

while True:
    student = input()
    course_student = student
    if ":" not in student:
        break
    new_students = student.split(":")
    students_list += new_students
    for i in range(0, len(new_students), 3):
        name = new_students[i]
        id_name = new_students[i + 1]
        course = new_students[i + 2]
        student_dict[name] = {course: id_name}

for name_student, course_id in student_dict.items():
    for course_only, id_only in course_id.items():
        if course_only.startswith(course_student[:4]):
            print(f"{name_student} - {id_only}")
