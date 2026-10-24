import importlib

module = importlib.import_module("29_armstrong_number")
is_armstrong = module.is_armstrong

def test_valid_three_digit():
    assert is_armstrong(153) is True

def test_valid_single_digit():
    assert is_armstrong(9) is True

def test_invalid_number():
    assert is_armstrong(123) is False

def test_valid_four_digit():
    assert is_armstrong(1634) is True

def test_negative_number():
    assert is_armstrong(-153) is False