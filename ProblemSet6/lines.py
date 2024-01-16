import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
filename =sys.argv[1]
if not filename.endswith(".py"):
    sys.exit("Not a python file")

try:
    file =open(filename,"r")
except FileNotFoundError:
    sys.exit("File does not exist")

number_of_rows = 0
for row in file:
    if len(row.lstrip()) > 0 and not row.lstrip().startswith("#"):
        number_of_rows +=1

print(number_of_rows)
file.close()