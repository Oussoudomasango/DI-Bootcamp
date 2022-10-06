-- Exercice 2:
--1
UPDATE film SET language_id=(SELECT language_id FROM language WHERE name='German') WHERE title ilike '%black%';
--2
 SELECT COUNT(*) FROM rental WHERE return_date IS NULL;
--3

SELECT f.title,f.description,f.rental_rate FROM film f 
join inventory i ON f.film_id=i.film_id
join rental r ON r.inventory_id =i.inventory_id
WHERE r.return_date IS NULL
ORDER BY f.rental_rate DESC LIMIT 30;
--4
--5
--6
--6_1
SELECT f.title,f.description,a.first_name,a.last_name
FROM film f join film_actor AS fac ON f.film_id= fac.film_id
join actor a ON fac.actor_id=a.actor_id
WHERE f.description ilike '%sumo wrestler%' AND (a.first_name='Penelope' AND a.last_name='Monroe');
--6_2
SELECT title,description,rating,length FROM film WHERE length = 60 AND rating = 'R';
--6_3
 SELECT f.title, f.rental_rate,r.return_date,c.first_name,c.last_name from film f
 JOIN inventory i ON f.film_id=i.film_id
 JOIN rental r ON i.inventory_id=r.inventory_id
 JOIN customer c ON r.customer_id=c.customer_id
 WHERE f.rental_rate > 4.00 AND r.return_date between
 '28/07/2005' AND '1/08/2005' AND c.first_name='Matthew'
 AND c.last_name='Mahan';
 --6_4
 SELECT f.title,f.description,f.replacement_cost,c.first_name,c.last_name FROM film f
 JOIN inventory i ON f.film_id=i.film_id
 JOIN rental r ON i.inventory_id=r.inventory_id
 JOIN customer c ON r.customer_id = c.customer_id
 WHERE c.first_name='Matthew' AND c.last_name='Mahan' AND
 (f.title ilike '%boat%' or f.description ilike '%boat%')
order by f.replacement_cost desc LIMIT 1;


