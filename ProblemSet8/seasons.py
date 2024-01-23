import sys
import inflect
from datetime import date


def input_date():
    return input("Date of Birth: ").strip()


def get_minutes(string):
    try:
        date_of_birth = date.fromisoformat(string)
    except ValueError:
        sys.exit("Invalid date")
    current_date = date.today()
    total = current_date - date_of_birth
    minutes = total.days * 60 * 24
    p = inflect.engine()
    return p.number_to_words(minutes,andword="")


def main():
    date_of_birth = input_date()
    print(get_minutes(date_of_birth))


if __name__ == "__main__":
    main()
