-- Ustawienie umo¿liwiaj¹ce korzystanie z BULK INSERT
EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
EXEC sp_configure 'Ad Hoc Distributed Queries', 1;
RECONFIGURE;

-- BULK INSERT dla tabel

-- Wymiar: Data
BULK INSERT Dates
FROM 'D:\hd\hurtownie_danych_generator_2\dates.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,  -- Pomija nag³ówki
    CODEPAGE = '65001', -- UTF-8
    DATAFILETYPE = 'char'
);

-- Wymiar: Czas
BULK INSERT Times
FROM 'D:\hd\hurtownie_danych_generator_2\times.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
    CODEPAGE = '65001',
    DATAFILETYPE = 'char'
);

-- Wymiar: Oceny
BULK INSERT Ratings
FROM 'D:\hd\hurtownie_danych_generator_2\ratings.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
    CODEPAGE = '65001',
    DATAFILETYPE = 'char'
);

-- Tabela: Pasa¿erowie
BULK INSERT Passengers
FROM 'D:\hd\hurtownie_danych_generator_2\passengers.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
    CODEPAGE = '65001',
    DATAFILETYPE = 'char'
);

-- Tabela: Pracownicy
BULK INSERT Employees
FROM 'D:\hd\hurtownie_danych_generator_2\employees.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
    CODEPAGE = '65001',
    DATAFILETYPE = 'char'
);

-- Tabela: Odprawy
BULK INSERT CheckIns
FROM 'D:\hd\hurtownie_danych_generator_2\check_ins.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
    CODEPAGE = '65001',
    DATAFILETYPE = 'char'
);

-- Tabela: Karty Pok³adowe
BULK INSERT BoardingPasses
FROM 'D:\hd\hurtownie_danych_generator_2\boarding_passes.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
    CODEPAGE = '65001',
    DATAFILETYPE = 'char'
);

-- Tabela: Kontrole Bezpieczeñstwa
BULK INSERT SecurityChecks
FROM 'D:\hd\hurtownie_danych_generator_2\security_checks.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
    CODEPAGE = '65001',
    DATAFILETYPE = 'char'
);
