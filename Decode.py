# by Seamus
def decode(encodedPass):
    decoded = ""
    encodedPass = str(encodedPass)
    for char in encodedPass:
        decoded += str(int(char) - 3)
    return decoded
