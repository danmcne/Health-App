import os
import csv
import json
from datetime import datetime

# Define the base directory for the health app
BASE_DIR = os.path.expanduser("~/health_app")

# Function to create user directories
def create_user(username):
    user_dir = os.path.join(BASE_DIR, "users", username)
    os.makedirs(user_dir, exist_ok=True)
    
    subdirs = ["measurements", "exercise", "nutrition", "medication"]
    for subdir in subdirs:
        os.makedirs(os.path.join(user_dir, subdir), exist_ok=True)
    
    print(f"User '{username}' directory created at {user_dir}")

# Function to initialize CSV file with headers if not exists
def initialize_csv(file_path, headers):
    if not os.path.exists(file_path):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)

# Function to add a health record
def add_health_record(username, category, record_type, headers, data):
    file_path = os.path.join(BASE_DIR, "users", username, category, f"{record_type}.csv")
    initialize_csv(file_path, headers)
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now()] + data)
    print(f"Record added to {file_path}")

# Function to view health records
def view_health_records(username, category, record_type):
    file_path = os.path.join(BASE_DIR, "users", username, category, f"{record_type}.csv")
    if not os.path.exists(file_path):
        print(f"No records found for {record_type} in {category}")
        return
    
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Function to initialize the base directory and config file
def initialize_app():
    os.makedirs(BASE_DIR, exist_ok=True)
    config_path = os.path.join(BASE_DIR, "config.json")
    users_path = os.path.join(BASE_DIR, "users.json")
    menus_path = os.path.join(BASE_DIR, "menus.json")
    
    default_config = {
        "version": "1.0",
        "created_at": str(datetime.now()),
        "default_units": "metric"
    }
    
    default_menus = {
        "main_menu": ["Add User", "Configure Settings", "Exercise Menu", "Body Measurements Menu", "Medication Menu", "Nutrition Menu", "View Health Records", "Exit"],
        "exercise_menu": ["Weight Exercises", "Cardio Exercises", "Add New Exercise", "Return to Main Menu"],
        "weight_exercises": ["squat", "ohp", "deadlift", "bench_press"],
        "cardio_exercises": ["running", "treadmill", "cycling", "swimming"],
        "measurements_menu": ["Enter Weight", "Enter Height", "Enter Blood Pressure", "Add New Measurement", "Return to Main Menu"],
        "medications_menu": ["aspirin", "ibuprofen", "acetaminophen", "metformin", "Add New Medication", "Return to Main Menu"],
        "nutrition_menu": ["Enter Meal", "Return to Main Menu"]
    }
    
    if not os.path.exists(config_path):
        with open(config_path, 'w') as config_file:
            json.dump(default_config, config_file)
    
    if not os.path.exists(users_path):
        with open(users_path, 'w') as users_file:
            json.dump({"users": []}, users_file)
    
    if not os.path.exists(menus_path):
        with open(menus_path, 'w') as menus_file:
            json.dump(default_menus, menus_file)

    print("Health app initialized.")

# Function to load a menu from the JSON file
def load_menu(menu_name):
    menus_path = os.path.join(BASE_DIR, "menus.json")
    with open(menus_path, 'r') as menus_file:
        menus = json.load(menus_file)
    return menus.get(menu_name, [])

# Function to save the updated menu back to the JSON file
def save_menu(menu_name, menu_items):
    menus_path = os.path.join(BASE_DIR, "menus.json")
    with open(menus_path, 'r+') as menus_file:
        menus = json.load(menus_file)
        menus[menu_name] = menu_items
        menus_file.seek(0)
        json.dump(menus, menus_file, indent=4)

# Function to display a menu and get the user's choice
def display_menu(menu_name):
    menu_items = load_menu(menu_name)
    for i, item in enumerate(menu_items, start=1):
        print(f"{i}. {item}")
    return menu_items

# Function to add a new item to a menu
def add_menu_item(menu_name, item_name):
    menu_items = load_menu(menu_name)
    menu_items.insert(len(menu_items) - 1, item_name)  # Insert before the last item (Return option)
    save_menu(menu_name, menu_items)

