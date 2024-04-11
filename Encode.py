def encode(password):
    new_password = 0
    for i in password:
        new_password = new_password*10 + int(i)

    return str(new_password)