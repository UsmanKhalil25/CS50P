def main():
    string = input("Input: ")
    print(shorten(string))


def shorten(string):
    vowels = ["A","a","E","e","I","i","O","o","U","u"]
    return "".join(char for char in string if not char in vowels)

if __name__ == "__main__":
    main()
