def is_edge(x, y, length):
    return 0 in (x, y) or length - 1 in (x, y)


def draw_square(length, symbol, is_solid):
    for i in range(length):
        for j in range(length):
            output = f'   '

            if is_edge(i, j, length) or is_solid:
                output = f'{symbol}  '

            print(output, end='')
        print()


draw_square(5, '$', False)


def find_min(a, b, c, d, e):
    return min(a, b, c, d, e)

def range_sum(start, end):
    return sum(range(start, end + 1))

import math

math.factorial()