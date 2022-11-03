--1
SELECT first_name, last_name FROM customers ORDER BY last_name DESC LIMIT 2;
--2
DELETE FROM purchases pu WHERE pu.customer_id IN (SELECT id FROM customers WHERE first_name='Scott');
--3
DELETE FROM customers  WHERE first_name='Scott';
SELECT * FROM customers WHERE first_name='Scott';
--4
SELECT * FROM purchases pu LEFT JOIN customers cu ON pu.customer_id=cu.id ;
--SELECT * FROM customers;
--5
SELECT * FROM purchases pu LEFT OUTER JOIN customers cu ON pu.customer_id=cu.id 

