from pyfiglet import Figlet
import sys


string = input("Input: ")
if len(sys.argv) == 1:
    f = Figlet()
    print(f.renderText(string))
elif len(sys.argv) == 3:
    font = sys.argv[2]
    f =Figlet(font = font)
    print(f.renderText(string))
    