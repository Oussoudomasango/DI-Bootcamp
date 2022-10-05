--Exercice 2
--1
SELECT * FROM customer;
--2
SELECT first_name|| ' '|| last_name AS full_name FROM customer;
--3
SELECT DISTINCT create_date FROM customer;
--4
SELECT * FROM customer ORDER BY first_name DESC;
--5
SELECT film_id, title, description,release_year, rental_rate FROM film ORDER BY rental_rate ASC;
--6
SELECT address, phone FROM address WHERE district = 'Texas';
--7
SELECT * FROM film WHERE film_id='15' OR film_id='150';
--8
SELECT film_id, title, description, length,rental_rate  FROM film WHERE title= 'Desert Poseidon';
--9
SELECT film_id, title, description,length,rental_rate FROM film WHERE title LIKE 'De%';
--10
SELECT film_id, title, description, length,replacement_cost FROM film ORDER BY replacement_cost LIMIT 10;
--11
SELECT film_id, title, description, length,replacement_cost FROM film ORDER BY replacement_cost OFFSET 10 LIMIT 10;
--12
SELECT customer.first_name ||' '||customer.last_name AS full_name,payment.amount,payment.payment_date FROM customer inner join payment on customer.customer_id=payment.customer_id ORDER BY customer.customer_id;
--13




