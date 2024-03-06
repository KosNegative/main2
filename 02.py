import csv
import random


def quicksort(n):
    if len(n) <= 1:
        return n
    else:
        l_list = []
        m_list = []
        r_list = []
        q = random.choice([x for x in n])
        for a in n:
            if a["date"] < q["date"]:
                l_list.append(a)
            elif a["date"] > q["date"]:
                r_list.append(a)
            else:
                m_list.append(a)
        return quicksort(l_list) + m_list + quicksort(r_list)


with open("scientist.txt", encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='#'))

    reader = quicksort(reader)

with open("scientist.txt", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=['ScientistName', 'preparation', 'date', 'components'], delimiter="#")
    writer.writeheader()
    writer.writerows(reader)
