def is_palindrome(text: str) -> bool:
    """Function checks if a string is a palindrome"""

    if type(text) is str or type(text) is int:
        return text.lower() == text[::-1].lower()
    else:
        return False
