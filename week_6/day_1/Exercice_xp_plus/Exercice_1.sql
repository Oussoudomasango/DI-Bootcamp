/*
CREATE TABLE students(
id SERIAL PRIMARY KEY,
first_name VARCHAR (200) NOT NULL,
last_name VARCHAR (100) NOT NULL,
birth_date DATE	NOT NULL
);*/
/*
INSERT INTO students (first_name, last_name, birth_date)
VALUES ('Marc', 'Benichou', '02/11/1998'),
	   ('Yoan', 'Cohen', '03/12/2010'),
	   ('Lea', 'Benichou', '27/07/1987'),
	   ('Amelia','Dux', '07/04/1996'),
	   ('David', 'Grez', '14/06/2003'),
	   ('Omer', 'Simpson', '03/10/1980');*/
/*
INSERT INTO students (first_name, last_name,birth_date)
VALUES ('Donald Ahldaïr Oussoudoma','Sango','10/11/1995');
*/
--1
SELECT * FROM students;
--2
SELECT first_name,last_name FROM students;
--3_1
SELECT first_name,last_name FROM students WHERE id = 2 ;
--3_2
SELECT first_name,last_name FROM students WHERE last_name = 'Benichou' AND first_name = 'Marc';
--3_3
SELECT first_name,last_name FROM students WHERE last_name = 'Benichou' or first_name = 'Marc';
--3_4
SELECT first_name,last_name FROM students WHERE first_name LIKE '%a%'  ;
--3_5
SELECT first_name,last_name FROM students WHERE first_name ILIKE 'a%' ;
--3_6
SELECT first_name,last_name FROM students WHERE first_name LIKE '%a'  ;
--3_7
SELECT first_name,last_name FROM students WHERE first_name LIKE '%a_'  ;
--3_8
SELECT first_name,last_name FROM students WHERE  id = 1  or id= 3 ;