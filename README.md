# Python Logic Challenges - Utility Functions

![Logique](sci-fi-cpu.png)

A comprehensive collection of utility functions for string manipulation, dictionary operations, and array processing, organized into clean, testable classes.

## 📦 Project Structure

```
Logique/
├── String/
│   ├── __init__.py
│   ├── string.py          # StringUtils class with 16 methods
│   └── string.md          # Exercise specifications
├── Object2/
│   ├── __init__.py
│   ├── object2.py         # DictUtils class with 18 methods
│   └── object-2.md        # Exercise specifications
├── Array_Object/
│   ├── __init__.py
│   ├── array_object.py    # ArrayUtils class with 5 methods
│   └── array-object.md    # Exercise specifications
├── tests/
│   ├── __init__.py
│   ├── fixtures.py        # Test data and fixtures
│   ├── test_string_utils.py
│   ├── test_dict_utils.py
│   └── test_array_utils.py
├── test_results.txt       # Latest test execution results
└── README.md
```

## 🚀 Features

### StringUtils (16 methods)
String manipulation utilities including:
- `clean_string()` - Clean and normalize strings
- `proper_case()` - Convert to title case
- `is_exclamation()` - Check for exclamation marks
- `reverse_words()` - Reverse word order
- `count_letters()` - Count alphabetic characters
- `to_camel_case()` - Convert to camelCase
- `count_vowels()` - Count vowels
- `capital_lowercase()` - Alternate case letters
- `remove_duplicates()` - Remove duplicate characters
- `get_initials()` - Extract initials
- `mask_last_n_chars()` - Mask string partially
- `is_palindrome()` - Check palindromes
- `longest_sequence()` - Find longest consecutive sequence
- `truncate_string()` - Truncate with ellipsis
- `greeting_proper()` - Generate personalized greetings

### DictUtils (18 methods)
Dictionary manipulation utilities including:
- `get_values()` - Extract all values
- `transform_values()` - Apply function to values
- `merge_objects()` - Merge dictionaries
- `filter_object()` - Filter by predicate
- `flat_to_nested()` - Convert flat to nested structure
- `find_keys_by_value()` - Find keys by value
- `count_values()` - Count value occurrences
- `extract_properties()` - Extract specific keys
- `sort_by_values()` - Sort by values
- `find_max_value()` - Find maximum value
- `create_objects_from_pairs()` - Create from key-value pairs
- `find_value_in_nested()` - Navigate nested structures
- `group_by_property()` - Group objects by property
- `validate_object()` - Validate against schema
- `compare_differences()` - Compare two objects
- `object_to_url_params()` - Convert to URL parameters
- `get_object_stats()` - Calculate statistics

### ArrayUtils (5 methods)
Array/list manipulation utilities including:
- `filter_by_property()` - Filter objects by property
- `group_by()` - Group objects by property
- `find_intersection()` - Find common elements
- `transform_array()` - Transform elements
- `aggregate_data()` - Aggregate by key

## 🔧 Installation

### Prerequisites
- Python 3.11+
- Virtual environment (recommended)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd Logique
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install pytest
```

## 📚 Usage

### Importing Modules

```python
from String import StringUtils
from Object2 import DictUtils
from Array_Object import ArrayUtils
```

### Example Usage

#### String Operations
```python
# Clean and normalize string
result = StringUtils.clean_string("  Hello World  ")
# Output: "hello world"

# Get initials
initials = StringUtils.get_initials("Jean Pierre Martin")
# Output: "JPM"

# Check palindrome
is_palindrome = StringUtils.is_palindrome("racecar")
# Output: True
```

#### Dictionary Operations
```python
# Transform values
prices = {"book": 20, "pen": 5}
dollars = DictUtils.transform_values(prices, lambda x: x * 1.1)
# Output: {"book": 22.0, "pen": 5.5}

# Flat to nested
flat = {"app.name": "MyApp", "app.version": "1.0"}
nested = DictUtils.flat_to_nested(flat)
# Output: {"app": {"name": "MyApp", "version": "1.0"}}

# Get statistics
stats = DictUtils.get_object_stats({"jan": 100, "feb": 200})
# Returns detailed stats with min, max, average, median, variance, etc.
```

#### Array Operations
```python
# Filter by property
users = [
    {"name": "Alice", "active": True},
    {"name": "Bob", "active": False}
]
active = ArrayUtils.filter_by_property(users, "active", True)
# Output: [{"name": "Alice", "active": True}]

# Group by property
products = [
    {"name": "Laptop", "category": "Electronics"},
    {"name": "T-shirt", "category": "Clothing"}
]
grouped = ArrayUtils.group_by(products, "category")
# Output: {"Electronics": [...], "Clothing": [...]}
```

## 🧪 Testing

### Run All Tests
```bash
pytest tests/ -v
```

### Run Specific Test File
```bash
pytest tests/test_string_utils.py -v
pytest tests/test_dict_utils.py -v
pytest tests/test_array_utils.py -v
```

### Test Coverage
- **37 test methods** covering all 39 utility functions
- All tests use fixtures from `tests/fixtures.py`
- 100% pass rate ✅

### Latest Test Results
See `test_results.txt` for the most recent test execution output.

## 📝 Development

### Project Organization
- All utility functions are implemented as **static methods** in their respective classes
- Each module has proper `__init__.py` for clean imports
- Comprehensive test fixtures based on exercise specifications
- Clear separation of concerns between modules

### Code Style
- Type hints on all function signatures
- Comprehensive docstrings
- PEP 8 compliant
- Clean, readable implementations

## 🎯 Use Cases

This library is designed for common programming challenges including:
- **String manipulation** for text processing, validation, formatting
- **Dictionary operations** for data transformation, configuration management
- **Array processing** for filtering, grouping, and transforming collections

Perfect for:
- Technical interviews and coding challenges
- Data processing pipelines
- API response formatting
- Configuration management
- Learning Python fundamentals

## 📄 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Contributions are welcome! Please ensure:
1. All new functions include tests
2. Tests pass before submitting
3. Code follows existing style patterns
4. Docstrings are comprehensive

## 📊 Statistics

- **3 Utility Classes**
- **39 Total Functions**
- **37 Test Methods**
- **100% Test Pass Rate**
- **0.13s Test Execution Time**

---

Made with ❤️ for Python learning and practice
