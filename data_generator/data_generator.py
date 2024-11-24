# data_generator/data_generator.py

from faker import Faker
import pandas as pd
import random
from datetime import datetime

# Initialize the Faker library for fake data generation
fake = Faker()

# Parameters for the number of data entries to generate
passengers_num = 5
check_ins_num = 5
employees_num = 5
boarding_passes_num = 5
security_checks_num = 5

# Lists to store generated data
passengers = []
check_ins = []
employees = []
boarding_passes = []
security_checks = []
ratings = []
dates = []
times = []

# Function to generate date-related data
def generate_dates():
    # Create a range of unique dates
    unique_dates = pd.date_range(start="2023-01-01", periods=10).to_pydatetime().tolist()
    # Create a mapping between date strings and date IDs
    date_id_map = {date.strftime("%Y-%m-%d"): i + 1 for i, date in enumerate(unique_dates)}
    
    # Loop through each date and generate the data
    for date in unique_dates:
        dates.append({
            "DateID": date_id_map[date.strftime("%Y-%m-%d")],
            "Date": date.strftime("%Y-%m-%d"),
            "Day": date.day,
            "Month": date.month,
            "Year": date.year,
            "DayOfWeek": date.strftime("%A"),
            "IsWeekend": int(date.weekday() >= 5),
            "WeekOfYear": date.isocalendar()[1]
        })

# Function to generate time-related data
def generate_times():
    # Generate random times and their shifts
    for i in range(1, 11):
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        shift = "morning" if hour < 12 else "afternoon" if hour < 18 else "night"
        times.append({
            "TimeID": i,
            "Time": f"{hour:02}:{minute:02}",
            "Hour": hour,
            "Minute": minute,
            "Shift": shift
        })

# Function to generate ratings data (for services)
def generate_ratings():
    rating_categories = ["Service quality", "Cleanliness", "Comfort"]
    for i in range(1, 6):
        ratings.append({
            "RatingID": i,
            "RatingCategory": random.choice(rating_categories),
            "RatingDescription": fake.sentence(nb_words=6)
        })

# Function to generate passengers data
def generate_passengers():
    for i in range(1, passengers_num + 1):
        passengers.append({
            "PassengerID": i,
            "FirstAndLastName": fake.first_name() + " " + fake.last_name(),
            "DocumentType": random.choice(["ID", "Passport"]),
            "Nationality": fake.country(),
            "IsCurrent": int(random.choice([True, False]))
        })

# Function to generate employees data
def generate_employees():
    for i in range(1, employees_num + 1):
        employees.append({
            "EmployeeID": i,
            "EmployeeName": f"{fake.first_name()} {fake.last_name()}",
            "ExperienceCategory": random.choice(["0-2", "3-5", "5-10"]),
            "AgeCategory": random.choice(["20-25", "25-30", "30-40"]),
            "Gender": random.choice(["Male", "Female"]),
            "IsCurrent": int(random.choice([True, False]))
        })

# Function to generate check-in data
def generate_check_ins():
    for i in range(1, check_ins_num + 1):
        baggage_count = random.randint(1, 3)
        check_in_duration = random.randint(5, 30)
        check_in_date = random.choice(dates)
        check_ins.append({
            "CheckInID": i,
            "PassengerID": random.randint(1, passengers_num),
            "EmployeeID": random.randint(1, employees_num),
            "BoardingPassID": i,
            "DateID": check_in_date["DateID"],
            "TimeID": random.randint(1, len(times)),
            "RatingID": random.randint(1, len(ratings)),
            "CheckInDuration": check_in_duration,
            "BaggageCount": baggage_count,
            "ServiceRating": round(random.uniform(1, 5), 2)
        })

# Function to generate boarding passes data
def generate_boarding_passes():
    for i in range(1, boarding_passes_num + 1):
        boarding_passes.append({
            "BoardingPassID": i,
            "Gate": f"{random.randint(1, 20)}A",
            "SeatNumber": f"{random.randint(1, 30)}{random.choice(['A', 'B', 'C', 'D'])}",
            "Destination": fake.city(),
            "FlightNumber": fake.bothify(text='FL###')
        })

# Function to generate security checks data
def generate_security_checks():
    for i in range(1, security_checks_num + 1):
        security_duration = random.randint(1, 10)
        security_checks.append({
            "SecurityCheckID": i,
            "EmployeeID": random.randint(1, employees_num),
            "BoardingPassID": random.randint(1, boarding_passes_num),
            "TimeID": random.randint(1, len(times)),
            "DateID": random.randint(1, len(dates)),
            "RatingID": random.randint(1, len(ratings)),
            "SecurityDuration": security_duration,
            "ClearanceStatus": random.choice(["Approved", "Denied"]),
            "ServiceRating": round(random.uniform(1, 5), 2)
        })

# Function to save data to CSV files
def save_data_to_csv():
    df_dates = pd.DataFrame(dates)
    df_times = pd.DataFrame(times)
    df_ratings = pd.DataFrame(ratings)
    df_passengers = pd.DataFrame(passengers)
    df_employees = pd.DataFrame(employees)
    df_check_ins = pd.DataFrame(check_ins)
    df_boarding_passes = pd.DataFrame(boarding_passes)
    df_security_checks = pd.DataFrame(security_checks)

    df_dates.to_csv("data/dates.csv", index=False)
    df_times.to_csv("data/times.csv", index=False)
    df_ratings.to_csv("data/ratings.csv", index=False)
    df_passengers.to_csv("data/passengers.csv", index=False)
    df_employees.to_csv("data/employees.csv", index=False)
    df_check_ins.to_csv("data/check_ins.csv", index=False)
    df_boarding_passes.to_csv("data/boarding_passes.csv", index=False)
    df_security_checks.to_csv("data/security_checks.csv", index=False)
