from flask import Flask, request, jsonify

app = Flask(__name)

# Your database (you can replace this with your preferred database setup)
userData = []

# Harris-Benedict equation constants
MALE_MULTIPLIER = 88.362
FEMALE_MULTIPLIER = 447.593
HEIGHT_MULTIPLIER = 3.351
WEIGHT_MULTIPLIER = 4.799
AGE_MULTIPLIER = 5.677

@app.route('/save_data', methods=['POST'])
def save_data():
    data = {
        'age': int(request.form['age']),
        'weight': float(request.form['weight']),
        'height': float(request.form['height']),
        'activity': request.form['activity'],
        'username': request.form['username'],
    }

    # Calculate BMR (Basal Metabolic Rate) using the Harris-Benedict equation
    if request.form['gender'] == 'male':
        bmr = MALE_MULTIPLIER + WEIGHT_MULTIPLIER * data['weight'] + HEIGHT_MULTIPLIER * data['height'] - AGE_MULTIPLIER * data['age']
    else:
        bmr = FEMALE_MULTIPLIER + WEIGHT_MULTIPLIER * data['weight'] + HEIGHT_MULTIPLIER * data['height'] - AGE_MULTIPLIER * data['age']

    # Adjust BMR based on activity level
    activity_multipliers = {
        'sedentary': 1.2,
        'lightly_active': 1.375,
        'moderately_active': 1.55,
        'very_active': 1.725
    }
    calorie_maintenance = bmr * activity_multipliers[data['activity']]

    data['calorie_maintenance'] = calorie_maintenance

    # Store the data in your database or any other data storage mechanism
    userData.append(data)

    # Return the data including the calculated calorie maintenance
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
