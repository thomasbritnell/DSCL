import unittest
from app import app

class ChallengeApiTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_challenges_list(self):
        response = self.client.get('/api/challenges')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_challenge_detail(self):
        # Assuming challenge with id 1 exists
        response = self.client.get('/api/challenges/1')
        self.assertIn(response.status_code, [200, 404])
        # If found, should be a dict
        if response.status_code == 200:
            self.assertIsInstance(response.json, dict)

if __name__ == "__main__":
    unittest.main()
