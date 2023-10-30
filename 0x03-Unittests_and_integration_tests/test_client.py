#!/usr/bin/env python3

"test_client.py - Parameterize and patch as decorators"

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([("google"), ("abc")])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name, mock_get_json):
        """
        Test function for `GithubOrgClient.org`. It asserts if the function
          returns
        the expected output for given inputs and checks if the decorated method
        is called only once.
        """

        test_class_instance = GithubOrgClient(org_name)
        self.assertEqual(test_class_instance.org, {"payload": True})
        mock_get_json.assert_called_once()

    @patch.object(GithubOrgClient, "org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test function for `GithubOrgClient._public_repos_url`. It asserts if
          the function returns
        the expected output for given inputs.
        """

        json_payload = {"repos_url": "World"}
        mock_org.return_value = json_payload

        test_class_instance = GithubOrgClient("test")
        self.assertEqual(
            test_class_instance._public_repos_url, json_payload["repos_url"]
        )

    @patch.object(GithubOrgClient, '_public_repos_url',
                  new_callable=PropertyMock)
    @patch('client.get_json', return_value=[{"name": "repo1"},
                                            {"name": "repo2"}])
    def test_public_repos(self, mock_get_json, mock_public_repos_url):
        """
        Test function for `GithubOrgClient.public_repos`. It asserts if the
          function returns
        the expected output for given inputs and checks if the decorated method
        is called only once.
        """

        mock_public_repos_url.return_value = "https://api.github.com"
        "/orgs/test/repos"

        test_class_instance = GithubOrgClient("test")
        self.assertEqual(test_class_instance.public_repos(),
                         ["repo1", "repo2"])

        mock_get_json.assert_called_once()
        mock_public_repos_url.assert_called_once()
