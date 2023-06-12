def recoding_messages(input_message: list):
    list_string_digit = []
    for message in input_message:
        for digit in range(len(message)):
            while message[digit].isdigit():
                list_string_digit.append(message[digit])
                message.pop(0)
            number = int(" ".join(list_string_digit))
            input_message.index(0, chr(number))

    return input_message


secret_messages = input().split()
print(recoding_messages(secret_messages))

