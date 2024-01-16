def main():
    print(get_input("Fraction: "))

def get_input(prompt):
    while True:
        try:
            fraction = input(prompt)
            x,y = map(int,fraction.split("/"))
            if x == y:
                return "F"
            elif x == 0:
                return "E"
            else:
                return str(round(x/y * 100))+ "%" 
               
            
        except (ValueError,ZeroDivisionError):
            pass

main()