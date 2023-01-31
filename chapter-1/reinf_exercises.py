from functools import reduce
from random import randrange

# 1.1
def is_multiple(n: int, m: int) -> bool:
    """Determines if n is a multiple of m.

    Args:
        n (int): tested number
        m (int): number which is tested against
    """
    if m % n == 0:
        return True
    return False


# 1.2
def is_even(k: int) -> bool:
    even = ["0", "2", "4", "6", "8"]
    num_str = str(k)
    if num_str[-1] in even:
        return True
    return False


# 1.3
def minmax(data: list[int]) -> tuple[int, int]:
    data.sort()
    return (data[0], data[-1])


# 1.4, R1.5
def sum_pos_squares(n: int) -> int:
    to_calculate = range(n, 0, -1)
    return reduce(lambda x, y: x + y * y, to_calculate, 0)


# 1.6, 1.7
def sum_pos_odd_squares(n: int) -> int:
    if n % 2 == 0:
        to_calculate = range(n - 1, 0, -2)
    else:
        to_calculate = range(n, 0, -2)
    return reduce(lambda x, y: x + y * y, to_calculate, 0)


# 1.8
# Just asks for an understanding that positive list indices
# have an equivalent negative index

# 1.9
def range_demo_one() -> list[int]:
    return list(range(50, 81, 10))


# 1.10
def range_demo_two():
    return list(range(8, -9, -2))


# 1.11
def list_comp_one():
    return [pow(2, n) for n in range(9)]


# 1.12
def choice(data: list):
    index = randrange(0, len(data), 1)
    return data[index]
