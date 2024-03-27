# print(list(range(5)))
#
# for i in range(5):
#    # Тело цикла
#    # i - переменная-счётчик
#
#    print(f"Hello #{i}")


# for letter in "Hello world!":
#    print(letter.upper())


# message = ''
#
# while message != 'quit':
#     message = input('Enter message: ')
# else:
#     print('Goodbye!')

# for val in "строка":
#    if val == "о":
#        continue
#    print(val)
#
# print("Конец")


a = int(input('Введіть нижню границю діапазона:'))
b = int(input('Введіть верхню границю діапазона:'))

if a > b:
    a, b = b, a

if a % 2 == 0:
    a += 1
# a += int(not a % 2)

for num in range(a, b + 1, 2):
   print(num)

numbers = [6, 2, 0, 4, 7, 12]

for number in range(10):
    number *= 2
    print(number, end=" ")


a = 0

while True:
    print('Hello!')
    a += 1
    if not a < 5:
        break