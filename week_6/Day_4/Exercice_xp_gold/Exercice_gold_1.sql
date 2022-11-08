--Update Statement
--1 Write a SQL statement to change the following details belonging all employes who’s department_id is 110:
--email column should be: ‘not available’
--commission_pct column should be: 0.10
UPDATE employees SET email='not available' WHERE department_id=110;

--2 Write a SQL statement which will change the email column of all employees to ‘available’ whom work in the ‘Accounting’ department.
UPDATE employees SET email='available' WHERE department_id=(SELECT department_id FROM departments WHERE department_name='Accounting');

--3 Write a SQL statement to change the salary of the employee whose ID is 105. If the existing salary is less than 5000, change it to 8000.
UPDATE employees SET salary=8000 WHERE employee_id=105 AND salary< 5000;

-- Aggregate Functions
--1 Write a query to find the number of jobs available in the employees table.
SELECT COUNT(DISTINCT job_id) FROM employees;

--2 Write a query to get the number of employees working in each post.
SELECT COUNT(employee_id), job_id FROM employees GROUP BY job_id;

--3 Write a query to get the difference between the highest and lowest salaries.
SELECT (MAX(salary)- MIN(salary)) AS difference FROM employees;

--4 Write a query to find a manager ID and the salary of the lowest-paid employee under that manager.
SELECT e.manager_id, e.salary FROM employees e WHERE e.salary=(SELECT MIN(salary) FROM employees WHERE manager_id=e.manager_id);

--5 Write a query to get the average salary for each post excluding Programmer.
SELECT AVG(e.salary) AS Average, j.job_title FROM employees e,jobs j WHERE e.job_id=j.job_id AND j.job_title !='Programmer' GROUP BY j.job_title ;

--6 Write a query to get the average salary for all departments that employ more than 10 employees.
SELECT AVG(e.salary) AS Average, d.department_name FROM employees e,departments d  WHERE e.department_id=d.department_id 
GROUP BY d.department_name HAVING COUNT(employee_id)>10;

--Alter Table Statement
--1 Write a SQL statement to change the name of the column “state_province” to “state” in the locations table, keeping the same data type and size.
ALTER TABLE locations RENAME COLUMN state_province TO state;

--Write a SQL statement to add a primary key to the “location_id” column in the locations table.
ALTER TABLE locations ADD PRIMARY KEY(location_id);

