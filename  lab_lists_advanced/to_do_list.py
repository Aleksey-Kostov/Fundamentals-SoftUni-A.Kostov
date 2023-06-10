def sorted_notes():
    result = []
    to_do_list = [0] * 10
    while True:
        to_do_notes = input()
        if to_do_notes == "End":
            break
        tokens = to_do_notes.split("-")
        priority = int(tokens[0]) - 1
        note = tokens[1]
        to_do_list.pop(priority)
        to_do_list.insert(priority, note)
        result = [note for note in to_do_list if note != 0]
    return result


print(sorted_notes())
