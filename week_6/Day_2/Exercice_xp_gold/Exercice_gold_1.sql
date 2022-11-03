--1
SELECT rating, count(film_id) FROM film GROUP by rating;
--2
SELECT film_id, title, description, rating FROM film WHERE rating IN ('G','PG-13') AND (film.length/60)<2 AND rental_rate<3 ORDER BY title ASC;
--3
UPDATE customer SET first_name ='Ahldaïr Donald O', last_name='SANGO',email='sangodonald@gmail.com', last_update=CURRENT_DATE WHERE customer_id=1;
--4
UPDATE address SET address='Lafiabougou', district='Houet', phone=0022675484296, last_update=CURRENT_DATE WHERE address_id=(select address_id FROM customer WHERE customer_id=1);
