-- Usuwanie tabel w odpowiedniej kolejnoœci (jeœli istniej¹)

-- Najpierw usuwamy zale¿noœci, aby unikn¹æ problemów z kluczami obcymi
IF EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[SecurityChecks]') AND type IN (N'U'))
DROP TABLE SecurityChecks;

IF EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[BoardingPasses]') AND type IN (N'U'))
DROP TABLE BoardingPasses;

IF EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[CheckIns]') AND type IN (N'U'))
DROP TABLE CheckIns;

IF EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Employees]') AND type IN (N'U'))
DROP TABLE Employees;

IF EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Passengers]') AND type IN (N'U'))
DROP TABLE Passengers;

IF EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Ratings]') AND type IN (N'U'))
DROP TABLE Ratings;

IF EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Times]') AND type IN (N'U'))
DROP TABLE Times;

IF EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Dates]') AND type IN (N'U'))
DROP TABLE Dates;
