from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

fake = Faker()

passengers_num = 5
check_ins_num = 5
employees_num = 5
baggage_num = 10
boarding_passes_num = 5
security_checks_num = 5

passengers = []
check_ins = []
baggages = []
employees = []
boarding_passes = []
security_checks = []
ratings = []
dates = []
times = []

# Wymiar: Data
unique_dates = pd.date_range(start="2023-01-01", periods=10).to_pydatetime().tolist()
date_id_map = {date.strftime("%Y-%m-%d"): i + 1 for i, date in enumerate(unique_dates)}
for date in unique_dates:
    dates.append({
        "DateID": date_id_map[date.strftime("%Y-%m-%d")],
        "Date": date.strftime("%Y-%m-%d"),
        "Day": date.day,
        "Month": date.month,
        "Year": date.year,
        "DayOfWeek": date.strftime("%A"),
        "IsWeekend": date.weekday() >= 5,
        "WeekOfYear": date.isocalendar()[1]
    })

# Wymiar: Czas
for i in range(1, 11):
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    shift = "ranna" if hour < 12 else "popołudniowa" if hour < 18 else "nocna"
    times.append({
        "TimeID": i,
        "Time": f"{hour:02}:{minute:02}",
        "Hour": hour,
        "Minute": minute,
        "Shift": shift
    })

# Wymiar: Ocena
rating_categories = ["Jakość obsługi", "Czystość", "Komfort"]
for i in range(1, 6):
    ratings.append({
        "RatingID": i,
        "RatingCategory": random.choice(rating_categories),
        "RatingDescription": fake.sentence(nb_words=6)
    })

# Tabela: Pasażerowie
for i in range(1, passengers_num + 1):
    passengers.append({
        "PassengerID": i,
        "FirstName": fake.first_name(),
        "LastName": fake.last_name(),
        "DocumentType": random.choice(["ID", "Passport"]),
        "Nationality": fake.country(),
        "IsCurrent": random.choice([True, False])
    })

# Tabela: Pracownicy
for i in range(1, employees_num + 1):
    employees.append({
        "EmployeeID": i,
        "EmployeeName": f"{fake.first_name()} {fake.last_name()}",
        "ExperienceCategory": random.choice(["0-2", "3-5", "5-10"]),
        "AgeCategory": random.choice(["20-25", "25-30", "30-40"]),
        "Gender": random.choice(["Male", "Female"]),
        "IsCurrent": random.choice([True, False])
    })

# Tabela: Odprawy
for i in range(1, check_ins_num + 1):
    baggage_count = random.randint(1, 3)
    check_in_duration = random.randint(5, 30)
    check_in_date = random.choice(unique_dates)
    check_ins.append({
        "CheckInID": i,
        "PassengerID": random.randint(1, passengers_num),
        "EmployeeID": random.randint(1, employees_num),
        "BoardingPassID": i,
        "DateID": date_id_map[check_in_date.strftime("%Y-%m-%d")],
        "TimeID": random.randint(1, len(times)),
        "RatingID": random.randint(1, len(ratings)),
        "CheckInDuration": check_in_duration,
        "BaggageCount": baggage_count,
        "ServiceRating": round(random.uniform(1, 5), 2)
    })

# Tabela: Bagaże
for i in range(1, baggage_num + 1):
    baggages.append({
        "BaggageID": i,
        "CheckInID": random.randint(1, check_ins_num),
        "Weight": round(random.uniform(5, 30), 2)
    })

# Tabela: Karty pokładowe
for i in range(1, boarding_passes_num + 1):
    boarding_passes.append({
        "BoardingPassID": i,
        "Gate": f"{random.randint(1, 20)}A",
        "SeatNumber": f"{random.randint(1, 30)}{random.choice(['A', 'B', 'C', 'D'])}",
        "Destination": fake.city(),
        "FlightNumber": fake.bothify(text='FL###')
    })

# Tabela: Kontrola bezpieczeństwa
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
        "ClearanceStatus": random.choice(["Zatwierdzono", "Odmowa"]),
        "ServiceRating": round(random.uniform(1, 5), 2)
    })

# Zapisywanie do plików CSV
df_dates = pd.DataFrame(dates)
df_times = pd.DataFrame(times)
df_ratings = pd.DataFrame(ratings)
df_passengers = pd.DataFrame(passengers)
df_employees = pd.DataFrame(employees)
df_check_ins = pd.DataFrame(check_ins)
df_baggages = pd.DataFrame(baggages)
df_boarding_passes = pd.DataFrame(boarding_passes)
df_security_checks = pd.DataFrame(security_checks)

df_dates.to_csv("dates.csv", index=False)
df_times.to_csv("times.csv", index=False)
df_ratings.to_csv("ratings.csv", index=False)
df_passengers.to_csv("passengers.csv", index=False)
df_employees.to_csv("employees.csv", index=False)
df_check_ins.to_csv("check_ins.csv", index=False)
df_baggages.to_csv("baggages.csv", index=False)
df_boarding_passes.to_csv("boarding_passes.csv", index=False)
df_security_checks.to_csv("security_checks.csv", index=False)
