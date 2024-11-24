# data_generator/__init__.py

# Importing functions from the data generator and main scripts
from .data_generator import (
    generate_dates, 
    generate_times, 
    generate_ratings, 
    generate_passengers, 
    generate_employees, 
    generate_check_ins, 
    generate_boarding_passes, 
    generate_security_checks, 
    save_data_to_csv
)

from ..main import run_data_generation

# Define package version
__version__ = "1.0.0"
