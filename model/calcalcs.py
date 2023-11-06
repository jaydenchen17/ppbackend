import json
import random

calorie_data = []

# Initialize calorie data
def initCalories():
    # Add initial calorie data, if needed
    pass

# Add a new calorie entry
def addCalorieEntry(calorie_entry):
    calorie_data.append(calorie_entry)
    return calorie_entry

# Get all calorie entries
def getCalorieEntries():
    return calorie_data

# Get a specific calorie entry by ID
def getCalorieEntry(calorie_id):
    if 0 <= calorie_id < len(calorie_data):
        return calorie_data[calorie_id]
    else:
        return None

# Update a calorie entry by ID
def updateCalorieEntry(calorie_id, updated_entry):
    if 0 <= calorie_id < len(calorie_data):
        calorie_data[calorie_id] = updated_entry
        return updated_entry
    else:
        return None

# Delete a calorie entry by ID
def deleteCalorieEntry(calorie_id):
    if 0 <= calorie_id < len(calorie_data):
        deleted_entry = calorie_data.pop(calorie_id)
        return deleted_entry
    else:
        return None

# Test the Calorie Model
if __name__ == "__main__":
    initCalories()  # initialize calorie data, if needed
    
    # Add a sample calorie entry
    sample_entry = {
        "user_id": 1,
        "date": "2023-11-04",
        "calories": 500
    }
    added_entry = addCalorieEntry(sample_entry)
    print("Added calorie entry:")
    print(added_entry)
    
    # Get all calorie entries
    all_entries = getCalorieEntries()
    print("\nAll calorie entries:")
    for entry in all_entries:
        print(entry)