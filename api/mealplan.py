from flask import Flask, render_template
from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource

mealplan_api = Blueprint('mealplan_api', __name__, url_prefix='/api/mealplans')
api = Api(mealplan_api)

# Initialize a list to store meal plan links (in a real application, use a database)
meal_plans = [
    {"name": "Meal Plan 1", "min_calories": 0, "max_calories": 1000},
    {"name": "Meal Plan 2", "min_calories": 1000, "max_calories": 1250},
    {"name": "Meal Plan 3", "min_calories": 1251, "max_calories": 1500},
    {"name": "Meal Plan 4", "min_calories": 1501, "max_calories": 1750},
    {"name": "Meal Plan 5", "min_calories": 1751, "max_calories": 2000},
    {"name": "Meal Plan 6", "min_calories": 2001, "max_calories": 2250},
    {"name": "Meal Plan 7", "min_calories": 2251, "max_calories": 2500},
    {"name": "Meal Plan 8", "min_calories": 2501, "max_calories": 2750},
    {"name": "Meal Plan 9", "min_calories": 2751, "max_calories": 3000},
    {"name": "Meal Plan 10", "min_calories": 3001, "max_calories": 3250},
    {"name": "Meal Plan 11", "min_calories": 3251, "max_calories": 3500},
    {"name": "Meal Plan 12", "min_calories": 3501, "max_calories": 3750},
    {"name": "Meal Plan 13", "min_calories": 3751, "max_calories": 4000},
    {"name": "Meal Plan 14", "min_calories": 4001, "max_calories": 4250},
    {"name": "Meal Plan 15", "min_calories": 4251, "max_calories": 4500},
    {"name": "Meal Plan 16", "min_calories": 4501, "max_calories": 4750},

    
    # Add more meal plans and ranges as needed
]
class MealPlansAPI:
    class _Create(Resource):
        def calculate_meal_plan(client_calories):
            for plan in meal_plans:
                if plan["min_calories"] <= client_calories <= plan["max_calories"]:
                    return plan["name"]
            return "Unknown"

        def post(self):
            data = request.get_json()
            meal_plan_link = data.get('/ppfrontend/mealplans/mealplan${mealPlanNumber}')
            meal_plans.append(meal_plan_link)
            return jsonify({"message": "Meal plan link created"})

    class _Read(Resource):
        def get(self):
            return jsonify(meal_plans)

api.add_resource(MealPlansAPI._Create, '/create')
api.add_resource(MealPlansAPI._Read, '/list')

if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)
    app.register_blueprint(mealplan_api)

    app.run(debug=True)
