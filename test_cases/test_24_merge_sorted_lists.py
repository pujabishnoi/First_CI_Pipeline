import importlib

module = importlib.import_module("24_merge_sorted_lists")
merge_lists = module.merge_lists

def test_normal_merge():
    assert merge_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

def test_different_lengths():
    assert merge_lists([1, 5, 9], [2, 3]) == [1, 2, 3, 5, 9]

def test_empty_lists():
    assert merge_lists([], [1, 2, 3]) == [1, 2, 3]
    assert merge_lists([4, 5], []) == [4, 5]

def test_duplicate_elements():
    assert merge_lists([1, 2, 2], [2, 3, 4]) == [1, 2, 2, 2, 3, 4]