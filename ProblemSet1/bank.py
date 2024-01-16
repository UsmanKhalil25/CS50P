greeting = input("Greeting: ")
greeting = greeting.lower().strip()

firstWord = greeting.split(" ")

if firstWord[0].find("hello")!=-1:
    print("$0")
elif firstWord[0][0].find("h") !=-1:
    print("$20")
else:
    print("$100")

