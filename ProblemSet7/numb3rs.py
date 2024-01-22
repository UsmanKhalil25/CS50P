import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip = ip.strip()
    matches = re.search(r"^([0-9]?[0-9]?[0-9])\.([0-9]?[0-9]?[0-9])\.([0-9]?[0-9]?[0-9])\.([0-9]?[0-9]?[0-9])$",ip)
    try:
        if 0<= int(matches.group(1))<=255 and 0<= int(matches.group(2))<=255 and 0<= int(matches.group(3))<=255 and 0<= int(matches.group(4))<=255:
            return True
        else:
            return False
    except AttributeError:
        return False
if __name__ == "__main__":
    main()
