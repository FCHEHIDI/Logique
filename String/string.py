class StringUtils:
    """A utility class for string manipulation and analysis operations."""

    @staticmethod
    def clean_string(s: str) -> str:
        """
        Cleans the input string by removing leading and trailing whitespace
        and converting it to lowercase.

        Args:
            s (str): The input string to be cleaned.

        Returns:
            str: The cleaned string.
        """
        return s.strip().lower()

    @staticmethod
    def proper_case(s: str) -> str:
        """
        Converts the input string to proper case (title case).

        Args:
            s (str): The input string to be converted.

        Returns:
            str: The string in proper case.
        """
        return s.title()

    @staticmethod
    def is_exclamation(s: str) -> bool:
        """
        Checks if the input string ends with an exclamation mark.

        Args:
            s (str): The input string to be checked.

        Returns:
            bool: True if the string ends with an exclamation mark,
                False otherwise.
        """
        return s.endswith('!')

    @staticmethod
    def reverse_words(s: str) -> str:
        """
        Reverses the order of words in the input string.

        Args:
            s (str): The input string whose words are to be reversed.
        Returns:
            str: The string with words in reversed order.
        """
        words = s.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

    @staticmethod
    def count_letters(s: str) -> int:
        """
        Counts the number of alphabetic letters in the input string.

        Args:
            s (str): The input string to be analyzed.

        Returns:
            int: The number of alphabetic letters in the string.
        """
        return sum(c.isalpha() for c in s)

    @staticmethod
    def to_camel_case(s: str) -> str:
        """
        Converts the input string to camel case.

        Args:
            s (str): The input string to be converted.

        Returns:
            str: The string in camel case.
        """
        words = s.split()
        if not words:
            return ''
        first_word = words[0].lower()
        camel_cased_words = [first_word] + [
            word.capitalize() for word in words[1:]
        ]
        return ''.join(camel_cased_words)

    @staticmethod
    def count_vowels(s: str) -> int:
        """
        Counts the number of vowels in the input string.

        Args:
            s (str): The input string to be analyzed.
        Returns:
            int: The number of vowels in the string.
        """
        vowels = 'aeiouAEIOU'
        return sum(c in vowels for c in s)

    @staticmethod
    def capital_lowercase(s: str) -> str:
        """
        Converts the input string to a format where uppercase and lowercase
        letters alternate.

        Args:
            s (str): The input string to be converted.
        Returns:
            str: The string with alternating uppercase and lowercase letters.
        """
        result = []
        upper = True
        for char in s:
            if char.isalpha():
                if upper:
                    result.append(char.upper())
                else:
                    result.append(char.lower())
                upper = not upper
            else:
                result.append(char)
        return ''.join(result)

    @staticmethod
    def remove_duplicates(s: str) -> str:
        """
        Removes duplicate characters from the input string while preserving
        the order of first occurrences.

        Args:
            s (str): The input string to be processed.
        Returns:
            str: The string with duplicate characters removed.
        """
        seen = set()
        result = []
        for char in s:
            if char not in seen:
                seen.add(char)
                result.append(char)
        return ''.join(result)

    @staticmethod
    def get_initials(s: str) -> str:
        """
        Extracts the initials from the input string.

        Args:
            s (str): The input string from which to extract initials.
        Returns:
            str: A string containing the initials.
        """
        words = s.split()
        initials = [word[0].upper() for word in words if word]
        return ''.join(initials)

    @staticmethod
    def mask_last_n_chars(s: str, n: int) -> str:
        """
        Remove the characters of the input string except for the last n
        characters.

        Args:
            s (str): The input string to be masked.
            n (int): The number of characters to mask from the end of the
                string.
        Returns:
            str: The masked string.
        """
        if n >= len(s):
            return s
        return s[-n:]

    @staticmethod
    def is_palindrome(s: str) -> bool:
        """
        Checks if the input string is a palindrome (reads the same forwards and
        backwards).

        Args:
            s (str): The input string to be checked.
        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]

    @staticmethod
    def longest_sequence(s: str) -> str:
        """
        Finds the longest sequence of consecutive identical characters in the
        input string.

        Args:
            s (str): The input string to be analyzed.
        Returns:
            str: The longest sequence of consecutive identical characters.
        """
        max_seq = ''
        current_seq = ''
        for char in s:
            if not current_seq or char == current_seq[-1]:
                current_seq += char
            else:
                if len(current_seq) > len(max_seq):
                    max_seq = current_seq
                current_seq = char
        if len(current_seq) > len(max_seq):
            max_seq = current_seq
        return max_seq

    @staticmethod
    def truncate_string(s: str, length: int) -> str:
        """
        Truncates the input string to the specified length, adding '...' if
        it was truncated.

        Args:
            s (str): The input string to be truncated.
            length (int): The maximum length of the truncated string.
        Returns:
            str: The truncated string.
        """
        if len(s) <= length:
            return s
        return s[:length] + '...'

    @staticmethod
    def greeting_proper(name: str) -> str:
        """
        Adds a greeting to the input string in proper case.
        Args:
            name (str): The input string to be greeted.
        Returns:
            str: The greeted string in proper case.
        """
        proper = StringUtils.proper_case(name)
        return f"Bonjour, {proper}!"
