def main():
    items = get_items()
    for item in sorted(items.keys()):
        print(items[item],item) 

def get_items():
    items = {}
    while True:
        try:
            item = input()
            item = item.upper()
            if items.get(item) !=None:
                items[item]+=1
            else:
                items.__setitem__(item,1)
        except EOFError:
            return items
        except KeyError:
            pass

main()
