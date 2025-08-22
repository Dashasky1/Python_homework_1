import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    ("  hello world", "hello world"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [("  123", " 123")])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol", [
    ("skypro", "o"),
    ("hello world", " "),
])
def test_contains_positive(string, symbol):
    Utiles2 = StringUtils()
    assert Utiles2.contains(string, symbol) is True


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol", [
    ("skypro", "z"),])
def test_contains_negative(string, symbol):
    Utiles2 = StringUtils()
    assert not Utiles2.contains(string, symbol) is False


@pytest.mark.positive
def test_delete_symbol_positive(string, symbol, expected_result):
    assert string_utils.delete_symbol(string, symbol) == expected_result
    assert string_utils.delete_symbol("skypro", "s") == "kypro"



@pytest.mark.negative
def test_delete_symbol_negative(string, symbol, expected_result):
    assert string_utils.delete_symbol(string, symbol) == expected_result
    assert string_utils.delete_symbol("skypro", "1") == "skypro"
