def main():
    ans = take_input()
    print("Adieu,adieu, to "+ans)

def take_input():
    list_of_names = []
    while True: 
        try:
            name = input("Name: ")
            list_of_names.append(name)
        except EOFError:
            break
    
    if len(list_of_names) ==1:
        return list_of_names[0]
    elif len(list_of_names) == 2:
        return list_of_names[0]+ " and " + list_of_names[1]
    else:
        to_return = ""
        for name in list_of_names[:-1]:
            to_return+= name+","
        to_return+=" and "+list_of_names[len(list_of_names)-1]
        return to_return
    
if __name__ == "__main__":
    main()