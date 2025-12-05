from typing import Any


class ArrayUtils:
    """A utility class for array and list operations.

    Includes filtering, grouping, and transformation.
    """

    @staticmethod
    def filter_by_property(arr: list, property_name: str, value: Any) -> list:
        """
        Filters an array of objects (dictionaries) based on a specified
        property and its value.

        :param arr: List of dictionaries to be filtered.
        :type arr: list[dict]
        :param property_name: The property name to filter by.
        :type property_name: str
        :param value: The value that the specified property should match.
        :return: A list of dictionaries that have the specified property equal to
            the given value.
        :rtype: list[dict]
        """
        return [obj for obj in arr if obj.get(property_name) == value]

    @staticmethod
    def group_by(arr: list, property_name: str) -> dict:
        """
        Groups an array of objects (dictionaries) by a specified property.

        :param arr: List of dictionaries to be grouped.
        :type arr: list[dict]
        :param property_name: The property name to group by.
        :type property_name: str
        :return: A dictionary where the keys are the unique values of the
            specified property, and the values are lists of dictionaries
            that share that property value.
        :rtype: dict[Any, list[dict]]
        """
        grouped = {}
        for obj in arr:
            key = obj.get(property_name)
            if key not in grouped:
                grouped[key] = []
            grouped[key].append(obj)
        return grouped

    @staticmethod
    def find_intersection(arr1: list, arr2: list, key_func) -> list:
        """
        Finds the intersection of two arrays (lists), returning a list of
        elements that are present in both arrays.

        :param arr1: The first list.
        :type arr1: list[Any]
        :param arr2: The second list.
        :type arr2: list[Any]
        :return: A list containing the elements that are present in both input
            lists.
        :rtype: list[Any]
        """
        set2 = set(key_func(item) for item in arr2)
        return [item for item in arr1 if key_func(item) in set2]

    @staticmethod
    def transform_array(arr: list, transformer_func) -> list:
        """
        Transforms an array (list) by applying a transformation function to
        each element.

        :param arr: The input list to be transformed.
        :type arr: list[Any]
        :param transformer_func: A function that takes an element of the
            list and returns a transformed element.
        :type transformer_func: Callable[[Any], Any]
        :return: A new list containing the transformed elements.
        :rtype: list[Any]
        """
        return [transformer_func(item) for item in arr]

    @staticmethod
    def aggregate_data(arr: list, key: str) -> dict:
        """
        Aggregates data from an array of objects (dictionaries) based on a
        specified key.

        :param arr: List of dictionaries to be aggregated.
        :type arr: list[dict]
        :param key: The key to aggregate by.
        :type key: str
        :return: A dictionary where the keys are the unique values of the
            specified key, and the values are counts of how many times each
            key value appears in the input list.
        :rtype: dict[Any, int]
        """
        aggregation = {}
        for obj in arr:
            key_value = obj.get(key)
            if key_value in aggregation:
                aggregation[key_value] += 1
            else:
                aggregation[key_value] = 1
        return aggregation
