def show_sum(a, b):
    print(f'{a} + {b} = {a + b}')

def count_dif(a, b):
    return a - b

def count_div(a, b):
    if b == 0:
        return None
    return a / b


# ============

a = int(input('Введіть перше число: '))
b = int(input('Введіть перше число: '))

print(show_sum(a, b))
print(f'{count_dif(a, b)=}')
show_sum(7, 13)
show_sum(0, 0)

'''
    За прикладом функції show_sum створити аналогічні функції для операцій мінус, помножити і поділити.
    ДЛЯ КОЖНОЇ ОПЕРАЦІЇ МАЄ БУТИ СВОЯ ФУНКЦІЯ. Реалізувати введення користувачем двох чисел і викликати всі
    функції, підставивши введені користувачем дані у кожну функцію.
'''

length = 5
symbol = '@'
direction = 'h'

number = 123456
digits = [int(i) for i in str(number)]
