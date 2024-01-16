def convert(string):
    string = string.replace(":)","🙂")
    string = string.replace(":(","🙁")
    return string

def main():
    string = input()
    print(convert(string))

main()
                            