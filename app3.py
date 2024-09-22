from flask import Flask, request, jsonify
import string

app = Flask(__name__)

@app.route('/check_alphabet', methods=['POST'])
def check_alphabet():
    data = request.get_json()
    input_string = data.get('input', '')
    
    # Create a set of all alphabet letters
    alphabet_set = set(string.ascii_lowercase)
    
    # Create a set of letters in the input string
    input_set = set(input_string.lower())
    
    # Check if all alphabet letters are present in the input set
    if alphabet_set.issubset(input_set):
        return jsonify({"contains_all_letters": True})
    else:
        return jsonify({"contains_all_letters": False})

if __name__ == '__main__':
    app.run(debug=True)
