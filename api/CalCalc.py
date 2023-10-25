from flask import Flask, request, jsonify

app = Flask(  name  )

# Initialize an empty dictionary to store user data
user_data = {}

@app.route('/api/saveUserData', methods=['POST'])
def save_user_data():
    data = request.json

    # Ensure the "username" key is in the data
    if 'username' not in data:
        return jsonify({"error": "Username is required."}), 400

    username = data['username']

    # Store user data in the dictionary
    user_data[username] = data

    return jsonify({"message": "Data saved successfully"})

if __name__ == '__main__':
    app.run(debug=True)