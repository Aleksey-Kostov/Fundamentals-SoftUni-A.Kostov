def time_needed(student_number, student_sum: int):
    from math import ceil
    needed_student_per_hour = student_sum
    total_needed_time = student_number / needed_student_per_hour
    if total_needed_time >= 4 and total_needed_time % 3 != 0:
        total_needed_time += total_needed_time // 3
    elif total_needed_time >= 4 and total_needed_time % 3 == 0:
        total_needed_time += total_needed_time / 3 - 1
    return ceil(total_needed_time)


first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
students_count = int(input())
sum_student = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
print(f"Time needed: {time_needed(students_count, sum_student)}h.")
