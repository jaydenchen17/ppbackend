from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize an empty dictionary to store user data
user_data = {}

@app.route('/api/saveUserData', methods=['POST'])
def save_user_data():
    data = request.json
    username = data.get('username')
    user_data[username] = data  # Store user data in the dictionary
    return jsonify({"message": "Data saved successfully"})

if __name__ == '__main__':
    app.run(debug=True)