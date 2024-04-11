from Encode import encode


def main():
    while True:
        print("Menu", "-------------", "1. Encode", "2. Decode", "3. Quit", sep="\n")
        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            password = encode(password)

        elif option == "2":
            pass

        elif option == "3":
            break


if __name__ == "__main__":
    main()

