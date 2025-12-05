"""
Test suite for StringUtils class.
Tests all string manipulation methods using fixtures from fixtures.py
"""
import pytest
from String import StringUtils
from tests.fixtures import STRING_FIXTURES


class TestStringUtils:
    """Test cases for StringUtils class."""

    def test_clean_string(self):
        """Test clean_string method."""
        for case in STRING_FIXTURES["clean_string"]:
            result = StringUtils.clean_string(case["input"])
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_proper_case(self):
        """Test proper_case method."""
        for case in STRING_FIXTURES["proper_case"]:
            result = StringUtils.proper_case(case["input"])
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_is_exclamation(self):
        """Test is_exclamation method."""
        for case in STRING_FIXTURES["is_exclamation"]:
            result = StringUtils.is_exclamation(case["input"])
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_reverse_words(self):
        """Test reverse_words method."""
        for case in STRING_FIXTURES["reverse_words"]:
            result = StringUtils.reverse_words(case["input"])
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_count_letters(self):
        """Test count_letters method."""
        for case in STRING_FIXTURES["count_letters"]:
            result = StringUtils.count_letters(case["input"])
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_to_camel_case(self):
        """Test to_camel_case method."""
        for case in STRING_FIXTURES["to_camel_case"]:
            result = StringUtils.to_camel_case(case["input"])
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_count_vowels(self):
        """Test count_vowels method."""
        for case in STRING_FIXTURES["count_vowels"]:
            result = StringUtils.count_vowels(case["input"])
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_capital_lowercase(self):
        """Test capital_lowercase method."""
        for case in STRING_FIXTURES["capital_lowercase"]:
            result = StringUtils.capital_lowercase(case["input"])
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_remove_duplicates(self):
        """Test remove_duplicates method."""
        for case in STRING_FIXTURES["remove_duplicates"]:
            result = StringUtils.remove_duplicates(case["input"])
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_get_initials(self):
        """Test get_initials method."""
        for case in STRING_FIXTURES["get_initials"]:
            result = StringUtils.get_initials(case["input"])
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_mask_last_n_chars(self):
        """Test mask_last_n_chars method."""
        for case in STRING_FIXTURES["mask_last_n_chars"]:
            s, n = case["input"]
            result = StringUtils.mask_last_n_chars(s, n)
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_is_palindrome(self):
        """Test is_palindrome method."""
        for case in STRING_FIXTURES["is_palindrome"]:
            result = StringUtils.is_palindrome(case["input"])
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_longest_sequence(self):
        """Test longest_sequence method."""
        for case in STRING_FIXTURES["longest_sequence"]:
            result = StringUtils.longest_sequence(case["input"])
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_truncate_string(self):
        """Test truncate_string method."""
        for case in STRING_FIXTURES["truncate_string"]:
            s, length = case["input"]
            result = StringUtils.truncate_string(s, length)
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_greeting_proper(self):
        """Test greeting_proper method."""
        for case in STRING_FIXTURES["greeting_proper"]:
            result = StringUtils.greeting_proper(case["input"])
            assert result == case["expected"], f"Failed for input: {case['input']}"
