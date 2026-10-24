import importlib

module = importlib.import_module("22_anagram_strings")
is_anagram = module.is_anagram

def test_valid_anagram():
    assert is_anagram("listen", "silent") is True

def test_invalid_anagram():
    assert is_anagram("hello", "world") is False

def test_with_spaces_and_case():
    assert is_anagram("Astronomer", "Moon starer") is True

def test_different_lengths():
    assert is_anagram("cat", "cats") is False