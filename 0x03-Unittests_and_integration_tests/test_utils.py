#!/usr/bin/env python3

"Parameterize a unit test"

import unittest
from parameterized import parameterized
import utils


class TestAccessNestedMap(unittest.TestCase):
    """
    This class inherits from `unittest.TestCase` and contains unit test for the
    `utils.access_nested_map` function.
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected_output):
        """
        Test function for `utils.access_nested_map`. It asserts if the
          function returns
        the expected output for given inputs. The test cases are provided
          by the
        `parameterized.expand` decorator.

        Args:
            nested_map (dict): The nested map to be tested.
            path (tuple): The path to the value in the map.
            expected_output (Any): The expected result from the function.
        """
        self.assertEqual(utils.access_nested_map(nested_map, path),
                         expected_output)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError, "a"),
            ({"a": 1}, ("a", "b"), KeyError, "b"),
        ]
    )
    def test_access_nested_map_exception(
        self, nested_map, path, expected_exception, expected_message
    ):
        """
        Test function for `utils.access_nested_map` to check if it raises a
          KeyError.
        """
        with self.assertRaises(expected_exception) as context:
            utils.access_nested_map(nested_map, path)

        self.assertEqual(
            str(context.exception), f"'{expected_message}' not found in nested"
            " map"
        )
