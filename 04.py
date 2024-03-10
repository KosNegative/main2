import csv
import random
from string import ascii_letters, digits


with open("scientist.txt", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter='#')
    reader = list(reader)
    for row in reader:
        author = row["ScientistName"].split()
        row["login"] = author[0] + "_" + author[1][0] + author[2][0]

        symb = ascii_letters + digits
        row["password"] = random.choices(symb, k=10)
        row["password"] = "".join(row["password"])


with open("scientist_password.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["ScientistName", "preparation", "date", "components",
                                              "login", "password"], delimiter="#")
    writer.writeheader()
    writer.writerows(reader)
