def loading_bar(number):
    if number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    if number != 100:
        percent_number = number // 10
        percent_point = 10 - percent_number
        return f"{number}% [{'%' * percent_number}{'.' * percent_point}]\nStill loading..."


percent = int(input())
print(loading_bar(percent))
