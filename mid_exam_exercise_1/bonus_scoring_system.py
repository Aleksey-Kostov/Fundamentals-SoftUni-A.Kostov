from math import ceil
number_of_student = int(input())
number_of_the_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
attendance = 0

for student in range(number_of_student):
    attendance_of_student = int(input())
    total_bonus = attendance_of_student / number_of_the_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        attendance = attendance_of_student

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {attendance} lectures.")
