joke_api = __name__ ('joke_api', __name__,
                   url_prefix='/api/jokes')

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/store_user_data', methods=['POST'])
def store_user_data():
    try:
        # Get user data from the request
        user_data = request.get_json()

        # You can perform additional validation and processing here if needed

        # Store the user data in a database or any other storage method
        # Replace this with your actual storage logic
        # For demonstration, we'll just print the data to the console
        print("Received user data:")
        print(user_data)

        # You can return a success message if data is successfully stored
        response = {
            "message": "User data stored successfully."
        }
        return jsonify(response), 201  # 201 Created status code

    except Exception as e:
        # Handle errors or validation failures
        response = {
            "error": "Failed to store user data",
            "details": str(e)
        }
        return jsonify(response), 400  # 400 Bad Request status code

if __name__ == '__main__':
    app.run(debug=True)
