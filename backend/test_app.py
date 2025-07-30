import unittest
from app import app

class ChallengeApiTestCase(unittest.TestCase):
    """
    TestCase for Challenge API endpoints.
    Tests list and detail endpoints for expected responses and types.
    """
    def setUp(self):
        """Set up test client before each test."""
        self.client = app.test_client()

    def test_challenges_list(self):
        """Test that /api/challenges returns a list and status 200."""
        response = self.client.get('/api/challenges')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_challenge_detail(self):
        """Test that /api/challenges/<id> returns 200 or 404, and dict if found."""
        # Assuming challenge with id 1 exists
        response = self.client.get('/api/challenges/1')
        self.assertIn(response.status_code, [200, 404])
        # If found, should be a dict
        if response.status_code == 200:
            self.assertIsInstance(response.json, dict)

if __name__ == "__main__":
    unittest.main()
