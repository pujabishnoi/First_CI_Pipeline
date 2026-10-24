import importlib

module = importlib.import_module("25_max_min_list")
find_max_min = module.find_max_min

def test_normal_list():
    assert find_max_min([3, 1, 9, 4, 7, 2]) == (9, 1)

def test_negative_numbers():
    assert find_max_min([-5, -1, -10, -2]) == (-1, -10)

def test_single_element():
    assert find_max_min([42]) == (42, 42)

def test_empty_list():
    assert find_max_min([]) == (None, None)