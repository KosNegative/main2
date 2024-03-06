import csv

with open('scientist.txt', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='#')
    reader = list(reader)
    request = input()
    while request != 'эксперимент':

        request = request.split('.')
        request = request[::-1]
        request = '-'.join(request)
        left = 0
        right = len(reader) - 1
        while left <= right:
            mid = (left + right) // 2
            if request == reader[mid]['date']:
                autor = reader[mid]
                name = autor['ScientistName'].split()
                print(f'Ученый {name[0]} {name[1][0]}.{name[2][0]}.'
                      f' создал препарат: {autor["preparation"]} - {autor["date"]}')
                break
            if request > reader[mid]['date']:
                left = mid + 1
            else:
                right = mid - 1

        request = input()