import sys
from tabulate import tabulate
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")
try:
    file = open(filename,"r")
except FileNotFoundError:
    sys.exit("File does not exist")

content = []

for line in file:
    row = line.rstrip().split(",")
    content.append(row)


print(tabulate(content,tablefmt="grid"))

file.close()

