"""
Пользователь вводит неделю(четная или нечетная) и название предмета,
программа считывает расписание группы 18704.1 из файла table1.txt(четная неделя)
или из файла table2.txt(нечетная неделя)
и выводит количество пар по этому предмету на данной неделе
"""

import sys

amount = 0
print('Список предметов: Математический анализ, Программирование, Физическая культура, Английский язык,\n'
      'Основы веб-программирования, Микроэкономика, История, Информатика, Линейная алгебра')
week = input('Введите номер недели(1 - четная или 2 - нечетная): ')
try:
    int_week = int(week)
except ValueError:
    print('Значение {} не является целым числом'.format(week))
    sys.exit()
subject = input('Введите полное название предмета из списка предметов: ').lower()
if int_week == 1:
    with open('table1.txt') as f_in:
        for line in f_in:
            new_line = line.lower().strip()
            if new_line == subject:
                amount += 1
elif int_week == 2:
    with open('table2.txt') as f_in:
        for line in f_in:
            new_line = line.lower().strip()
            if new_line == subject:
                amount += 1
print('Количетсво пар по предмету "{}" на данной неделе: {}'.format(subject, amount))
