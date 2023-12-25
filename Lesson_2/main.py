a = int(input('Введіть перше число:'))
b = int(input('Введіть друге число:'))

print(a + b)
print()


'''
    Введіть перше число: 2
    Введіть друге число: 3
    
    2 + 3 = 5
    2 - 3 = -1
    
    ----------------------------------------------------------
    
    Задані моменти початку і кінця деякого проміжку часу в годинах, хвилинах і 
    секундах (в межах доби). Знайти тривалість цього проміжку в 
    кожній з перелічених одиниць.
 
    Наприклад:
    Введіть початкову годину: 10 (10 * 3600)
    Введіть початкову хвилину: 15 (15 * 60)
    Введіть початкову секунду: 34
     
    Введіть кінцеву годину: 13
    Введіть кінцеву хвилину: 10
    Введіть кінцеву секунду: 47
     
    Різниця між введеними моментами часу: 2 години 55 хвилин 13 секунди
    Різниця між введеними моментами часу: 10513  секунди
'''

start_hours = 10
start_min = 15
start_sec = 34
end_hours = 13
end_min = 14
end_sec = 21

result_sec = end_sec - start_sec + 60
result_min = (end_min - 1 + result_sec // 60) - start_min + 60
result_hours = (end_hours - 1 + result_min // 60) - start_hours
result_sec %= 60
result_min %= 60

print('Start:\t', start_hours, ':', start_min, ':', start_sec)
print('End:\t', end_hours, ':', end_min, ':', end_sec)
print('Diff:\t', result_hours, ':', result_min, ':', result_sec)