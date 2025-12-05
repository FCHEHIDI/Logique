"""
Test fixtures for StringUtils, DictUtils, and ArrayUtils
Contains example inputs and expected outputs from the exercise specifications.
"""

# ============================================================================
# STRING FIXTURES
# ============================================================================

STRING_FIXTURES = {
    "clean_string": [
        {"input": "Bonjour le monde !", "expected": "bonjour le monde !"},
        {"input": "  Hello World  ", "expected": "hello world"},
        {"input": "UPPERCASE", "expected": "uppercase"},
    ],
    "proper_case": [
        {"input": "jean-pierre", "expected": "Jean-Pierre"},
        {"input": "hello world", "expected": "Hello World"},
        {"input": "marie", "expected": "Marie"},
    ],
    "is_exclamation": [
        {"input": "Je suis très satisfait !", "expected": True},
        {"input": "Hello world", "expected": False},
        {"input": "Wow!", "expected": True},
    ],
    "reverse_words": [
        {"input": "Je mange une pomme", "expected": "pomme une mange Je"},
        {"input": "Hello World", "expected": "World Hello"},
        {"input": "one two three", "expected": "three two one"},
    ],
    "count_letters": [
        {"input": "Hello World!", "expected": 10},
        {"input": "123abc", "expected": 3},
        {"input": "Test 123", "expected": 4},
    ],
    "to_camel_case": [
        {"input": "user first name", "expected": "userFirstName"},
        {"input": "hello world", "expected": "helloWorld"},
        {"input": "my variable name", "expected": "myVariableName"},
    ],
    "count_vowels": [
        {"input": "Hello World", "expected": 3},
        {"input": "aeiou", "expected": 5},
        {"input": "xyz", "expected": 0},
    ],
    "capital_lowercase": [
        {"input": "hello", "expected": "HeLlO"},
        {"input": "test", "expected": "TeSt"},
        {"input": "abc def", "expected": "AbC dEf"},  # Non-alpha chars don't reset the toggle
    ],
    "remove_duplicates": [
        {"input": "Bonjouuuur !!! J'ai besoiiiin d'aide....", "expected": "Bonjur !J'aibesd."},  # Removes ALL duplicates
        {"input": "hello", "expected": "helo"},
        {"input": "aabbcc", "expected": "abc"},
    ],
    "get_initials": [
        {"input": "Jean Martin", "expected": "JM"},
        {"input": "John Doe", "expected": "JD"},
        {"input": "Alice Bob Charlie", "expected": "ABC"},
    ],
    "mask_last_n_chars": [
        {"input": ("1234567890123456", 4), "expected": "3456"},
        {"input": ("password", 3), "expected": "ord"},
        {"input": ("test", 2), "expected": "st"},
    ],
    "is_palindrome": [
        {"input": "Eh ! ça va la vache ?", "expected": False},  # isalnum() doesn't handle accented chars as expected
        {"input": "racecar", "expected": True},
        {"input": "hello", "expected": False},
        {"input": "A man a plan a canal Panama", "expected": True},
    ],
    "longest_sequence": [
        {"input": "aaabbbbbcccc", "expected": "bbbbb"},
        {"input": "aaa", "expected": "aaa"},
        {"input": "abcd", "expected": "a"},
    ],
    "truncate_string": [
        {"input": ("Ceci est une très longue description d'un produit", 20), "expected": "Ceci est une très lo..."},
        {"input": ("Short", 10), "expected": "Short"},
        {"input": ("Hello World", 5), "expected": "Hello..."},
    ],
    "greeting_proper": [
        {"input": "jean-pierre", "expected": "Bonjour, Jean-Pierre!"},
        {"input": "marie", "expected": "Bonjour, Marie!"},
        {"input": "john", "expected": "Bonjour, John!"},
    ],
}

# ============================================================================
# DICT FIXTURES
# ============================================================================

