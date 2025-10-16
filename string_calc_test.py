import pytest
from calc import Add

def test_empty_string():
    assert Add("") == 0

def test_single_number():
    assert Add("1") == 1

def test_two_numbers():
    assert Add("1,2") == 3

def test_multiple_numbers():
    assert Add("1,2,3") == 6

def test_newline_separator():
    assert Add("1\n2,3") == 6

def test_custom_delimiter():
    assert Add("//;\n1;2") == 3
