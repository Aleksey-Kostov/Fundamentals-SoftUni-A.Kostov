receive_the_gifts = input().split()
list_gifts = []
command = ""

while command != "No Money":
    command = input()
    list_gifts = command.split()
    index = 0
    if "OutOfStock" in list_gifts:
        gift = list_gifts[1]
        while gift in receive_the_gifts:
            index = receive_the_gifts.index(gift)
            receive_the_gifts[index] = "None"
        list_gifts.clear()
    elif "Required" in list_gifts:
        index = int(list_gifts[2])
        receive_the_gifts[index - 1] = list_gifts[1]
        list_gifts.clear()
    elif "JustInCase" in list_gifts:
        receive_the_gifts[-1] = list_gifts[1]
        list_gifts.clear()

while "None" in receive_the_gifts:
    receive_the_gifts.remove("None")
print(*receive_the_gifts, sep=" ")

