


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