# Data Warehouse Generator <img src="https://github.com/bablubambal/All_logo_and_pictures/blob/main/databases/mysql.svg" width="30" /> <img src="https://github.com/bablubambal/All_logo_and_pictures/blob/main/programming%20languages/python.svg" width="30" />

## Description

This project generates test data for a data warehouse related to the aviation industry. The data is generated in CSV format and can later be loaded into a database. The generated data covers various aspects such as passengers, check-ins, boarding passes, security checks, and more.

### Project Contents:
- **Data Generation**: A Python script generates the data using the `Faker` library and saves it in CSV format.
- **SQL Scripts**: SQL scripts to create tables in the database, insert data, and drop tables.
- **Test Data**: The data is generated based on 10 different dates and 10 different times.

## Requirements

- Python 3.7+
- Pandas
- Faker

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/zuzqqa/hurtownie_danych_generator_2 
    ```

2. Navigate to the project folder:

    ```bash
    cd hurtownie_danych_generator_2 
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Linux/macOS:

      ```bash
      source venv/bin/activate
      ```

    - On Windows:

      ```bash
      .\venv\Scripts\activate
      ```

5. Install the required packages:

    ```bash
    pip install -r data_generator/requirements.txt
    ```

## Usage

### Generating Data

1. Run the data generation script:

    ```bash
    python data_generator/data_generator.py
    ```

   This script will generate the data and save it in the `data/` folder as CSV files:

   - `dates.csv`
   - `times.csv`
   - `ratings.csv`
   - `passengers.csv`
   - `employees.csv`
   - `check_ins.csv`
   - `boarding_passes.csv`
   - `security_checks.csv`

### Inserting Data into Database

1. Run the SQL `CREATE.sql` script to create the tables in the database:

    ```sql
    -- Script: sql_scripts/CREATE.sql
    ```

2. Run the `INSERT.sql` script to load the data into the tables:

    ```sql
    -- Script: sql_scripts/INSERT.sql
    ```

3. The `DROP.sql` script allows you to remove all the tables from the database:

    ```sql
    -- Script: sql_scripts/DROP.sql
    ```

4. The `SELECT.sql` script contains queries to inspect the inserted data and ensure everything is loaded correctly. You can execute it to query and verify the contents of the tables.

    ```sql
    -- Script: sql_scripts/SELECT.sql
    ```

### Project File Structure

```text
data_warehouse_generator/
│
├── data_generator/           # Folder with data generation related files
│   ├── __init__.py           # Package initialization file
│   ├── data_generator.py     # Main script for generating data (your Python data)
│   └── requirements.txt      # Requirements (e.g., Faker, pandas)
│
├── sql_scripts/              # Folder with SQL files
│   ├── CREATE.sql            # Script to create tables
│   ├── INSERT.sql            # Script to insert data
│   ├── DROP.sql              # Script to drop tables
│   └── SELECT.sql            # Script with SELECT queries (for testing)
│
├── data/                     # Folder to store the generated CSV files
│   ├── dates.csv             # Generated CSV file with date data
│   ├── times.csv             # Generated CSV file with time data
│   ├── ratings.csv           # Generated CSV file with rating data
│   ├── passengers.csv        # Generated CSV file with passenger data
│   ├── employees.csv         # Generated CSV file with employee data
│   ├── check_ins.csv         # Generated CSV file with check-in data
│   ├── boarding_passes.csv   # Generated CSV file with boarding pass data
│   └── security_checks.csv   # Generated CSV file with security check data
│
├── README.md                 # This README file with project documentation
├── main.py                   # It runs the data generation process by calling various functions from the data_generator package.
└── .gitignore                # Git ignore file (for virtualenv and other exclusions)
