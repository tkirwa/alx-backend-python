#!/usr/bin/env python3

"Parameterize a unit test"

import unittest
from parameterized import parameterized
import utils
import unittest
from unittest.mock import patch, Mock
from utils import memoize


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

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test function for `utils.access_nested_map`. It asserts if the
          function raises a
        KeyError with expected message for given inputs. The test cases are
          provided by the
        `parameterized.expand` decorator.

        Args:
            nested_map (dict): The nested map to be tested.
            path (tuple): The path to the value in the map.
        """
        with self.assertRaises(KeyError) as cm:
            utils.access_nested_map(nested_map, path)
        self.assertEqual(cm.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """ Class for Testing Memoize """

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test function for `utils.get_json`. It asserts if the function returns
        the expected output for given inputs. The test cases are provided
          by the
        `parameterized.expand` decorator.

        Args:
            test_url (str): The URL that `get_json` will be called with.
            test_payload (dict): The expected return value from `get_json`.
            mock_get (Mock): The mock object for `requests.get`.
        """
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(utils.get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        """
        Test function for `utils.memoize`. It asserts if the function returns
        the expected output for given inputs and checks if the decorated method
        is called only once.
        """

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method",
                          return_value=42) as mocked_a_method:
            test_class_instance = TestClass()
            self.assertEqual(test_class_instance.a_property, 42)
            self.assertEqual(test_class_instance.a_property, 42)
            mocked_a_method.assert_called_once()
