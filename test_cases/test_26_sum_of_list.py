import importlib

module = importlib.import_module("26_sum_of_list")
sum_list = module.sum_list

def test_positive_numbers():
    assert sum_list([1, 2, 3, 4, 5]) == 15

def test_mixed_numbers():
    assert sum_list([-2, 5, -1, 3]) == 5

def test_empty_list_returns_zero():
    assert sum_list([]) == 0

def test_single_element():
    assert sum_list([42]) == 42