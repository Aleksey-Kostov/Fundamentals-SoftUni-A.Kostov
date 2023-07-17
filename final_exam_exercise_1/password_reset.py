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
    new_text = ""
    if given_substring in text:
        for character in text:
            if character == given_substring or given_substring == character + character:
                new_text += substring_for_replace
            else:
                new_text += character
        return new_text
    return "Nothing to replace!"


while command != "Done":
    if command[0] == "TakeOdd":
        string = take_odd(string)
        print(string)
    elif command[0] == "Cut":
        string = cut(string, command[1], command[2])
        print(string)
    elif command[0] == "Substitute":
        string = substitute(string, command[1], command[2])
        print(string)
    command = input().split()
