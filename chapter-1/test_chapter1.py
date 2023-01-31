from reinf_exercises import (
    is_multiple,
    is_even,
    minmax,
    sum_pos_squares,
    sum_pos_odd_squares,
    range_demo_one,
    range_demo_two,
    list_comp_one,
)

# Reinforcement tests
def test_is_multiple():
    assert is_multiple(5, 10) == True
    assert is_multiple(10, 5) == False
    assert is_multiple(3, 4) == False


def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(100) == True
    assert is_even(101) == False


def test_min_max():
    assert minmax([1, 2, 3, 4, 5]) == (1, 5)


def test_sum_pos_squares():
    assert sum_pos_squares(5) == 55
    assert sum_pos_squares(6) == 91


def test_sum_pos_odd_squares():
    assert sum_pos_odd_squares(5) == 35
    assert sum_pos_odd_squares(6) == 35
    assert sum_pos_odd_squares(7) == 84


def test_range_one():
    assert range_demo_one() == [50, 60, 70, 80]


def test_range_two():
    assert range_demo_two() == [8, 6, 4, 2, 0, -2, -4, -6, -8]


def test_list_comp():
    assert list_comp_one() == [1, 2, 4, 8, 16, 32, 64, 128, 256]


# Creativity tests
