"""
Test suite for DictUtils class.
Tests all dictionary manipulation methods using fixtures from fixtures.py
"""
import pytest
from Object2 import DictUtils
from tests.fixtures import DICT_FIXTURES


class TestDictUtils:
    """Test cases for DictUtils class."""

    def test_get_values(self):
        """Test get_values method."""
        for case in DICT_FIXTURES["get_values"]:
            result = DictUtils.get_values(case["input"])
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_transform_values(self):
        """Test transform_values method."""
        for case in DICT_FIXTURES["transform_values"]:
            obj, func = case["input"]
            result = DictUtils.transform_values(obj, func)
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_merge_objects(self):
        """Test merge_objects method."""
        for case in DICT_FIXTURES["merge_objects"]:
            obj1, obj2 = case["input"]
            result = DictUtils.merge_objects(obj1, obj2)
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_filter_object(self):
        """Test filter_object method."""
        for case in DICT_FIXTURES["filter_object"]:
            obj, predicate = case["input"]
            result = DictUtils.filter_object(obj, predicate)
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_flat_to_nested(self):
        """Test flat_to_nested method."""
        for case in DICT_FIXTURES["flat_to_nested"]:
            result = DictUtils.flat_to_nested(case["input"])
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_find_keys_by_value(self):
        """Test find_keys_by_value method."""
        for case in DICT_FIXTURES["find_keys_by_value"]:
            obj, target = case["input"]
            result = DictUtils.find_keys_by_value(obj, target)
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_count_values(self):
        """Test count_values method."""
        for case in DICT_FIXTURES["count_values"]:
            result = DictUtils.count_values(case["input"])
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_extract_properties(self):
        """Test extract_properties method."""
        for case in DICT_FIXTURES["extract_properties"]:
            obj, keys = case["input"]
            result = DictUtils.extract_properties(obj, keys)
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_sort_by_values(self):
        """Test sort_by_values method."""
        for case in DICT_FIXTURES["sort_by_values"]:
            result = DictUtils.sort_by_values(case["input"])
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_find_max_value(self):
        """Test find_max_value method."""
        for case in DICT_FIXTURES["find_max_value"]:
            result = DictUtils.find_max_value(case["input"])
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_create_objects_from_pairs(self):
        """Test create_objects_from_pairs method."""
        for case in DICT_FIXTURES["create_objects_from_pairs"]:
            result = DictUtils.create_objects_from_pairs(case["input"])
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_find_value_in_nested(self):
        """Test find_value_in_nested method."""
        for case in DICT_FIXTURES["find_value_in_nested"]:
            obj, keys = case["input"]
            result = DictUtils.find_value_in_nested(obj, keys)
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_group_by_property(self):
        """Test group_by_property method."""
        for case in DICT_FIXTURES["group_by_property"]:
            obj, key_func = case["input"]
            result = DictUtils.group_by_property(obj, key_func)
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_validate_object(self):
        """Test validate_object method."""
        for case in DICT_FIXTURES["validate_object"]:
            obj, schema = case["input"]
            result = DictUtils.validate_object(obj, schema)
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_compare_differences(self):
        """Test compare_differences method."""
        for case in DICT_FIXTURES["compare_differences"]:
            obj1, obj2 = case["input"]
            result = DictUtils.compare_differences(obj1, obj2)
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_object_to_url_params(self):
        """Test object_to_url_params method."""
        for case in DICT_FIXTURES["object_to_url_params"]:
            result = DictUtils.object_to_url_params(case["input"])
            assert result == case["expected"], f"Failed for input: {case['input']}"

    def test_get_object_stats(self):
        """Test get_object_stats method."""
        for case in DICT_FIXTURES["get_object_stats"]:
            result = DictUtils.get_object_stats(case["input"])
            expected = case["expected"]
            
            # Compare basic stats
            assert result["basic"]["min"] == expected["basic"]["min"]
            assert result["basic"]["max"] == expected["basic"]["max"]
            assert result["basic"]["total"] == expected["basic"]["total"]
            
            # Compare with tolerance for floating point
            if expected["basic"]["average"] is not None:
                assert abs(result["basic"]["average"] - expected["basic"]["average"]) < 0.01
            
            # Compare advanced stats
            assert result["advanced"]["median"] == expected["advanced"]["median"]
            
            if expected["advanced"]["variance"] is not None:
                assert abs(result["advanced"]["variance"] - expected["advanced"]["variance"]) < 0.01
            
            if expected["advanced"]["standardDeviation"] is not None:
                assert abs(result["advanced"]["standardDeviation"] - expected["advanced"]["standardDeviation"]) < 0.01