# Exercise Menu
def exercise_menu(username):
    while True:
        print("\nExercise Menu")
        exercise_options = display_menu("exercise_menu")
        
        choice = input(f"Enter your choice (1-{len(exercise_options)}): ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(exercise_options):
            selected_option = exercise_options[int(choice) - 1]
            
            if selected_option == "Weight Exercises":
                weight_exercise_menu(username)
            elif selected_option == "Cardio Exercises":
                cardio_exercise_menu(username)
            elif selected_option == "Add New Exercise":
                add_new_exercise(username)
            elif selected_option == "Return to Main Menu":
                break
        else:
            print("Invalid choice. Please try again.")

def weight_exercise_menu(username):
    while True:
        print("\nWeight Exercises")
        weight_exercises = load_menu("weight_exercises")
        
        for i, exercise in enumerate(weight_exercises, start=1):
            print(f"{i}. {exercise.replace('_', ' ').title()}")
        print(f"{len(weight_exercises) + 1}. Return to Exercise Menu")
        
        choice = input(f"Choose an exercise (1-{len(weight_exercises) + 1}): ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(weight_exercises):
            exercise = weight_exercises[int(choice) - 1]
            add_weight_exercise_record(username, exercise)
        elif choice == str(len(weight_exercises) + 1):
            break
        else:
            print("Invalid choice. Please try again.")

def cardio_exercise_menu(username):
    while True:
        print("\nCardio Exercises")
        cardio_exercises = load_menu("cardio_exercises")
        
        for i, exercise in enumerate(cardio_exercises, start=1):
            print(f"{i}. {exercise.replace('_', ' ').title()}")
        print(f"{len(cardio_exercises) + 1}. Return to Exercise Menu")
        
        choice = input(f"Choose an exercise (1-{len(cardio_exercises) + 1}): ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(cardio_exercises):
            exercise = cardio_exercises[int(choice) - 1]
            add_cardio_exercise_record(username, exercise)
        elif choice == str(len(cardio_exercises) + 1):
            break
        else:
            print("Invalid choice. Please try again.")

def add_weight_exercise_record(username, exercise):
    config_path = os.path.join(BASE_DIR, "config.json")
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)

    unit_system = config.get("default_units", "metric")
    
    weight = input(f"Enter weight lifted ({unit_system}): ").strip()
    reps = input("Enter number of reps: ").strip()
    rir = input("Enter reps in reserve (RIR): ").strip()
    rpe = input("Enter rate of perceived exertion (RPE): ").strip()

    headers = ["Timestamp", "Weight", "Reps", "RIR", "RPE"]
    add_health_record(username, "exercise", exercise, headers, [weight, reps, rir, rpe])

def add_cardio_exercise_record(username, exercise):
    duration = input("Enter duration (minutes): ").strip()
    distance = input("Enter distance (km): ").strip()

    headers = ["Timestamp", "Duration", "Distance"]
    add_health_record(username, "exercise", exercise, headers, [duration, distance])

def add_new_exercise(username):
    exercise_name = input("Enter the name of the new exercise: ").strip().lower().replace(' ', '_')
    exercise_type = input("Is this a weight (w) or cardio (c) exercise? ").strip().lower()

    if exercise_type == 'w':
        add_menu_item("weight_exercises", exercise_name)
    elif exercise_type == 'c':
        add_menu_item("cardio_exercises", exercise_name)
    else:
        print("Invalid exercise type. Please try again.")
        return

    print(f"New exercise '{exercise_name.replace('_', ' ').title()}' added.")

# Main Menu
def main_menu():
    while True:
        print("\nHealth App Main Menu")
        main_menu_options = display_menu("main_menu")
        
        choice = input(f"Enter your choice (1-{len(main_menu_options)}): ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(main_menu_options):
            selected_option = main_menu_options[int(choice) - 1]
            
            if selected_option == "Add User":
                username = input("Enter username: ").strip()
                create_user(username)
            elif selected_option == "Configure Settings":
                # Configuration settings can be handled here
                print("Configuration settings feature is not yet implemented.")
            elif selected_option == "Exercise Menu":
                username = input("Enter username: ").strip()
                exercise_menu(username)
            elif selected_option == "Body Measurements Menu":
                username = input("Enter username: ").strip()
                measurements_menu(username)
            elif selected_option == "Medication Menu":
                username = input("Enter username: ").strip()
                medication_menu(username)
            elif selected_option == "Nutrition Menu":
                username = input("Enter username: ").strip()
                nutrition_menu(username)
            elif selected_option == "View Health Records":
                username = input("Enter username: ").strip()
                view_health_records(username, "exercise", "weight_exercises")
                view_health_records(username, "exercise", "cardio_exercises")
                # Add similar calls for other record types as needed
            elif selected_option == "Exit":
                print("Exiting the Health App. Goodbye!")
                break
        else:
            print("Invalid choice. Please try again.")

# Body Measurements Menu
def measurements_menu(username):
    while True:
        print("\nBody Measurements Menu")
        measurements_options = display_menu("measurements_menu")
        
        choice = input(f"Enter your choice (1-{len(measurements_options)}): ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(measurements_options):
            selected_option = measurements_options[int(choice) - 1]
            
            if selected_option == "Enter Weight":
                weight = input("Enter weight (kg): ").strip()
                headers = ["Timestamp", "Weight"]
                add_health_record(username, "measurements", "weight", headers, [weight])
            elif selected_option == "Enter Height":
                height = input("Enter height (cm): ").strip()
                headers = ["Timestamp", "Height"]
                add_health_record(username, "measurements", "height", headers, [height])
            elif selected_option == "Enter Blood Pressure":
                bp = input("Enter blood pressure (e.g., 120/80): ").strip()
                headers = ["Timestamp", "Blood Pressure"]
                add_health_record(username, "measurements", "blood_pressure", headers, [bp])
            elif selected_option == "Add New Measurement":
                print("Add new measurement functionality is not yet implemented.")
            elif selected_option == "Return to Main Menu":
                break
        else:
            print("Invalid choice. Please try again.")

# Medication Menu
def medication_menu(username):
    while True:
        print("\nMedication Menu")
        medication_options = display_menu("medications_menu")
        
        choice = input(f"Enter your choice (1-{len(medication_options)}): ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(medication_options):
            selected_option = medication_options[int(choice) - 1]
            
            if selected_option == "Add New Medication":
                medication_name = input("Enter the name of the new medication: ").strip().lower()
                add_menu_item("medications_menu", medication_name)
            elif selected_option == "Return to Main Menu":
                break
        else:
            print("Invalid choice. Please try again.")

# Nutrition Menu
def nutrition_menu(username):
    while True:
        print("\nNutrition Menu")
        nutrition_options = display_menu("nutrition_menu")
        
        choice = input(f"Enter your choice (1-{len(nutrition_options)}): ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(nutrition_options):
            selected_option = nutrition_options[int(choice) - 1]
            
            if selected_option == "Enter Meal":
                meal_description = input("Enter meal description: ").strip()
                calories = input("Enter calories: ").strip()
                headers = ["Timestamp", "Meal Description", "Calories"]
                add_health_record(username, "nutrition", "meal", headers, [meal_description, calories])
            elif selected_option == "Return to Main Menu":
                break
        else:
            print("Invalid choice. Please try again.")

# Initialize the application
initialize_app()

# Start the main menu
if __name__ == "__main__":
    main_menu()

