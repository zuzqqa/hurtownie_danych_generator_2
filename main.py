# main.py

from data_generator.data_generator import (
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

def run_data_generation():
    """Run the entire data generation process."""
    print("Generating data...")
    
    # Call each data generation function
    generate_dates()
    generate_times()
    generate_ratings()
    generate_passengers()
    generate_employees()
    generate_check_ins()
    generate_boarding_passes()
    generate_security_checks()

    # Save data to CSV files
    save_data_to_csv()

    print("Data generation complete!")

if __name__ == "__main__":
    # Run the data generation process
    run_data_generation()
