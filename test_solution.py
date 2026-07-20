import unittest

from solution import longest_valid_parentheses


class TestLongestValidParentheses(unittest.TestCase):
    def test_first_example(self):
        self.assertEqual(longest_valid_parentheses("(()"), 2)

    def test_second_example(self):
        self.assertEqual(longest_valid_parentheses(")()())"), 4)

    def test_empty_string(self):
        self.assertEqual(longest_valid_parentheses(""), 0)

    def test_nested_parentheses(self):
        self.assertEqual(longest_valid_parentheses("(())"), 4)

    def test_no_valid_pair(self):
        self.assertEqual(longest_valid_parentheses(")))((("), 0)


if __name__ == "__main__":
    unittest.main()
