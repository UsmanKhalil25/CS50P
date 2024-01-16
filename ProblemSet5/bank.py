def main():
    greeting = input("Greeting: ")

def value(greeting):
    greeting = greeting.lower().strip()
    firstWord = greeting.split(" ")
    if firstWord[0].find("hello")!=-1:
        return 0
    elif firstWord[0][0].find("h") !=-1:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()