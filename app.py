import logging
from flask import Flask, request, jsonify
import string
import os

# Change the name of the app
alphabet_checker = Flask(__name__)

# Create a log file in the same directory
log_file = 'alphabet_checker.log'
logging.basicConfig(filename=log_file, level=logging.INFO, 
                    format='%(asctime)s %(levelname)s %(message)s')

# Function to check if the string contains all letters of the alphabet
def contains_all_letters(input_string):
    alphabet_set = set(string.ascii_lowercase)  # Set of all lowercase letters
    input_string = input_string.lower()  # Convert the input string to lowercase
    input_set = set(filter(str.isalpha, input_string))  # Get only alphabetic characters
    
    # Print the alphabet set and the input set
    #print(f"Alphabet Set: {alphabet_set}")
    #print(f"Input Set (alphabetic characters only): {input_set}")
    
    # Log the input string and the sets for debugging
    logging.info(f"Input String: {input_string}")
    logging.info(f"Alphabet Set: {alphabet_set}")
    logging.info(f"Input Set: {input_set}")
    result = alphabet_set.issubset(input_set)
    return result

# Define a route for the service
@alphabet_checker.route('/check_alphabet', methods=['POST'])
def check_alphabet():
    data = request.json  # Get the JSON data from the request body
    input_string = data.get('input_string', '')
    
    if not input_string:
        return jsonify({'error': 'No input string provided'}), 400
    
    # Call the function to check if the input string contains all letters
    result = contains_all_letters(input_string)
    
    # Log the result of the check
    logging.info(f"Contains all letters: {result}")
    
    return jsonify({'contains_all_letters': result})

if __name__ == '__main__':
    # Ensure the log file is created in the same directory
    log_dir = os.path.dirname(os.path.realpath(__file__))
    log_file_path = os.path.join(log_dir, log_file)
    print(f"Logging to: {log_file_path}")
    
    alphabet_checker.run(debug=True)
