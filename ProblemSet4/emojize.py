from emoji import emojize
def main():
    string = input("Input: ")
    if "_" in string:
        print("Output:",emojize(string))
    else:
        print("Output:", emojize(string,language="alias"))

if __name__ == "__main__":
    main()
