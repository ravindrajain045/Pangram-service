import unittest
import json
import logging
from app import alphabet_checker  # Importing the Flask app instance from your app

# Set up logging
log_file = 'test_alphabet_checker.log'
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

class TestAlphabetChecker(unittest.TestCase):

    # Setup the Flask test client and log file
    def setUp(self):
        self.app = alphabet_checker.test_client()
        self.app.testing = True
        logging.info("=== Starting a new test ===")

    # Test case for a valid pangram (string contains all letters)
    def test_valid_pangram(self):
        input_string = "The quick brown fox jumps over the lazy dog"
        logging.info(f"Test case: Valid Pangram. Input: {input_string}")
        
        response = self.app.post('/check_alphabet', 
                                 data=json.dumps({"input_string": input_string}),
                                 content_type='application/json')
        data = json.loads(response.get_data(as_text=True))

        logging.info(f"Response: {data}")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['contains_all_letters'])

    # Test case for a string missing some letters
    def test_incomplete_string(self):
        input_string = "Hello World"
        logging.info(f"Test case: Incomplete String. Input: {input_string}")
        
        response = self.app.post('/check_alphabet', 
                                 data=json.dumps({"input_string": input_string}),
                                 content_type='application/json')
        data = json.loads(response.get_data(as_text=True))

        logging.info(f"Response: {data}")
        self.assertEqual(response.status_code, 200)
        self.assertFalse(data['contains_all_letters'])

    # Test case for an empty string
    def test_empty_string(self):
        input_string = ""
        logging.info(f"Test case: Empty String. Input: {input_string}")
        
        response = self.app.post('/check_alphabet', 
                                 data=json.dumps({"input_string": input_string}),
                                 content_type='application/json')
        data = json.loads(response.get_data(as_text=True))

        logging.info(f"Response: {data}")
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)

    # Test case for string with numbers and special characters
    def test_string_with_numbers_special_chars(self):
        input_string = "1234!@#$%^&*() The quick brown fox jumps over the lazy dog"
        logging.info(f"Test case: String with Numbers and Special Characters. Input: {input_string}")
        
        response = self.app.post('/check_alphabet', 
                                 data=json.dumps({"input_string": input_string}),
                                 content_type='application/json')
        data = json.loads(response.get_data(as_text=True))

        logging.info(f"Response: {data}")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['contains_all_letters'])

    # Tear down after each test
    def tearDown(self):
        logging.info("=== Test finished ===\n")

if __name__ == '__main__':
    unittest.main()
