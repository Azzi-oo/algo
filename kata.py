def alphanumeric(password):
    if password == "":
        return False

    for char in password:
        if not char.isalnum():
            return False

    return True
