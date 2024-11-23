import csv
data = [["name", "age", "city"],["John", 30, "New York"], ["Mike", 25, "Chicago"]]

with open("./data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open("./data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)