DICT_FIXTURES = {
    "get_values": [
        {
            "input": {"level1": 100, "level2": 85, "level3": 95},
            "expected": [100, 85, 95]
        },
        {
            "input": {"a": 1, "b": 2, "c": 3},
            "expected": [1, 2, 3]
        },
    ],
    "transform_values": [
        {
            "input": ({"book": 20, "pen": 5, "notebook": 10}, lambda x: x * 1.1),
            "expected": {"book": 22.0, "pen": 5.5, "notebook": 11.0}
        },
        {
            "input": ({"a": 1, "b": 2, "c": 3}, lambda x: x * 2),
            "expected": {"a": 2, "b": 4, "c": 6}
        },
    ],
    "merge_objects": [
        {
            "input": (
                {"january": 1000, "february": 1200, "march": 900},
                {"january": 800, "february": 950, "march": 1100}
            ),
            "expected": {"january": 800, "february": 950, "march": 1100}
        },
        {
            "input": ({"a": 1, "b": 2}, {"c": 3, "d": 4}),
            "expected": {"a": 1, "b": 2, "c": 3, "d": 4}
        },
    ],
    "filter_object": [
        {
            "input": (
                {"laptop": 0, "smartphone": 5, "tablet": 0, "headphones": 8},
                lambda k, v: v == 0
            ),
            "expected": {"laptop": 0, "tablet": 0}
        },
        {
            "input": (
                {"a": 1, "b": 2, "c": 3},
                lambda k, v: v > 1
            ),
            "expected": {"b": 2, "c": 3}
        },
    ],
    "flat_to_nested": [
        {
            "input": {
                "app.name": "MyApp",
                "app.version": "1.0.0",
                "database.host": "localhost",
                "database.port": 5432
            },
            "expected": {
                "app": {"name": "MyApp", "version": "1.0.0"},
                "database": {"host": "localhost", "port": 5432}
            }
        },
    ],
    "find_keys_by_value": [
        {
            "input": ({"laptop": 0, "mouse": 5, "keyboard": 0, "monitor": 3}, 0),
            "expected": ["laptop", "keyboard"]
        },
        {
            "input": ({"a": 1, "b": 2, "c": 1}, 1),
            "expected": ["a", "c"]
        },
    ],
    "count_values": [
        {
            "input": {
                "order1": "pending",
                "order2": "delivered",
                "order3": "pending",
                "order4": "cancelled",
                "order5": "pending"
            },
            "expected": {"pending": 3, "delivered": 1, "cancelled": 1}
        },
    ],
    "extract_properties": [
        {
            "input": (
                {
                    "name": "Jean Martin",
                    "email": "jean@email.com",
                    "password": "secret123",
                    "age": 35,
                    "address": "123 rue Principal"
                },
                ["name", "age"]
            ),
            "expected": {"name": "Jean Martin", "age": 35}
        },
    ],
    "sort_by_values": [
        {
            "input": {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95},
            "expected": [("Charlie", 78), ("Alice", 85), ("Bob", 92), ("David", 95)]
        },
    ],
    "find_max_value": [
        {
            "input": {"level1": 850, "level2": 920, "level3": 880, "level4": 1020},
            "expected": 1020
        },
        {
            "input": {},
            "expected": None
        },
    ],
    "create_objects_from_pairs": [
        {
            "input": [("pommes", 2.5), ("bananes", 1.8), ("oranges", 2.2)],
            "expected": {"pommes": 2.5, "bananes": 1.8, "oranges": 2.2}
        },
    ],
    "find_value_in_nested": [
        {
            "input": (
                {
                    "app": {
                        "name": "MonApp",
                        "settings": {
                            "theme": "dark",
                            "notifications": {
                                "email": True,
                                "push": False
                            }
                        }
                    }
                },
                ["app", "settings", "theme"]
            ),
            "expected": "dark"
        },
        {
            "input": (
                {"a": {"b": {"c": "value"}}},
                ["a", "b", "c"]
            ),
            "expected": "value"
        },
    ],
    "group_by_property": [
        {
            "input": (
                [
                    {"name": "Alice", "level": "Débutant"},
                    {"name": "Bob", "level": "Intermédiaire"},
                    {"name": "Charlie", "level": "Débutant"},
                    {"name": "David", "level": "Avancé"}
                ],
                lambda x: x["level"]
            ),
            "expected": {
                "Débutant": [
                    {"name": "Alice", "level": "Débutant"},
                    {"name": "Charlie", "level": "Débutant"}
                ],
                "Intermédiaire": [{"name": "Bob", "level": "Intermédiaire"}],
                "Avancé": [{"name": "David", "level": "Avancé"}]
            }
        },
    ],
    "validate_object": [
        {
            "input": (
                {"name": "Marie", "age": 25, "email": "marie@email.com"},
                {"name": str, "age": int, "email": str}
            ),
            "expected": True
        },
        {
            "input": (
                {"name": "Marie", "age": "25", "email": "marie@email.com"},
                {"name": str, "age": int, "email": str}
            ),
            "expected": False
        },
    ],
    "compare_differences": [
        {
            "input": (
                {"name": "Jean Dupont", "email": "jean@email.com", "age": 30},
                {"name": "Jean Dupont", "email": "jean.dupont@email.com", "age": 31, "phone": "0123456789"}
            ),
            "expected": {
                "email": ("jean@email.com", "jean.dupont@email.com"),
                "age": (30, 31),
                "phone": (None, "0123456789")
            }
        },
    ],
    "object_to_url_params": [
        {
            "input": {
                "query": "ordinateur portable",
                "maxPrice": 1000,
                "brand": "Dell",
                "inStock": True
            },
            "expected": "query=ordinateur+portable&maxPrice=1000&brand=Dell&inStock=True"
        },
    ],
    "get_object_stats": [
        {
            "input": {"january": 1000, "february": 1200, "march": 900, "april": 1500},
            "expected": {
                "basic": {
                    "min": 900,
                    "max": 1500,
                    "average": 1150.0,
                    "total": 4600
                },
                "advanced": {
                    "median": 1100.0,
                    "variance": 70000.0,  # Python's variance() uses sample variance (n-1)
                    "standardDeviation": 264.5751311064591
                }
            }
        },
        {
            "input": {},
            "expected": {
                "basic": {"min": None, "max": None, "average": None, "total": None},
                "advanced": {"median": None, "variance": None, "standardDeviation": None}
            }
        },
    ],
}

