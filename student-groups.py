import csv
import random

# read names from the csv file
names = []

with open("students.txt", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        if row:
            names.append(row[0])

# shuffle the names into a random order
random.shuffle(names)

# ask the user for the desired group size
group_size = int(input("How many students per group? (2 or 3): "))

# create the groups
groups = []

for i in range(0, len(names), group_size):
    groups.append(names[i:i + group_size])

# if one student is left over, add them to the previous group
if len(groups) > 1 and len(groups[-1]) == 1:
    groups[-2].extend(groups[-1])
    groups.pop()

# display the groups
for number, group in enumerate(groups, start=1):
    print(f"\nGroup {number}")
    for student in group:
        print(f"  • {student}")