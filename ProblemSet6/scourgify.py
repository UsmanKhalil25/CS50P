import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

reading_filename = sys.argv[1]
writing_filename = sys.argv[2]

if not reading_filename.endswith(".csv") or not writing_filename.endswith(".csv"):
    sys.exit("Not a CSV file")

students = []

try:
    with open(reading_filename,"r") as file:
        reader = csv.DictReader(file)
        for line in reader:
            last,first = line["name"].split(",")
            student = {"first":first,"last":last,"house":line["house"]}
            students.append(student)
except FileNotFoundError:
    sys.exit("File does not exist")

with open(writing_filename,"a") as file:
    writer = csv.DictWriter(file,fieldnames=["first","last","house"])
    for student in students:
        writer.writerow(student)
        