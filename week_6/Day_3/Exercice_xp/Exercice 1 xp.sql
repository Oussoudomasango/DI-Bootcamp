-- Exercice 1 xp
--1
SELECT * FROM language;
--2
SELECT f.title,f.description,l.name FROM film f INNER JOIN language l ON f.language_id=l.language_id;
--2_1
SELECT f.title,f.description,l.name FROM film f LEFT JOIN language l ON f.language_id=l.language_id;
--2_2
SELECT f.title,f.description,l.name FROM film f RIGHT JOIN language l ON f.language_id=l.language_id;
--3
/*
CREATE TABLE new_film(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL
);*/
INSERT INTO new_film (name) VALUES ('Badman Dawn'),('Balloon Homeward'),('Deep Crusade'),('Crusade Honey'),('Boogie Amelie'),('Candles Grapes'),('Cider Desire'),('Antitrust Tomatoes'),('Blackout Private');
--4
/*
CREATE TABLE customer_review ( 
	review_id SERIAL PRIMARY KEY,
	film_id INTEGER REFERENCES new_film(id) ON DELETE CASCADE,
	language_id INTEGER REFERENCES language(language_id) ON DELETE CASCADE,
	title_review VARCHAR (50),
	score INTEGER,
	review_text TEXT,
	last_udapte DATE
);*/
--5
INSERT INTO customer_review(film_id,language_id,title_review,score,review_text,last_update)
VALUES ((SELECT id FROM new_film WHERE name='Crusade Honey' LIMIT 1),(SELECT language_id FROM language WHERE name='English' LIMIT 1), 'cool',8,'this film very cool','20-09-2012');
--6
-- Avec le DELETE CASCADE il y aura une suppression automatique chez dans la table customer_review

