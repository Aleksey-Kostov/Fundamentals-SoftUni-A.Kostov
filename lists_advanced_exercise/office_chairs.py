def check_chairs(number_rooms):
    total_diff_chair = 0
    total_diff_free_chairs = 0
    for room in range(1, number_rooms + 1):
        number_of_chairs = input().split()
        for character in number_of_chairs:
            counter_free_chairs = len(number_of_chairs[0])
            number_of_visitors = int(number_of_chairs[1])
            diff_free_chairs = counter_free_chairs - number_of_visitors
            if diff_free_chairs < 0 and character[0]:
                print(f"{abs(diff_free_chairs)} more chairs needed in room {room}")
                total_diff_free_chairs += abs(diff_free_chairs)
                break
            else:
                total_diff_chair += diff_free_chairs
                break
    return total_diff_chair, total_diff_free_chairs


number_of_rooms = int(input())
free_chairs, needed_chairs = check_chairs(number_of_rooms)
if free_chairs >= needed_chairs:
    print(f"Game On, {free_chairs} free chairs left")
