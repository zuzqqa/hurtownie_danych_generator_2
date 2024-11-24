-- Wymiar: Date
CREATE TABLE Dates (
    DateID INT PRIMARY KEY,
    Date DATE NOT NULL,
    Day INT NOT NULL,
    Month INT NOT NULL,
    Year INT NOT NULL,
    DayOfWeek VARCHAR(20) NOT NULL,
    IsWeekend BIT NOT NULL, -- BIT: 0 = False, 1 = True
    WeekOfYear INT NOT NULL
);

-- Wymiar: Time
CREATE TABLE Times (
    TimeID INT PRIMARY KEY,
    Time TIME NOT NULL,
    Hour INT NOT NULL,
    Minute INT NOT NULL,
    Shift VARCHAR(20) NOT NULL
);

-- Wymiar: Rating
CREATE TABLE Ratings (
    RatingID INT PRIMARY KEY,
    RatingCategory VARCHAR(50) NOT NULL,
    RatingDescription TEXT
);

-- Wymiar: Passenger
CREATE TABLE Passengers (
    PassengerID INT PRIMARY KEY,
    FirstAndLastName VARCHAR(100) NOT NULL,
    DocumentType VARCHAR(20) NOT NULL,
    Nationality VARCHAR(100) NOT NULL,
    IsCurrent BIT NOT NULL -- BIT: 0 = False, 1 = True
);

-- Wymiar: Employee
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    EmployeeName VARCHAR(100) NOT NULL,
    ExperienceCategory VARCHAR(20) NOT NULL,
    AgeCategory VARCHAR(20) NOT NULL,
    Gender VARCHAR(10) NOT NULL,
    IsCurrent BIT NOT NULL -- BIT: 0 = False, 1 = True
);

-- Fakt: Check-Ins
CREATE TABLE CheckIns (
    CheckInID INT PRIMARY KEY,
    PassengerID INT NOT NULL,
    EmployeeID INT NOT NULL,
    BoardingPassID INT NOT NULL,
    DateID INT NOT NULL,
    TimeID INT NOT NULL,
    RatingID INT NOT NULL,
    CheckInDuration INT NOT NULL,
    BaggageCount INT NOT NULL,
    ServiceRating DECIMAL(3, 2) NOT NULL,
    FOREIGN KEY (PassengerID) REFERENCES Passengers(PassengerID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
    FOREIGN KEY (DateID) REFERENCES Dates(DateID),
    FOREIGN KEY (TimeID) REFERENCES Times(TimeID),
    FOREIGN KEY (RatingID) REFERENCES Ratings(RatingID)
);

-- Fakt: Boarding Passes
CREATE TABLE BoardingPasses (
    BoardingPassID INT PRIMARY KEY,
    Gate VARCHAR(10) NOT NULL,
    SeatNumber VARCHAR(10) NOT NULL,
    Destination VARCHAR(100) NOT NULL,
    FlightNumber VARCHAR(20) NOT NULL
);

-- Fakt: Security Checks
CREATE TABLE SecurityChecks (
    SecurityCheckID INT PRIMARY KEY,
    EmployeeID INT NOT NULL,
    BoardingPassID INT NOT NULL,
    DateID INT NOT NULL,
    TimeID INT NOT NULL,
    RatingID INT NOT NULL,
    SecurityDuration INT NOT NULL,
    ClearanceStatus VARCHAR(20) NOT NULL,
    ServiceRating DECIMAL(3, 2) NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
    FOREIGN KEY (BoardingPassID) REFERENCES BoardingPasses(BoardingPassID),
    FOREIGN KEY (DateID) REFERENCES Dates(DateID),
    FOREIGN KEY (TimeID) REFERENCES Times(TimeID),
    FOREIGN KEY (RatingID) REFERENCES Ratings(RatingID)
);
