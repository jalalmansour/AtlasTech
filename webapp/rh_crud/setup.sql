-- AtlasTech HR Database Setup
-- Run this script on the target server to initialize the vulnerable database

CREATE DATABASE IF NOT EXISTS RH;

USE RH;

-- Create user with limited privileges (but misconfigured)
CREATE USER IF NOT EXISTS 'RH'@'localhost' IDENTIFIED BY 'StrongPassword123';
GRANT SELECT, INSERT, UPDATE, DELETE ON RH.* TO 'RH'@'localhost';
FLUSH PRIVILEGES;

-- Employees table (PII stored in plaintext - vulnerability)
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    email VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(10,2),
    ssn VARCHAR(20),          -- Social Security Number in plaintext
    bank_account VARCHAR(30), -- Banking info in plaintext
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Users table for authentication (weak password storage - vulnerability)
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(100),  -- Stored in plaintext - vulnerability
    role VARCHAR(20) DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample employees (with sensitive data)
INSERT INTO employees (firstname, lastname, email, position, salary, ssn, bank_account) VALUES
('Youssef', 'El Amrani', 'y.amrani@atlastech.ma', 'CEO', 45000.00, '123-45-6789', 'MA64 0011 1111 0000 1111 0011 11'),
('Fatima', 'Bennani', 'f.bennani@atlastech.ma', 'CTO', 38000.00, '234-56-7890', 'MA64 0022 2222 0000 2222 0022 22'),
('Omar', 'Alaoui', 'o.alaoui@atlastech.ma', 'Lead Developer', 28000.00, '345-67-8901', 'MA64 0033 3333 0000 3333 0033 33'),
('Khadija', 'Tazi', 'k.tazi@atlastech.ma', 'HR Manager', 25000.00, '456-78-9012', 'MA64 0044 4444 0000 4444 0044 44'),
('Ahmed', 'Fassi', 'a.fassi@atlastech.ma', 'DevOps Engineer', 26000.00, '567-89-0123', 'MA64 0055 5555 0000 5555 0055 55'),
('Salma', 'Idrissi', 's.idrissi@atlastech.ma', 'Frontend Developer', 22000.00, '678-90-1234', 'MA64 0066 6666 0000 6666 0066 66'),
('Mehdi', 'Chraibi', 'm.chraibi@atlastech.ma', 'Backend Developer', 23000.00, '789-01-2345', 'MA64 0077 7777 0000 7777 0077 77'),
('Layla', 'Ouazzani', 'l.ouazzani@atlastech.ma', 'Marketing Manager', 24000.00, '890-12-3456', 'MA64 0088 8888 0000 8888 0088 88');

-- Insert admin user (weak credentials - vulnerability)
INSERT INTO users (username, password, role) VALUES
('admin', 'admin123', 'admin'),
('hr_user', 'hr2024', 'hr'),
('dev', 'developer', 'user');
