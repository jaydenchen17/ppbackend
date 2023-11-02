import json

class UserData:
    def __init__(self, username, age, weight, height, activity, gender, calorie_maintenance, meal_plan, meal_plan_number):
        self.username = username
        self.age = age
        self.weight = weight
        self.height = height
        self.activity = activity
        self.gender = gender
        self.calorie_maintenance = calorie_maintenance
        self.meal_plan = meal_plan
        self.meal_plan_number = meal_plan_number

    def to_dict(self):
        return {
            "username": self.username,
            "age": self.age,
            "weight": self.weight,
            "height": self.height,
            "activity": self.activity,
            "gender": self.gender,
            "calorie_maintenance": self.calorie_maintenance,
            "meal_plan": self.meal_plan,
            "meal_plan_number": self.meal_plan_number
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data.get("username"),
            data.get("age"),
            data.get("weight"),
            data.get("height"),
            data.get("activity"),
            data.get("gender"),
            data.get("calorie_maintenance"),
            data.get("meal_plan"),
            data.get("meal_plan_number")
        )
