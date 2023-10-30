#!/usr/bin/env python3

"test_client.py - Parameterize and patch as decorators"

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from parameterized import parameterized_class
import fixtures


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

    @patch.object(GithubOrgClient, "_public_repos_url",
                  new_callable=PropertyMock)
    @patch("client.get_json", return_value=[{"name": "repo1"},
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

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license_key, has_license):
        """
        Test function for `GithubOrgClient.has_license`. It asserts if the
          function returns
        the expected output for given inputs.

        Args:
            repo (dict): A dictionary representing a repository with a license.
            license_key (str): The key of the license to check for.
            has_license (bool): Whether the repo is expected to have
              the license.
        """

        test_class_instance = GithubOrgClient("test")
        self.assertEqual(
            test_class_instance.has_license(repo, license_key), has_license
        )


@parameterized_class([
    {"org_payload": fixtures.org_payload,
     "repos_payload": fixtures.repos_payload,
     "expected_repos": fixtures.expected_repos,
     "apache2_repos": fixtures.apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient"""

    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up the test class. This method is called once for the entire
          TestCase before any test methods are executed.
        """
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            """
            Helper function to return payload for a given URL.
            """
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """
        Test public_repos method of GithubOrgClient. This method tests that
          the public_repos method of a GithubOrgClient instance returns
            the expected list of repositories.
        """
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )
