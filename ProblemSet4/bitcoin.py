import sys
import requests
import json

def main():
    if len(sys.argv) == 2:
        if not is_float(sys.argv[1]):
            sys.exit("Command-line argument is not number")
        request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data =request.json()
        rate_str = data["bpi"]["USD"]["rate"]
        rate_str = "".join(char for char in rate_str if char.isdigit() or char == ".")
        print(float(rate_str))
        amount =float(rate_str)* float(sys.argv[1])
        print(f"${amount:,.4f}")

    else:
        sys.exit("Missing commad-line argument")

def is_float(number):
    try:
        float(number)
        return True
    except ValueError:
        return False
    
if __name__ == "__main__":
    main()