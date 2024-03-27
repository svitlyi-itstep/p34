import random

def show_list(list):
    for item in list:
        print(item, end=', ')

marks = [random.randint(1, 12) for i in range(10)]

marks += [10]
marks.append(8)
marks.extend([7, 6, 8, 9])
marks.extend([2, 3, 4, 3, 2, 1])

while marks.count(10):
    marks.remove(10)

print('Marks: ', end='')
show_list(marks)
print('\b\b. ')

print('\nMarks: ', end='')
for i in range(len(marks)):
    print(marks[i], end=', ')
print('\b\b. ')

print('Bad marks: ', end='')
for mark in marks:
    if mark < 4:
        print(mark, end=', ')
print('\b\b. ')

double_marks = [ mark for mark in marks if mark >= 9 ]

print('Double marks: ', end='')
for mark in double_marks:
    print(mark, end=', ')
print('\b\b. ')

'''
    Написати програму, яка дозволяє користувачу вводити оцінки до тих пір, доки користувач
    не введе 0. Після введення нуля програма має вивести на екран всі введені оцінки.
'''

statement = '23+12'
if '+' in statement:
    print(sum([int(num) for num in statement.split('+')]))
