import importlib

module = importlib.import_module("30_decimal_to_binary")
decimal_to_binary = module.decimal_to_binary

def test_zero():
    assert decimal_to_binary(0) == "0"

def test_small_integer():
    assert decimal_to_binary(5) == "101"

def test_larger_integer():
    assert decimal_to_binary(15) == "1111"

def test_power_of_two():
    assert decimal_to_binary(16) == "10000"