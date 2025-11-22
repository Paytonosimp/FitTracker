import json
import os
from datetime import datetime

DATA_FILE = "data.json"

def load_data():
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                return json.load(f)
    except json.JSONDecodeError:
        print("⚠️ Data file corrupted — starting fresh.")
        return {"user": {}, "workouts": [], "meals": []}

    return {"user": {}, "workouts": [], "meals": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input — enter a number.")

def get_user_info(data):
    if not data["user"]:
        print("Welcome! Let's get you set up.")
        name = input("What's your name? ")
        height = get_valid_number("Height in meters (e.g. 1.75): ")
        weight = get_valid_number("Weight in kg (e.g. 75): ")
        bmi = round(weight / (height ** 2), 2)
        data["user"] = {"name": name, "height": height, "weight": weight, "bmi": bmi}
        save_data(data)
    return data["user"]

def log_workout(data):
    workout = input("Enter workout (e.g. Running): ")
    duration = int(get_valid_number("Duration in minutes: "))
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    data["workouts"].append({"activity": workout, "duration": duration, "time": timestamp})
    print(f"Workout logged: {workout} for {duration} minutes.")
    save_data(data)

def log_meal(data):
    meal = input("Enter meal name (e.g. Chicken Salad): ")
    calories = int(get_valid_number("Enter calories: "))
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    data["meals"].append({"meal": meal, "calories": calories, "time": timestamp})
    print(f"Meal logged: {meal} with {calories} calories.")
    save_data(data)

def delete_workout(data):
    if not data["workouts"]:
        print("No workouts to delete.")
        return

    print("\nWorkout Entries:")
    for i, w in enumerate(data["workouts"], start=1):
        print(f"{i}. {w['activity']} — {w['duration']} mins at {w['time']}")

    idx = int(get_valid_number("Enter number to delete: ")) - 1

    if 0 <= idx < len(data["workouts"]):
        removed = data["workouts"].pop(idx)
        print(f"Deleted workout: {removed['activity']}")
        save_data(data)
    else:
        print("Invalid selection.")

def delete_meal(data):
    if not data["meals"]:
        print("No meals to delete.")
        return

    print("\nMeal Entries:")
    for i, m in enumerate(data["meals"], start=1):
        print(f"{i}. {m['meal']} — {m['calories']} calories at {m['time']}")

    idx = int(get_valid_number("Enter number to delete: ")) - 1

    if 0 <= idx < len(data["meals"]):
        removed = data["meals"].pop(idx)
        print(f"Deleted meal: {removed['meal']}")
        save_data(data)
    else:
        print("Invalid selection.")

def view_summary(data):
    print("\n🔹 Summary of Logged Data 🔹")

    print("Workouts:")
    total_minutes = 0
    
