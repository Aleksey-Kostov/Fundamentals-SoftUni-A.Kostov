def password_validation(password):
    is_valid = True
    if len(password) not in range(6, 11):
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not password.isalnum():
        is_valid = False
        print("Password must consist only of letters and digits")
    counter_of_digit = 0
    for characters in password:
        if characters.isdigit():
            counter_of_digit += 1
    if counter_of_digit < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    return is_valid


password_input = input()
password_is_valid = password_validation(password_input)
if password_is_valid:
    print(f"Password is valid")
