-- Create Tables
--1 Write a SQL statement to create a simple table “new_countries” including columns country_id and country_name.
--make sure that no duplicate data is added to the country_id column (which data type should you use for the column country_id ?)
--make sure that no countries except Italy, India and China will be entered in the table.
/*
CREATE TABLE new_countries(
	country_id SERIAL PRIMARY KEY,
	country_name VARCHAR(20) CHECK(country_name IN ('India','Italy','China'))
);
*/
--2 Write a SQL statement to create a duplicate copy of the “new_countries” table including the structure and the data of the “new_countries” table.
--CREATE TABLE copy_new_countries AS SELECT * FROM new_countries;

--3 Write a SQL statement to create a table named “new_jobs” including columns job_id, job_title, min_salary, max_salary
--make sure that the max_salary column won’t exceed 25000.
--make sure that job_title, min_salary and max_salary have the following default values:
--job_title is blank
--min_salary is 8000
--max_salary is NULL.
/*
CREATE TABLE new_jobs (
	job_id SERIAL PRIMARY KEY,
	job_title VARCHAR(50) DEFAULT '', 
	min_salary INTEGER DEFAULT 8000, 
	max_salary INTEGER CHECK(max_salary<25000) DEFAULT NULL 
);*/

--4 Write an SQL statement to create a table called “new_employees” the table should include the following columns: employee_id, first_name, last_name, email, phone_number hire_date, job_id and salary.
--make sure that, the employee_id column does not contain any duplicate value at the time of insertion,
--make sure that the foreign key column job_id, references the column job_id in the “new_jobs” table.
/*
CREATE TABLE new_employees (
	employee_id INTEGER PRIMARY KEY,
	first_name VARCHAR(50) , 
	last_name VARCHAR(50) , 
	email  VARCHAR(50) , 
	phone_number  VARCHAR(50) ,
	hire_date DATE, 
	job_id INTEGER NOT NULL,
	salary INTEGER NOT NULL,
	FOREIGN KEY(job_id) REFERENCES new_jobs(job_id)
);*/


--5 Write a SQL statement to create a table called “new_job_history” the table should include the following columns: employee_id, start_date, end_date, job_id
--make sure that the foreign key employee_id references the column employee_id in the “new_employees” table.
--make sure that the foreign key job_id is equal to an id that exists in the “new_jobs” table.
/*
CREATE TABLE new_job_history (
	employee_id INTEGER ,
	start_date DATE , 
	end_date DATE, 
	job_id INTEGER NOT NULL,
	FOREIGN KEY(job_id) REFERENCES new_jobs(job_id) ON DELETE SET NULL ON UPDATE SET NULL,
	FOREIGN KEY(employee_id) REFERENCES new_employees(employee_id)
);*/
/*
--1 Write a SQL statement to insert a record with your own value into the “new_countries” table.
INSERT INTO new_countries (country_name) VALUES ('India');

--2 Using only one insert statement insert 3 row of data to the “new_countries” table
INSERT INTO new_countries (country_name) VALUES ('India'),('Italy'),('China');

--3 Write a SQL statement to insert the rows whithin the “new_countries” table to a duplicate table.
INSERT INTO copy_new_countries (country_name) VALUES ('India'),('Italy'),('China');
*/
/*
--4 Write a SQL statement to insert data into the “new_employees” table, the job_id column must contain values which exist in the “new_jobs” table.
INSERT INTO new_jobs (job_title, min_salary, max_salary) VALUES ('Programmer',20000,22000);
*/
/*
INSERT INTO new_employees (employee_id, first_name, last_name, email, phone_number ,hire_date, job_id,salary) 
VALUES (1,'Donald Ahldaïr Oussoudoma','SANGO','sangodonald@gmail.com','0022675484296','2022-11-07',(SELECT job_id FROM new_jobs WHERE job_title='Programmer'),50000);
*/