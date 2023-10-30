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

    @patch.object(GithubOrgClient, "_public_repos_url",
                  new_callable=PropertyMock)
    @patch("client.get_json", return_value=[{"name": "repo1"},
                                            {"name": "repo2"}])
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """_summary_

        Args:
                mock_get_json (MagicMock): _description_
        """
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "episodes.dart",
                    "kratu",
                ],
            )
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()
