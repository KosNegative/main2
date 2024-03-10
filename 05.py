import csv
import random


with open("scientist.txt", encoding="utf-8") as file:   # Открываем файл
    reader = csv.DictReader(file, delimiter='#')    # Считываем
    reader = list(reader)

    nums = [n for n in range(1024)]
    random.shuffle(nums)

    for row in range(len(reader)):
        hashs = 0
        for let in reader[row]["ScientistName"]:
            hashs += nums[ord(let) % 1024]

        reader[row] = {'hash': hashs % 2048, "ScientistName": reader[row]["ScientistName"],
                       "preparation": reader[row]["preparation"], "date": reader[row]["date"],
                       "components": reader[row]["components"]}


with open("scientist_with_hash.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["hash", "ScientistName", "preparation", "date", "components"], delimiter="#")
    writer.writeheader()
    writer.writerows(reader)
