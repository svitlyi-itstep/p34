print(8 % 2)

a = 4

print(a / 2)

if a % 2 != 0:
    print('Непарне')
else:
    print('Парне')


if a % 2 == 0:
    print('Парне')
else:
    print('Непарне')


print('1. Sum')
print('2. Dif')

choice = input('Оберіть дію: ')
if choice == '1':
    print('Make SUM')
elif choice == '2':
    print('Make Dif')
else:
    print('Incorrect choice')


'''
message = input('Введіть повідомлення: ')

if len(message) > 0:
    print(f'Ваше повідомлення: {message}')
else:
    print('Ви нічого не ввели')
'''
'''
a = 9
b = 0


if b == 0:
    print('На нуль ділити не можна!')
    b = 1
else:
    print(f'{a} / {b} = {a / b}')


a = 9
b = 0

if b == 0:
    print('На нуль ділити не можна!')
    b = 1
    if b != 0:
        print(f'{a} / {b} = {a / b}')
'''
'''
    Програма запитує в користувача його вік. В залежності від відповіді
    програма має написати "повнолітній" або "неповнолітній".

    Особа вважається повнолітньою, якщо їй є повних 18 років.

    Діапазони віку:
    0-3 – Малюк
    4-11 — Дитина
    11-18 — Підліток
    18-59 — Дорослий
    60-120 — Пенсіонер
'''
'''
age = 2

if age >= 0 and age <=3:
    print('Малюк')

if 0 <= age <= 3:
    print('Малюк')
if 4 <= age <= 11:
    print('Дитина')


if age < 0:
    print('Некоректний вік')
elif age <= 3:
    print('Малюк')
elif age <= 11:
    print('Дитина')
else:
    print('Некоректний вік')
'''