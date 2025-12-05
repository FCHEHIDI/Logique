"""
Test suite for ArrayUtils class.
Tests all array manipulation methods using fixtures from fixtures.py
"""
import pytest
from Array_Object import ArrayUtils
from tests.fixtures import ARRAY_FIXTURES


class TestArrayUtils:
    """Test cases for ArrayUtils class."""

    def test_filter_by_property(self):
        """Test filter_by_property method."""
        for case in ARRAY_FIXTURES["filter_by_property"]:
            arr, prop, value = case["input"]
            result = ArrayUtils.filter_by_property(arr, prop, value)
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_group_by(self):
        """Test group_by method."""
        for case in ARRAY_FIXTURES["group_by"]:
            arr, prop = case["input"]
            result = ArrayUtils.group_by(arr, prop)
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_find_intersection(self):
        """Test find_intersection method."""
        for case in ARRAY_FIXTURES["find_intersection"]:
            arr1, arr2, key_func = case["input"]
            result = ArrayUtils.find_intersection(arr1, arr2, key_func)
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_transform_array(self):
        """Test transform_array method."""
        for case in ARRAY_FIXTURES["transform_array"]:
            arr, transformer = case["input"]
            result = ArrayUtils.transform_array(arr, transformer)
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_aggregate_data(self):
        """Test aggregate_data method."""
        for case in ARRAY_FIXTURES["aggregate_data"]:
            arr, key = case["input"]
            result = ArrayUtils.aggregate_data(arr, key)
            assert result == case["expected"], f"Failed for input: {case['input']}"
