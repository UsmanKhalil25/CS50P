def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s)<2:
        return False
    if not s[0:len(s)].isalnum() or not s[0:2].isalpha():
        return False
    number = "".join(char for char in s if char.isdigit())
    position = s.find(number)
    if len(number)!=0 and (position+ len(number) != len(s) or number.startswith("0") ):
        return False
    return True


if __name__ == "__main__":
    main()