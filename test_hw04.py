"""Suite of test cases for getting the list of repos"""
import unittest
from hw04a import get_repo_list


class TestGetRepoList(unittest.TestCase):
    """Class representing the suite of test cases for getting the list of repos"""

    def test_correct_response(self):
        """
        Tests the correct (expected) response. Keep in mind
        this test may need to be adjusted based on whether the
        user in question makes changes to their repositories
        (either creating/renaming/deleting repos, committing changes)
        """
        correct_response = [('electron-app-iot', 6), ('SSW345-hw1', 3),
                            ('SSW345-lab1', 1), ('SSW345-REST', 2),
                            ('SSW567-hw0', 2), ('SSW567-hw1',
                                                7), ('SSW567-hw2a', 11),
                            ('SSW567-HW4a', 7), ('Superalgos', 30)]
        self.assertEqual(get_repo_list("amitb913"), correct_response)

    def test_nonexistent_user(self):
        """Tests the response for a username
        that does not exist on GitHub"""
        user_id = "sdiofjasdiofjasdiofjsdafunsuadofn"
        self.assertEqual(get_repo_list(
            user_id), "Error retrieving repo data with status code 404: Not Found")

    def test_no_commits(self):
        """Tests the response for a user
        with a repository is empty/has 0 commits"""
        self.assertEqual(get_repo_list(
            "brendanprobst"), "Error retrieving commit data from repo 'ssw215' with status code 200: OK")


if __name__ == '__main__':
    unittest.main()
