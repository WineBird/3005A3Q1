-- easy drop tables, uncomment if needed
/*
DROP TABLE IF EXISTS students CASCADE;
*/
-- CREATE DATABASE a3db;


-- SERIAL essentially translates to INTEGER and AUTO_INCREMENT at the same time - postgresql does not support AUTO_INCREMENT.
CREATE TABLE students
	(
	student_id	SERIAL,
	first_name	TEXT NOT NULL,
	last_name	TEXT NOT NULL,
	email	TEXT	UNIQUE NOT NULL,
	enrollment_date DATE,
	PRIMARY KEY (student_id)
	);

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');