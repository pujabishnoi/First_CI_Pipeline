import importlib

module = importlib.import_module("28_set_intersection")
set_intersection = module.set_intersection

def test_overlapping_elements():
    assert set_intersection([1, 2, 3], [2, 3, 4]) == [2, 3]

def test_no_overlap():
    assert set_intersection([1, 2], [3, 4]) == []

def test_with_duplicates():
    assert set_intersection([1, 1, 2], [1, 2, 2]) == [1, 2]

def test_empty_lists():
    assert set_intersection([], [1, 2]) == []
    assert set_intersection([1, 2], []) == []