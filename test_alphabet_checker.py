import unittest
import json
from app import alphabet_checker  # Import the Flask app instance

class TestAlphabetChecker(unittest.TestCase):

    def setUp(self):
        # Set up the Flask test client
        self.app = alphabet_checker.test_client()
        self.app.testing = True

    def test_valid_pangram(self):
        input_string = "The quick brown fox jumps over the lazy dog"
        response = self.app.post('/check_alphabet', 
                                 data=json.dumps({"input_string": input_string}),
                                 content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        result = data['contains_all_letters']
        print(f"Test valid pangram: {result}")
        self.assertTrue(result)

    def test_incomplete_string(self):
        input_string = "Hello World"
        response = self.app.post('/check_alphabet', 
                                 data=json.dumps({"input_string": input_string}),
                                 content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        result = data['contains_all_letters']
        print(f"Test incomplete string: {result}")
        self.assertFalse(result)

    def test_empty_string(self):
        input_string = ""
        response = self.app.post('/check_alphabet', 
                                 data=json.dumps({"input_string": input_string}),
                                 content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)
        print(f"Test empty string: False")  # Since it should return an error

    def test_string_with_numbers_special_chars(self):
        input_string = "1234!@#$%^&*() The quick brown fox jumps over the lazy dog"
        response = self.app.post('/check_alphabet', 
                                 data=json.dumps({"input_string": input_string}),
                                 content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        result = data['contains_all_letters']
        print(f"Test string with numbers and special characters: {result}")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
