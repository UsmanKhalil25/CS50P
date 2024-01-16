def main():
    camel_case = input("camelCase: ")
    print(convert_into_snake_case(camel_case))

def convert_into_snake_case(word):
    ans =""
    for i in range(len(word)):
        if word[i].isupper():
            ans = ans +"_"+ word[i].lower()
        else:
            ans = ans+ word[i]
    return ans

main()