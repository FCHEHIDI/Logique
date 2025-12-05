class DictUtils:
    """A utility class for dictionary manipulation, analysis, and
    transformation operations."""

    @staticmethod
    def get_values(iterable_obj: dict) -> list:
        """
        Docstring for get_values
        
        :param iterable_obj: Description
        :type iterable_obj: dict
        :return: Description
        :rtype: list[Any]
        """
        return list(iterable_obj.values())

    @staticmethod
    def transform_values(iterable_obj: dict, func) -> dict:
        """
        Docstring for transform_values
        
        :param iterable_obj: Description
        :type iterable_obj: dict
        :param func: Description
        :type func: Callable
        :return: Description
        :rtype: dict[Any, Any]
        """
        return {k: func(v) for k, v in iterable_obj.items()}

    @staticmethod
    def merge_objects(obj1: dict, obj2: dict) -> dict:
        """
        Docstring for merge_objects
        
        :param obj1: Description
        :type obj1: dict
        :param obj2: Description
        :type obj2: dict
        :return: Description
        :rtype: dict[Any, Any]
        """
        merged = obj1.copy()
        merged.update(obj2)
        return merged

    @staticmethod
    def filter_object(obj: dict, predicate) -> dict:
        """
        Docstring for filter_object
        
        :param obj: Description
        :type obj: dict
        :param predicate: Description
        :type predicate: Callable
        :return: Description
        :rtype: dict[Any, Any]
        """
        return {k: v for k, v in obj.items() if predicate(k, v)}

    @staticmethod
    def flat_to_nested(obj: dict, delimiter: str = '.') -> dict:
        """
        Docstring for flat_to_nested
        
        :param obj: Description
        :type obj: dict
        :param delimiter: Description
        :type delimiter: str
        :return: Description
        :rtype: dict[Any, Any]
        """
        nested = {}
        for key, value in obj.items():
            parts = key.split(delimiter)
            d = nested
            for part in parts[:-1]:
                if part not in d:
                    d[part] = {}
                d = d[part]
            d[parts[-1]] = value
        return nested

    @staticmethod
    def find_keys_by_value(obj: dict, target_value) -> list:
        """
        Docstring for find_keys_by_value
        
        :param obj: Description
        :type obj: dict
        :param target_value: Description
        :type target_value: Any
        :return: Description
        :rtype: list[Any]
        """
        return [k for k, v in obj.items() if v == target_value]

    @staticmethod
    def count_values(obj: dict) -> dict:
        """
        Docstring for count_values
        
        :param obj: Description
        :type obj: dict
        :return: Description
        :rtype: dict[Any, int]
        """
        value_count = {}
        for value in obj.values():
            if value in value_count:
                value_count[value] += 1
            else:
                value_count[value] = 1
        return value_count

    @staticmethod
    def extract_properties(obj: dict, keys: list) -> dict:
        """
        Docstring for extract_properties
        
        :param obj: Description
        :type obj: dict
        :param keys: Description
        :type keys: list
        :return: Description
        :rtype: dict[Any, Any]
        """
        return {k: obj[k] for k in keys if k in obj}

    @staticmethod
    def sort_by_values(obj: dict) -> list:
        """
        Docstring for sort_by_values
        
        :param obj: Description
        :type obj: dict
        :return: Description
        :rtype: list[tuple[Any, Any]]
        """
        return sorted(obj.items(), key=lambda item: item[1])

    @staticmethod
    def find_max_value(obj: dict):
        """
        Docstring for find_max_value
        
        :param obj: Description
        :type obj: dict
        :return: Description
        :rtype: Any
        """
        if not obj:
            return None
        return max(obj.values())

    @staticmethod
    def create_objects_from_pairs(pairs: list) -> dict:
        """
        Docstring for create_objects_from_pairs
        
        :param pairs: Description
        :type pairs: list[tuple[Any, Any]]
        :return: Description
        :rtype: dict[Any, Any]
        """
        return {k: v for k, v in pairs}

    @staticmethod
    def find_value_in_nested(obj: dict, keys: list):
        """
        Docstring for find_value_in_nested
        
        :param obj: Description
        :type obj: dict
        :param keys: Description
        :type keys: list
        :return: Description
        :rtype: Any
        """
        current = obj
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return None
        return current

    @staticmethod
    def group_by_property(iterable_obj: list, key_func) -> dict:
        """
        Docstring for group_by_property
        
        :param iterable_obj: Description
        :type iterable_obj: list[dict]
        :param key_func: Description
        :type key_func: Callable
        :return: Description
        :rtype: dict[Any, list[dict]]
        """
        grouped = {}
        for item in iterable_obj:
            key = key_func(item)
            if key not in grouped:
                grouped[key] = []
            grouped[key].append(item)
        return grouped

    @staticmethod
    def validate_object(obj: dict, schema: dict) -> bool:
        """
        Docstring for validate_object
        
        :param obj: Description
        :type obj: dict
        :param schema: Description
        :type schema: dict
        :return: Description
        :rtype: bool
        """
        for key, expected_type in schema.items():
            if key not in obj or not isinstance(obj[key], expected_type):
                return False
        return True

    @staticmethod
    def compare_differences(obj1: dict, obj2: dict) -> dict:
        """
        Docstring for compare_differences
        
        :param obj1: Description
        :type obj1: dict
        :param obj2: Description
        :type obj2: dict
        :return: Description
        :rtype: dict[Any, tuple[Any, Any]]
        """
        differences = {}
        all_keys = set(obj1.keys()).union(set(obj2.keys()))
        for key in all_keys:
            val1 = obj1.get(key)
            val2 = obj2.get(key)
            if val1 != val2:
                differences[key] = (val1, val2)
        return differences

    @staticmethod
    def object_to_url_params(obj: dict) -> str:
        """
        Docstring for object_to_url_params
        
        :param obj: Description
        :type obj: dict
        :return: Description
        :rtype: str
        """
        from urllib.parse import urlencode
        return urlencode(obj)

    @staticmethod
    def get_object_stats(obj: dict) -> dict:
        """
        Docstring for get_object_stats
        
        :param obj: Description
        :type obj: dict
        :return: Description basic and advanced statistics about the object.
        :rtype: dict[str, Any]
    """

        import statistics

        values = [v for v in obj.values() if isinstance(v, (int, float))]
        if not values:
            return {
                "basic": {
                    "min": None,
                    "max": None,
                    "average": None,
                    "total": None
                },
                "advanced": {
                    "median": None,
                    "variance": None,
                    "standardDeviation": None
                }
            }

        basic_stats = {
            "min": min(values),
            "max": max(values),
            "average": sum(values) / len(values),
            "total": sum(values)
        }

        advanced_stats = {
            "median": statistics.median(values),
            "variance": statistics.variance(values) if len(values) > 1 else 0,
            "standardDeviation": statistics.stdev(values) if len(values) > 1 else 0
        }

        return {
            "basic": basic_stats,
            "advanced": advanced_stats
        }
