import csv

with open("scientist.txt", encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='#'))
    autors = []
    prep = []
    was = False

    reader.sort(key=lambda x: x["date"])
    print("Разработчиками Аллопуринола были такие люди")

    for row in reader:
        if row["preparation"] not in prep:
            prep.append(row["preparation"])
            autors.append(row)
        if row["preparation"] == "Аллопуринол":
            print(f"{row['ScientistName']} - {row['date']}")
            if not was:
                name = row['ScientistName']
                was = True
    print(f"‘Оригинальный рецепт принадлежит: {name}")

with open("scientist_origin.txt", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=['ScientistName', 'preparation', 'date', 'components'], delimiter="#")
    writer.writeheader()
    writer.writerows(autors)
