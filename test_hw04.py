import unittest
from hw04a import get_repo_list


class Test_GetRepoList(unittest.TestCase):
    def test_correct_response(self):
        correct_response = [('electron-app-iot', 6), ('SSW345-hw1', 3), ('SSW345-lab1', 1), ('SSW567-hw0', 2),
                            ('SSW567-hw1', 7), ('SSW567-hw2a', 11), ('SSW567-HW4a', 5), ('Superalgos', 30)]
        self.assertEqual(get_repo_list("amitb913"), correct_response)
    def test_nonexistent_user(self):
        userId = "sdiofjasdiofjasdiofjsdafunsuadofn"
        self.assertEqual(get_repo_list(userId), "Error retrieving repo data with status code 404: Not Found")

if __name__ == '__main__':
    unittest.main()
