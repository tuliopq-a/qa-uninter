-- ================================
-- CRIAÇÃO DAS TABELAS SGHSS
-- ================================

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'doctor', 'nurse', 'patient') NOT NULL
);

CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    birth_date DATE NOT NULL
);

CREATE TABLE appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_name VARCHAR(100) NOT NULL,
    appointment_date DATETIME NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patients(id)
);

-- ================================
-- DADOS DE MOCK
-- ================================

INSERT INTO      (cpf, password, role)
VALUES 
('12345678901', 'senha123', 'patient'),
('98765432100', 'doctorpass', 'doctor'),
('11122233344', 'adminpass', 'admin');

INSERT INTO patients (name, cpf, birth_date)
VALUES
('João Silva', '12345678901', '1990-04-12'),
('Maria Oliveira', '55566677788', '1985-10-20');

INSERT INTO appointments (patient_id, doctor_name, appointment_date)
VALUES
(1, 'Dr. Renato', '2025-01-20 14:00:00'),
(1, 'Dra. Ana', '2025-01-22 09:00:00'),
(2, 'Dr. Paulo', '2025-01-23 16:30:00');