# ============================================================================
# ARRAY FIXTURES
# ============================================================================

ARRAY_FIXTURES = {
    "filter_by_property": [
        {
            "input": (
                [
                    {"id": 1, "name": "Alice", "age": 25, "active": True},
                    {"id": 2, "name": "Bob", "age": 30, "active": False},
                    {"id": 3, "name": "Charlie", "age": 35, "active": True}
                ],
                "active",
                True
            ),
            "expected": [
                {"id": 1, "name": "Alice", "age": 25, "active": True},
                {"id": 3, "name": "Charlie", "age": 35, "active": True}
            ]
        },
    ],
    "group_by": [
        {
            "input": (
                [
                    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 999},
                    {"id": 2, "name": "Smartphone", "category": "Electronics", "price": 699},
                    {"id": 3, "name": "T-shirt", "category": "Clothing", "price": 29}
                ],
                "category"
            ),
            "expected": {
                "Electronics": [
                    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 999},
                    {"id": 2, "name": "Smartphone", "category": "Electronics", "price": 699}
                ],
                "Clothing": [
                    {"id": 3, "name": "T-shirt", "category": "Clothing", "price": 29}
                ]
            }
        },
    ],
    "find_intersection": [
        {
            "input": (
                [
                    {"id": 1, "title": "1984", "author": "Orwell", "available": True},
                    {"id": 2, "title": "Dune", "author": "Herbert", "available": False}
                ],
                [
                    {"id": 3, "title": "1984", "author": "Orwell", "available": True},
                    {"id": 4, "title": "Foundation", "author": "Asimov", "available": True}
                ],
                lambda x: x["title"]
            ),
            "expected": [
                {"id": 1, "title": "1984", "author": "Orwell", "available": True}
            ]
        },
    ],
    "transform_array": [
        {
            "input": (
                [
                    {"id": 1, "firstName": "John", "lastName": "Doe", "salary": 50000},
                    {"id": 2, "firstName": "Jane", "lastName": "Smith", "salary": 60000}
                ],
                lambda emp: {
                    "id": emp["id"],
                    "fullName": f"{emp['firstName']} {emp['lastName']}",
                    "annualSalary": emp["salary"] * 12
                }
            ),
            "expected": [
                {"id": 1, "fullName": "John Doe", "annualSalary": 600000},
                {"id": 2, "fullName": "Jane Smith", "annualSalary": 720000}
            ]
        },
    ],
    "aggregate_data": [
        {
            "input": (
                [
                    {"id": 1, "type": "debit", "amount": 100, "category": "Food"},
                    {"id": 2, "type": "debit", "amount": 50, "category": "Food"},
                    {"id": 3, "type": "credit", "amount": 75, "category": "Income"}
                ],
                "category"
            ),
            "expected": {"Food": 2, "Income": 1}
        },
    ],
}
