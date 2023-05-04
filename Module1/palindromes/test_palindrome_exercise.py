import unittest
from palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):
    def test_is_paindrome(self) -> None:
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("Kajak"))
        self.assertTrue(is_palindrome("KAJAK"))
        self.assertTrue(is_palindrome("KAjak"))
        self.assertTrue(is_palindrome("kajak"))
        self.assertTrue(is_palindrome("potop"))
        self.assertTrue(is_palindrome("aka"))
        self.assertTrue(is_palindrome("www"))
        self.assertTrue(is_palindrome("12321"))


    def test_is_not_palindrome(self) -> None:
        self.assertFalse(is_palindrome("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod"))
        self.assertFalse(is_palindrome("dom"))
        self.assertFalse(is_palindrome("terminator"))
        self.assertFalse(is_palindrome("alaska"))
        self.assertFalse(is_palindrome("example"))
        self.assertFalse(is_palindrome("123456"))
        self.assertFalse(is_palindrome("1.23"))
        self.assertFalse(is_palindrome(['a', 'b', 'a']))


if __name__ == "__main__":
    unittest.main()

# Zastanów się, jak (i czy) uwzględniać:

# puste wejście
# różną wielkość znaków
# całe zdania z interpunkcją
# liczby całkowite i zmiennoprzecinkowe
# inne typy danych wejściowych (listy, daty, ...)
