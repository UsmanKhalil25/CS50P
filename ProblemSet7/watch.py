import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(url):
    url = url.strip()
    matches = re.search(r"src=\"https?://(?:www\.)?youtube\.com/.+/([^\"]+)\"", url)
    try:
        return "https://youtu.be/" + matches.group(1)
    except AttributeError:
        pass

if __name__ == "__main__":
    main()
