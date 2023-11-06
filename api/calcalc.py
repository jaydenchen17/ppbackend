from flask import Flask, request, jsonify
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random


calcalc_api = __name__ ('calcalc_api', __name__,
                   url_prefix='/api/calcalc')

api = Api(calcalc_api)


app = Flask(__name__)

def calculateCalories(user_data):
    age = user_data['age']
    weight = user_data['weight']
    height = user_data['height']
    activity = user_data['activity']
    gender = user_data['gender']

    # Define activity level multipliers
    activity_levels = {
        'sedentary': 1.2,
        'lightly_active': 1.375,
        'moderately_active': 1.55,
        'very_active': 1.725
    }

    # Example calorie calculation (Harris-Benedict equation)
    if gender == 'male':
        calorie_maintenance = (88.362 + 13.397 * weight + 4.799 * height - 5.677 * age) * activity_levels[activity]
    else:
        calorie_maintenance = (447.593 + 9.247 * weight + 3.098 * height - 4.330 * age) * activity_levels[activity]

    return calorie_maintenance


class CalCalcAPI(Resource):
    def post(self):
        try:
            data = request.get_json()

            # Ensure that all required fields are present in the request JSON
            required_fields = ['age', 'weight', 'height', 'activity', 'gender', 'username']
            for field in required_fields:
                if field not in data:
                    return {'error': f"Missing field: {field}"}, 400

            # Calculate calorie maintenance (you can reuse your client-side logic here)
            calorie_maintenance = calculateCalories(data)

            # Calculate the meal plan based on calorie maintenance
            mealPlan = ''
            mealPlanNumber = 0
            if calorie_maintenance < 1000:
                mealPlan = 'Meal Plan 1'
            else:
                mealPlanNumber = (calorie_maintenance - 1000) // 250 + 1
                mealPlan = f'Meal Plan {mealPlanNumber}'

            # Add calorie maintenance and meal plan to the user data
            data['calorie_maintenance'] = calorie_maintenance
            data['mealPlan'] = mealPlan
            data['mealPlanNumber'] = mealPlanNumber

            # Store the user data in a database or any other storage method
            # Replace this with your actual storage logic
            # For demonstration, we'll just print the data to the console
            print("Received user data:")
            print(data)

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

api.add_resource(CalCalcAPI, '/api/calcalc/store_user_data')

if __name__ == "__main__":
    app.run(debug=True)