import unittest
from src.data_processing import normalize_ingredients

class TestNormalizeIngredients(unittest.TestCase):
    def test_normalize_valid_input(self):
        raw = "chiken, garlick, lemmon"
        expected = "chicken, garlic, lemon"
        result = normalize_ingredients(raw)
        self.assertEqual(result, expected)

    def test_normalize_empty_input(self):
        raw = ""
        result = normalize_ingredients(raw)
        self.assertEqual(result, "")

if __name__ == '__main__':
    unittest.main()
