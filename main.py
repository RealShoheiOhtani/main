from Encode import encode
from Decode import decode

def main():
    while True:
        print("Menu", "-------------", "1. Encode", "2. Decode", "3. Quit", sep="\n")
        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            password = encode(password)
        elif option == "2":
            print(f"The encoded password is {password} and the original password is {decode(password)}")
        elif option == "3":
            break


if __name__ == "__main__":
    main()

