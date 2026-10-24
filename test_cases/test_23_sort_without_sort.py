import importlib

module = importlib.import_module("23_sort_without_sort")
sort_list = module.sort_list

def test_unsorted_list():
    assert sort_list([4, 2, 1, 3]) == [1, 2, 3, 4]

def test_already_sorted():
    assert sort_list([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_reverse_sorted():
    assert sort_list([4, 3, 2, 1]) == [1, 2, 3, 4]

def test_with_duplicates():
    assert sort_list([2, 1, 2, 3]) == [1, 2, 2, 3]

def test_empty_and_single_element():
    assert sort_list([]) == []
    assert sort_list([5]) == [5]