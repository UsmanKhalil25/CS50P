import sys

def main():
    fraction = input("Input: ")
    percentage =convert(fraction)
    fuel = gauge(percentage)
    print(f"Fuel: {fuel}")


def convert(fraction):
    try:
        x,y = fraction.split("/")
    except ValueError:
        sys.exit("Invalid Expression")

    try:
        x = int(x)
        y = int(y)
    except ValueError:
        sys.exit("X/Y must be intergers")
    if x > y:
        raise(ValueError("In X/Y, X is greater then Y"))
    try:
        return int(x/y * 100)
    except ZeroDivisionError:
        sys.exit("Division by zero")


def gauge(percentage):
    print(percentage)
    if percentage <=1:
        return "E"
    elif percentage >=99:
        return "F"
    else:
        return str(percentage)+"%"
    


if __name__ == "__main__":
    main()
