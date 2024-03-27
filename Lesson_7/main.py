'''

    Рік високосний, якщо:
    - кратний 400
    - не кратний 100
    - кратний 4

'''

year = 2023

if not year % 400:
    print('Рік високосний')
elif year % 100:
    if not year % 4:
        print('Рік високосний')
    else:
        print('Рік не високосний')
else:
    print('Рік не високосний')


if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    print('Рік високосний')
else:
    print('Рік не високосний')