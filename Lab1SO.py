import csv

kol_zapis = 0
bol_30 = 0
poisk = input('Введите автора: ')
with open('C:/Users/79218/Downloads/books.csv', newline='') as csvfile:
    vot = list(csv.reader(csvfile, delimiter=';'))
    for row in vot[1:]:
        kol_zapis += 1
        if len(row[1]) > 30:
            bol_30 += 1
        ishod = row[3].find(poisk)
        if poisk in row[3]:
            if float(row[7]) > 150:
                print(row[1])

print('\n''Кол-во записей в файле:', kol_zapis)
print('Строка "Название" длиннее 30:', bol_30)

with open('books.txt', 'w') as f:
    for i, note in enumerate(vot[100:120]):
        stroka = str(i + 1) + ' ' + note[3] + ' ' + note[1] + ' - ' + note[6][6:10] + '\n'
        f.write(stroka)
