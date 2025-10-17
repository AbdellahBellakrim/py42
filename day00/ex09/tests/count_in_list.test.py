import unittest
from ft_package import count_in_list


class TestCountInList(unittest.TestCase):
    def test_count_element_present_multiple_times(self):
        """Test counting an element that appears multiple times"""
        self.assertEqual(count_in_list([1, 2, 3, 2, 4, 2], 2), 3)

    def test_count_element_not_present(self):
        """Test counting an element that doesn't exist in the list"""
        self.assertEqual(count_in_list([1, 2, 3, 4], 5), 0)

    def test_count_in_empty_list(self):
        """Test counting in an empty list"""
        self.assertEqual(count_in_list([], 1), 0)

    def test_count_string_element(self):
        """Test counting string elements"""
        self.assertEqual(count_in_list(['a', 'b', 'c', 'a', 'a'], 'a'), 3)

    def test_count_single_occurrence(self):
        """Test counting element with single occurrence"""
        self.assertEqual(count_in_list([1, 2, 3, 4], 3), 1)

    def test_count_all_same_elements(self):
        """Test counting when all elements are the same"""
        self.assertEqual(count_in_list([5, 5, 5, 5], 5), 4)


if __name__ == '__main__':
    unittest.main()
