def function(count):
    if count <= 0:
        return

    function(count - 1)
    print(f'Hello! {count=}')

function(10)


def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

# 5! = 1 * 2 * 3 * 4 * 5

# 5! = 5 * 4!
# 0! = 1

# 5 ^ 3 = 5 * 5 * 5
# 5 ^ 3 = 5 * 5 ^ 2
# x ^ n = x * x ^ n - 1
# Степінь — power