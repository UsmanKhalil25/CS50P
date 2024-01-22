import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert_util(h, m, p):
    if m is None:
        m = ":00"

    if p == "AM":
        if h == "12":
            return "00" + m
        else:
            return "0" + h  + m if int(h) < 10 else h + m
    elif p == "PM":
        if h == "12":
            return h + m
        else:
            return str(int(h) + 12) + m

def convert(s):
    s = s.strip()
    if matches := re.search(r"^([0-9]?[0-9])(:[0-9][0-9])? (AM|PM) to ([0-9]?[0-9])(:[0-9][0-9])? (AM|PM)$",s,re.IGNORECASE):
        hour1 = matches.group(1)
        minutes1 = matches.group(2)
        period1  = matches.group(3)

        hour2 = matches.group(4)
        minutes2 = matches.group(5)
        period2  = matches.group(6)
        return convert_util(hour1,minutes1,period1)+" to "+convert_util(hour2,minutes2,period2)


if __name__ == "__main__":
    main()
