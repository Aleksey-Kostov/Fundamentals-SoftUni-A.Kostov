messages = input()

command = input().split(":|:")
while command[0] != "Reveal":
    operation, *instructions = command
    if operation == "InsertSpace":
        index = int(instructions[0])
        messages = messages[:index] + " " + messages[index:]
        print(messages)
    elif operation == "Reverse":
        substring = instructions[0]
        if substring in messages:
            messages = messages.replace(substring, "", 1)
            messages = messages + substring[::-1]
            print(messages)
        else:
            print("error")
    elif operation == "ChangeAll":
        substring_change = instructions[0]
        replacement = instructions[1]
        messages = messages.replace(substring_change, replacement)
        print(messages)
    command = input().split(":|:")

print(f"You have a new text message: {messages}")
