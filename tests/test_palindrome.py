"""
Tests the palindrome module
"""
import pytest
from palindrome import is_palindrome


def test_empty_not_string_input():
    """
    Assert that if data type is not a string, a ValueError is raised.
    """
    with pytest.raises(ValueError, match='value must be an str'):
        raise ValueError('value must be an str')


def test_empty_string():
    """
     Assert that value is an empty string it returns False.
     """
    assert is_palindrome('')
    return False


def test_string_true():
    """
    Assert that value is "a" that it return True
     """

    assert is_palindrome('a')
    return True


def test_return_true_with_string_as_bb():
    """
    Assert that value is "bb" that it return True
     """
    assert is_palindrome('bb')
    return True


def test_return_false_with_string_as_abc():
    """
    Assert that value is "abc" that it return False
     """

    assert is_palindrome('abc')
    return False


def test_return_true_with_string_as_laval():
    """
    Assert that value is "laval" that it return True
     """
    assert is_palindrome('laval')
    return True


def test_return_false_with_string_as_toronto():
    """
    Assert that value is "toronto" that it return False
     """
    assert is_palindrome('toronto')
    return False


def test_return_another_true():
    """
    Assert that value is "toronto" that it return True
     """
    assert is_palindrome('Able was I ere I saw Elba')
    return True
