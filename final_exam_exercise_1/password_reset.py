string = input()
command = input().split()


def take_odd(text):
    new_text = ""
    for index in range(len(text)):
        if index % 2 != 0:
            new_text += text[index]
    return new_text


def cut(text, index, length):
    end_index = int(index) + int(length)
    new_text = ""
    for i in range(len(text)):
        if i in range(int(index), end_index):
            continue
        else:
            new_text += text[i]
    return new_text


def substitute(text, given_substring, substring_for_replace):
    if given_substring in text:
        new_text = text.split(given_substring)
        new_text = f"{substring_for_replace}".join(new_text)
        return new_text
    else:
        return "Nothing to replace!"


while command[0] != "Done":
    if command[0] == "TakeOdd":
        string = take_odd(string)
        print(string)
    elif command[0] == "Cut":
        string = cut(string, command[1], command[2])
        print(string)
    elif command[0] == "Substitute":
        subs = substitute(string, command[1], command[2])
        if subs != "Nothing to replace!":
            string = subs
            print(string)
        else:
            print(subs)
    command = input().split()

print(f"Your password is: {string}")
