def check_password(password):
    correct_password = "XoT@4kD5"
    if password == correct_password:
        return True
    return False

def brute_force(password_list):
    for password in password_list:
        print("Checking password: {password}")
        if check_password(password):
            print("ACCESS GRANTED! Password is {password}")
            return password
    print("ACCED DENIED! Password is not found!")
    return None

with open('passwords.txt', 'r') as file:
    passwords = file.readlines()

passwords = [password.strip()for password in passwords]

brute_force(passwords)


